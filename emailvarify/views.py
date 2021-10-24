

from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
#from .forms import UserForms
from django.contrib.auth.models import User
from .models import Profile
import uuid
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

def sendmail(email,token):
    subject = 'Varify Email'
    message = 'Hello User please activate your account '+'http://127.0.0.1:8000/email/varify/'+token
    from_email = 'praveenyadav1602@gmail.com'
    recipient_list = [email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

class Home(View):
    def get(self,request):
        return render(request, "emailvarify/home.html")


class SignUpView(View):
    def get(self,request):
        return render(request,'emailvarify/signup.html')        
    def post(self,request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,password=password,email=email)
        messages.success(request,"You Have Successfully registered! Now you can login after activating your email! check your email",)
        uid = uuid.uuid4()
        st = str(uid)
        pf = Profile(user=user,token=st)
        pf.save()
        sendmail(user.email,st)
        return render(request,'emailvarify/signup.html',)


def varify(request,token):
    p = Profile.objects.get(token=token)
    xp = p.varify
    p.varify = True
    p.save()
    messages.success(request,"Email Varified, Now You Can Login",)
        

    # if y.token == token:
    #     print('token Match')
    # else:
    #     print('Token mismatch') 
    return redirect('/email/login/')    

from django.contrib.auth import authenticate, login, logout
class loginf(View):           
    def get(self, request):
         return render(request,'emailvarify/login.html')
    def post(self,request):
        username = request.POST.get('exampleInputEmail1')
        password = request.POST.get('exampleInputPassword1')
        print(username,password)
        #msg = None
        user = authenticate(username=username, password=password)
        if user is not None:
            print("will not be")
            pf = Profile.objects.get(user=user)
            print(user)
            if pf.varify == False:
                messages.warning(request,"First Activate Your Email")
                print('activate email')
                return render(request,'emailvarify/login.html',)
            else:
                login(request, user)
                print('success')
                return redirect('/email/loginss/')
        else:
            print('wrong Email or Password')    
            return render(request,'emailvarify/login.html',)

def loginss(request):
    return render(request,'emailvarify/logedin.html')


def logoutt(request):
    logout(request) 
    return render('emailvarify/home.html')   
