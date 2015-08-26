from django.shortcuts import render,render_to_response,redirect
import datetime
from .models import Testing

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse

#from .forms import NameForm

def hello(request):
    userinfolist=Testing.objects.all().order_by('submittedtime')
    if 'user_name' in request.POST:
        username=request.POST['user_name']
        phonenumber=request.POST['phone_number']
        comments = request.POST['comments']
        submittedtime = datetime.datetime.now()
        userinfo=Testing.objects.create(name=username,phone=phonenumber,comments=comments,submittedtime=submittedtime)
        userinfo.save()
        return render_to_response('welcome.html',locals())
        #{"username":yourname, "phonenumber":phonenumber}) 
    else:
        return render_to_response('welcome.html',locals())


def hellorefresh(request):
    if 'deletelist' in request.POST:
        Testing.objects.filter(id__in=request.POST.getlist('checkDelete')).delete() 
    userinfolist=Testing.objects.all().order_by('submittedtime')    
    return render_to_response('welcome.html',locals())

def testingajax(reqeust,num="0"): #if num="0" doesn't provide, it will show the error message: testingajax() takes exactly 2 arguments (1 given)
    if num=='1':
        return render_to_response("today.html")
    elif num=='2':
        return render_to_response("yesterday.html")
    elif num=='3':
        return render_to_response("lastweek.html")
    else:
        return render_to_response("load.html")

