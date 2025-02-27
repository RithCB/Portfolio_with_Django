from django.core.mail import send_mail, BadHeaderError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render,HttpResponse,redirect
from .models import Journal, Project, Certification, MessageContact
from django.conf import settings
from django.contrib import messages

def getPage(request):
    certification_data = Certification.objects.all()
    project_data = Project.objects.all()
    journal_data = Journal.objects.all()
    
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        # Validate email before proceeding
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'contact_fail.html', {'error': 'Invalid email address.'})

        # if username and email and message:
        #     MessageContact.objects.create(Username=username, Email=email, Message=message)

        subject = f"New Message from {username} ({email})"
        message_content = f"\n\nMessage \n\n{message}\n\nFrom: {username}\nEmail: {email}"

        try:
            email_sent = send_mail(
                subject,
                message_content,
                email,  # The user's email is used as the sender
                [settings.EMAIL_HOST_USER],  # You receive the message
                fail_silently=False,
            )
        except BadHeaderError:
            return render(request, 'contact_fail.html', {'error': 'Invalid email header.'})
        except Exception as e:
            return render(request, 'contact_fail.html', {'error': str(e)})

        if email_sent:
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/')  # Redirects to home page
        else:
            return render(request, 'contact_fail.html', {'error': 'Failed to send message. Please try again.'})
    
    context = {
        'certification_data': certification_data,
        'project_data': project_data,
        'journal_data': journal_data,
    }

    return render(request, 'index.html', context)
