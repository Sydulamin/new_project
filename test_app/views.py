from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.db.models import F
import time

def index(request):
   
   '''
   name = 'Ridoy'
   age = 200
   stu = Students.objects.all().update(age=F('age') * 1.50
   )
   for i in stu:
      print(i.Name , i.age)
   print(stu)
   return render(request, 'Home/home.html', {'na': name, 'a': age
   })
   
   '''
   
   
   #hi
   # stu = Students.objects.all()
   # for i in stu:
   #    print(i.Name , i.age)
   # print(stu.Name , stu.age)
   # name = None
   # age = None
   # if request.method == 'POST':
   #    name = request.POST.get('name')
   #    if name:
   #       stu = Students.objects.filter(Q(Name__icontains=name) | Q(Name__iexact=name))
      
   #    age = request.POST.get('age')
   #    print(f"Name: {name}, Age: {age}")
   
   time_start = time.time()
   th = TeacherName.objects.filter(subject__className__name='Class 6')
   print(f'1st querry -{time.time() - time_start} seconds')
   print(th)
   
   
   time_start = time.time()
   teachers = TeacherName.objects.select_related("subject__className").filter(subject__className__name="Class 6")
   print(f'2nd querry -{time.time() - time_start} seconds')
   
   print(teachers)
   
   
   time_start = time.time()
   teachers = TeacherName.objects.prefetch_related("subject__students_set").filter(subject__className__name="Class 6")
   print(f'3rd querry -{time.time() - time_start} seconds')
   
   print(teachers)
   
   return render(request, 'Home/home.html'
   # {
   #    # 'na': name,
   #    # 'a': age,
   #    # 'stu' : stu
   # }
   )

def about(request):
   # name = 'Ridoy'
   # age = 200
   # stu = Students.objects.all().update(age=F('age') * 1.50)
   # for i in stu:
   #    print(i.Name , i.age)
   # print(stu)
   
   return render(request, 'Home/about.html')