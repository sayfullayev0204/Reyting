from django.shortcuts import render, redirect,get_object_or_404
from .models import Student, Score,Priz,Category
from django.db.models import Sum

def index(request):
    bolimlar_list = Category.objects.all()
    return render(request, 'index.html', {'bolimlar_list': bolimlar_list})

def student_list(request, category_id):
    category = Category.objects.get(pk=category_id)
    students = Student.objects.annotate(total_score=Sum('score__score')).order_by('-total_score').filter(category=category)
    for student in students:
        scores = Score.objects.filter(student=student)
        total_score = sum(score.score for score in scores)
        student.total_score = total_score
    return render(request, 'home.html', {'category': category, 'students': students})

def add_score(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        Nomi = request.POST['Nomi']
        img = request.FILES['img']
        date = request.POST['date']
        score = request.POST['score']
        Izoh = request.POST['Izoh']
        Score.objects.create(student=student, Nomi=Nomi, img=img, date=date, score=score, Izoh=Izoh)
        return redirect('student_list')

def student_details(request, student_id):
    student = Student.objects.get(pk=student_id)
    scores = Score.objects.filter(student=student)
    total_score = sum(score.score for score in scores)
    return render(request, 'm.html', {'student': student, 'scores': scores, 'total_score': total_score})

def priz(request):
    priz=Priz.objects.all()
    return render(request, 'priz.html', {'priz': priz})