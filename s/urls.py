from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('category/<int:category_id>/', views.student_list, name='student_list'),
    path('add_score/<int:student_id>/', views.add_score, name='add_score'),
    path('details/<int:student_id>/', views.student_details, name='student_details'),
    path('priz/',views.priz, name='priz'),
    
]
