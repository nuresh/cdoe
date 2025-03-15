from django.contrib import admin
from .models import Student, Department, Recruiter, Product, Service, Job, NoticeType, Notice

# Register your models here.
# admin.site.register(ADMIN)
# admin.site.register(STUDENT)

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Recruiter)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Job)
admin.site.register(NoticeType)
admin.site.register(Notice)
