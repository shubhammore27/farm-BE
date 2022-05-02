from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def registerUserMail(email, name, otherTeamMembers):
    template = render_to_string('registerUser.html', {'name' :name, 'otherTeamMembers': otherTeamMembers})
    msg = EmailMultiAlternatives('Registration Successfull',template, 'shubham.more26@gmail.com', [email])
    msg.content_subtype = 'html'
    msg.send()

def emailVerification(email, otp):
    template = render_to_string('emailVerification.html', {'email' :email, 'otp': otp})
    msg = EmailMultiAlternatives('Email Verification',template, 'shubham.more26@gmail.com', [email])
    msg.content_subtype = 'html'
    msg.send()
    
    