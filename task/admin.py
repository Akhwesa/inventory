from django.contrib import admin
from .models import Task_Request, Repair, Movement, Issuance

# Register your models here.
admin.site.register(Task_Request)
admin.site.register(Issuance)
admin.site.register(Repair)
admin.site.register(Movement)
