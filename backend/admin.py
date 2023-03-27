from django.contrib import admin
from .models import User,DoctorProfile,Hospital,Report
# Register your models here.
admin.site.register(User)
admin.site.register(DoctorProfile)
admin.site.register(Hospital)
admin.site.register(Report)