from django.db import models
from django.contrib.auth.models import User 

class customer_detail(models.Model):
    by_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  
    which_call = models.CharField(max_length=120,null=True)
    name = models.CharField(max_length=26,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=16,null=True)
    alternate_phone = models.CharField(max_length=16,null=True)
    billing_address = models.TextField(null=True)
    member_of_family = models.TextField(null=True)
    worth = models.CharField(max_length=50)
    favourable_apps = models.TextField(null=True)
    next_followup = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,editable=False)

    def __str__(self) -> str:
        return "Which call: {}, Name: {}".format(self.which_call,self.name)

class reminders(models.Model):
    for_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    time = models.DateTimeField(null=True)
    reminder = models.TextField(null=True)

    def __str__(self) -> str:
        return "user: {}, time: {}, reminder: {}".format(self.for_user,self.time,self.reminder)

class notes(models.Model):
    by_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    notepad = models.TextField(null=True)

    def __str__(self) -> str:
        return self.by_user.username
