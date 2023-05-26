from django.contrib import admin
from .models import User, Applicant, Employer
# , Admin

admin.site.register(User)
admin.site.register(Applicant)
admin.site.register(Employer)
# admin.site.register(Admin)
