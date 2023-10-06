from django.contrib import admin
from .models import Profile, Supervisor, Officer, Assistant
# Register your models here.
admin.site.register(Profile)
admin.site.register(Supervisor)
admin.site.register(Assistant)
admin.site.register(Officer)

