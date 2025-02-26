from django.shortcuts import render
from .models import Journal,Project,Certification,MessageContact
from django.conf import settings

# Create your views here.
def hello(request):
    return render(request, 'index.html')

def getPage(request):
    certification_data = Certification.objects.all()
    project_data = Project.objects.all()
    journal_data = Journal.objects.all()
    context = {
        'certification_data': certification_data,
        'project_data': project_data,
        'journal_data': journal_data,
    }
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if username and email and message:
            MessageContact.objects.create(Username=username, Email = email, Message = message)

    

    return render(request,'index.html',context,)


    

