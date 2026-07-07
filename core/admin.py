from django.contrib import admin

from .models import *

admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Certificate)