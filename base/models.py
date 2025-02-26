from django.db import models

# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    Project_name = models.CharField(max_length=50)
    project_image = models.CharField(max_length=255, default="project image")
    description = models.CharField(max_length=255)
    git_repo = models.CharField(max_length=100,default="github_repo")
    link = models.CharField(max_length=255)


class Certification(models.Model):
    Course_name = models.CharField(max_length=50)
    Certi_image = models.CharField(max_length=255, default='image')
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class MessageContact(models.Model):
    Username = models.CharField(max_length=100,default="name")
    Email = models.EmailField(max_length=200)
    Message = models.CharField(max_length=255)

