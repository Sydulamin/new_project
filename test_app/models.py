from django.db import models

# Create your models here.
    
class ClassName(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class SubjectName(models.Model):
    name = models.CharField(max_length=100)
    className = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class TeacherName(models.Model):
    name = models.CharField(max_length=100)
    subject = models.OneToOneField(SubjectName, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=100)
    roll = models.PositiveBigIntegerField()
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    SubjectName = models.ManyToManyField(SubjectName)
    
    def __str__(self):
        return self.name