from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    type=models.CharField(max_length=90)

class staff(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=90)
    lname=models.CharField(max_length=90)
    place=models.CharField(max_length=90)
    phno=models.BigIntegerField()
    email=models.CharField(max_length=90)

class parent(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=90)
    lname=models.CharField(max_length=90)
    place=models.CharField(max_length=90)
    address=models.CharField(max_length=90)
    phno=models.BigIntegerField()
    email = models.CharField(max_length=90)

class tips(models.Model):
    sid=models.ForeignKey(staff,on_delete=models.CASCADE)
    tips=models.CharField(max_length=90)
    date=models.DateField()

class stdymtrls(models.Model):
    sid = models.ForeignKey(staff, on_delete=models.CASCADE)
    name=models.CharField(max_length=90)
    file=models.FileField()
    date=models.DateField()

class rating(models.Model):
    pid = models.ForeignKey(parent, on_delete=models.CASCADE)
    sid = models.ForeignKey(staff, on_delete=models.CASCADE)
    rating=models.CharField(max_length=90)
    review=models.CharField(max_length=90)
    date=models.DateField()

class feedback(models.Model):
    pid = models.ForeignKey(parent, on_delete=models.CASCADE)
    sid = models.ForeignKey(staff, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=90)
    date = models.DateField()

class chat(models.Model):
    pid=models.ForeignKey(login,on_delete=models.CASCADE ,related_name='pid')
    sid = models.ForeignKey(login, on_delete=models.CASCADE)
    message=models.CharField(max_length=90)
    date = models.DateField()

class classwork(models.Model):
    sid = models.ForeignKey(staff, on_delete=models.CASCADE)
    works = models.CharField(max_length=90)
    subject= models.CharField(max_length=90)
    date = models.DateField()










