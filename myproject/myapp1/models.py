from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    enrollment_date = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return f"Contact from {self.name} - {self.email}"