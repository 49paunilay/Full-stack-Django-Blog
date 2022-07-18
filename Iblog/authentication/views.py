from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def signin(request):
    if request.POST:
        signinEmail = request.POST.get('signinEmail')
        signinPassword = request.POST.get('signinPassword')
        user = authenticate(username=signinEmail,password=signinPassword)
        if user != None:
            login(request,user)
            messages.success(request, "Signed IN ! Welcome to IBlog "+str(user.username) )
            return redirect('/')
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.POST:
        signupEmail = request.POST['signupEmail']
        signupPassword = request.POST['signupPassword']
        userNamesignup = request.POST['userName']
        if signupPassword != None and signupEmail != None and len(signupPassword)>3 and userNamesignup !=None:
            user = User.objects.create_user(userNamesignup,signupEmail,signupPassword)
            user.save()
            messages.success(request, "Signed Up ! Welcome to IBlog "+userNamesignup )

            send_mail(
            'Welcome to Iblog',
            'Hi ! {} We are thrilled to have you onboard ! \n 🥳 🥳 🥳 🥳 '.format(userNamesignup),
            settings.EMAIL_HOST_USER,
            [signupEmail],
            fail_silently=False,)

            context = {
                'user':user
            }
            return redirect('/',context)
    return redirect('/')

def forgetpassword(request):
    return HttpResponse('<html><body>Forget Password</body></html>')

def signout(request):
    if request.POST:
        logout(request)
        messages.success(request, "Logged out" )
    return redirect('/')