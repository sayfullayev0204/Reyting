from django.db import models

class Category(models.Model):
    Nomi = models.CharField(max_length=200, blank=True)
    img=models.ImageField(upload_to='category')
    def __str__(self):
        return self.Nomi
class Student(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')
    def __str__(self):
        return self.name
class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Nomi = models.CharField(max_length=200)
    img = models.ImageField(upload_to='izoh', blank=True)
    date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    Izoh = models.TextField()    
    def __str__(self):
        return self.Nomi

class Priz(models.Model):
    Nomi = models.CharField(max_length=200)
    score= models.IntegerField()
    img = models.ImageField(upload_to='priz')
    def __str__(self):
        return self.Nomi