from django.contrib import admin

from .models import CV, WorkExperience, Education

admin.site.register(CV)
admin.site.register(WorkExperience)
admin.site.register(Education)
