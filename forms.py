from django import forms
from django.core.validators import RegexValidator


#Create form to enable signing up
class signupForm(forms.Form):
   fname=forms.CharField(max_length=30)
   lname=forms.CharField(max_length=30)
   email=forms.EmailField()
   phone=forms.CharField()
   passwd=forms.CharField(widget=forms.PasswordInput())
   confirmpasswd=forms.CharField(widget=forms.PasswordInput(),label='confirm password')
#method to validate the phone number to ensure it conforms to twilio app requirements   
   def clean_phone(self):
       phone_regex=RegexValidator(regex=r'^\+\d{9,15}$',message='Enter phone number in the format +9999999999.Upto 15 digits allowed')
       phone=forms.CharField(validators=[phone_regex])
       if not phone:
            raise forms.ValidationError("Enter phone Number in the correct format")

       return self.cleaned_data.get('phone')
   def clean_confirmpasswd(self):
       pass1=self.cleaned_data.get('passwd')
       pass2=self.cleaned_data.get('confirmpasswd')
       if not pass1:
          raise forms.ValidationError("Enter Password!")
       if not pass2:
          raise forms.ValidationError("You must confirm your password")
       if pass1 != pass2:
          raise forms.ValidationError("passwords do not match")
       return self.cleaned_data.get('confirmpasswd')
   def clean_fname(self):
       fname=self.cleaned_data.get('fname')
       if not fname:
          raise forms.ValidationError("Enter first name.")
       return self.cleaned_data.get("fname")
   def clean_lname(self):
       lname=self.cleaned_data.get("fname")
       if not lname:
          raise forms.ValidationError("Enter Last name")
       return self.cleaned_data.get("lname")
   def clean_email(self):
       email=self.cleaned_data.get("email")
       if not email:
          raise forms.ValidationError("Enter your Email")
       return self.cleaned_data.get("email")
        

