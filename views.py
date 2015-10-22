from django.shortcuts import render
from django.shortcuts import redirect
from authApp.forms import signupForm
from django.http import request
from django.core.mail import send_mail
#from twilio.rest import TwilioRestClient
import string
import random
def signup(request):
   if request.method == 'POST':
      form=signupForm(request.POST)
      if form.is_valid():
         cd=form.cleaned_data
         #sends mail with link to login
         #commented out due to non-compatibility of mail servers
         # send_mail('url link to login','/login/',cd.get('email'),['danielkarama@gmail.com'],)
         #send_mail goes here
         return redirect('/login/')
     
   else:
       form=signupForm()
   return render(request,"signup.html",{'form':form})

def login(request):
   #Account sid and auth token commented out for security reasons
   # ACCOUNT_SID="ACXXXXXXXXXXXXXXXXXXXXXX"
   # AUTH_TOKEN="64YYYYYYYYYYYYYYYYYYYYYYY"
   #client=TwilioRestClient(ACCOUNT_SID,AUTH_TOKEN)
   #client.messages.create( body=captcha, to=phone, from_="+12012895291", )
   #capthcha generating code goes here
   char=string.ascii_uppercase+string.digits
   captcha=''.join(random.choice(char)for _ in range(5))
   if request.method == "POST":
      if captcha==request.POST.get("cpt"):
         message='Successfully entered correct captcha code'
         return render(request,"login.html",{'captcha':captcha,'message':message})
   message=''
   return render(request,"login.html",{'captcha':captcha,'message':message})

# Create your views here.
