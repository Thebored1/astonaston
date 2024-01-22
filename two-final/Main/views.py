from django.shortcuts import render, redirect
from Main.models import *
from Main.form import *
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.html import strip_tags
from datetime import datetime



def post(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return context

def blog(request):
    context = post(request)

    return render(request, 'blog.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def index(request):
    context = post(request)

    return render(request, "index.html", context)

def career(request):
    careers = Career.objects.all()
    return render(request, 'career.html', {'careers': careers})

def career_detail(request, slug):
    career = Career.objects.get(slug=slug)
    form = CareerForm()
    if request.method == "POST":
        form = CareerForm(request.POST, request.FILES)
        form.instance.job = career.title
        if form.is_valid():
            form.instance.job = career.title
            form.save()

            job = career.title
            name = form['name'].value()
            email = form['email'].value()
            experience = form['experience'].value()
            date_added = datetime.now()
            phone_no = form['phone_no'].value()
            
            subject = 'New Career Form Fill-Up'
            html_message = render_to_string('job-mail.html', {'name': name, 'email': email, 'job': job, 'experience': experience, 'date_added': date_added, 'phone_no': phone_no })
            plain_message = strip_tags(html_message)
            from_email = email
            to = [
                'rrahulchandraakr2@gmail.com', 
                'rrahulchandraakr1@gmail.com'
            ]


            mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
            return render(request, 'sucessfull.html')
        else:
            q = form.errors
            return render(request, 'career-detail.html', {'form': form, 'q': q})
        
    context = {'form': form, 'career': career}
    return render(request, 'career-detail.html', context)



def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            name = form['name'].value()
            email = form['email'].value()
            phone_no = form['phone_no'].value()
            message = form['description'].value()
            date_added = datetime.now()
            
            subject = 'New Contact Form Fill-Up'
            html_message = render_to_string('contact_mail.html', {'name': name, 'email': email, 'phone_no': phone_no, 'message': message, 'date_added': date_added })
            plain_message = strip_tags(html_message)
            from_email = email
            to = [
                'rrahulchandraakr2@gmail.com', 
                'rrahulchandraakr1@gmail.com'
            ]

            mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
            return render(request, 'sucessfull.html')
    
        else:
            q = form.errors
            return render(request, 'contact-us.html', {'form': form, 'q': q})
    return render(request, "contact-us.html", {'form': form})

def about(request):
    return render(request, "about-us.html")

def service(request):
    return render(request, "service.html")

def automation(request):
    return render(request, "services/automation.html")

def functional(request):
    return render(request, "services/functional.html")

def performance(request):
    return render(request, "services/performance.html")

def application(request):
    return render(request, "services/application.html")

def cloud(request):
    return render(request, "services/cloud.html")

def mobile(request):
    return render(request, "services/mobile.html")

def data(request):
    return render(request, "services/data.html")

def cx(request):
    return render(request, "services/cx.html")

def game(request):
    return render(request, "services/game.html")

def integration(request):
    return render(request, "services/integration.html")

def iot(request):
    return render(request, "services/iot.html")


def devops(request):
    return render(request, "services/devops.html")

def sales(request):
    return render(request, "services/sales.html")

def rpa(request):
    return render(request, "services/rpa.html")

def accessibility(request):
    return render(request, "services/accessibility.html")
