from django.db import models
from django.utils import timezone

class Application(models.Model):
    application_type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    problem = models.TextField(blank=True)
    address = models.CharField(max_length=50)
    post_time = models.DateTimeField(default=timezone.now)
    complete_time = models.DateTimeField(null=True)
    message_id = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    act_name = models.CharField(max_length=255)
    
    workers = models.ManyToManyField('Worker', through='ApplicationWorkerAssociation')

class Worker(models.Model):
    worker_type = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    user_id = models.CharField(max_length=50)
    additional_info = models.TextField(blank=True)
    
    applications = models.ManyToManyField('Application', through='ApplicationWorkerAssociation')

class ApplicationWorkerAssociation(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    comment = models.CharField(max_length=255)

class Service(models.Model):
    service_type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    services = models.CharField(max_length=350)
    photo = models.ImageField(upload_to=None, max_length=100)
    price = models.IntegerField(default=0)
