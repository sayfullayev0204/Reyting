from django.contrib import admin

# Register your models here.
from .models import Student,Score,Priz,Category
admin.site.register(Student)
admin.site.register(Score)
admin.site.register(Priz)
admin.site.register(Category)