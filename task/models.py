from django.db import models
from simple_history.models import HistoricalRecords
from dashboard.models import Phone, Desktop, Laptop
from user.models import User, Profile
# Create your models here.
DeviceType = (
    ('phones', 'phone'),
    ('desktop', 'desktop'),
    ('laptop', 'laptop',)
)
rq_type = (
    ('issuance', 'issuance'),
    ('movement', 'movement'),
    ('repair', 'repair'),
    ('maintenance', 'maintenance'),
) 
st = (
    ('open', 'open'),
    ('Verified', 'Verified'),
    ('Closed', 'Closed'),
)


class Task_Request(models.Model):
    request_number = models.IntegerField()
    request_type = models.CharField(max_length=100, choices=rq_type)
    device = models.CharField(max_length=100)
    device_serial = models.CharField(max_length=250)
    assigned = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task_assigned')
    subject = models.CharField(max_length=250)
    last_updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=st, default='open')
    history = HistoricalRecords()


    def __str__(self) -> str:
        return f'{self.request_number} - {self.request_type} - {self.device} - {self.status}'


class Issuance(models.Model):
    request_number = models.IntegerField(unique=True)
    request_type = models.CharField(max_length=100, default='Issuance')
    device = models.CharField(max_length=100, choices=DeviceType)
    device_serial = models.CharField(max_length=250)
    requester = models.ForeignKey(User,  on_delete = models.SET_NULL, null=True, related_name='Issuance_requester')
    Issued = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Issued_to')
    Approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Approved_by')
    Technician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Issuance_Tech')
    subject = models.CharField(max_length=250)
    comment = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=st, default='open')
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate the number if the object is being created
            last_object = Issuance.objects.order_by('-request_number').first()
            if last_object:
                last_number = last_object.request_number
                new_number = last_number + 1
            else:
                new_number = 1000  # Starting number when no objects exist yet
            self.request_number = new_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.request_number} - {self.request_type} - {self.device} - {self.status}'


class Assign(models.Model):
    request_number = models.IntegerField(unique=True)
    request_type = models.CharField(max_length=100, default='issuance')
    device = models.CharField(max_length=100)
    device_serial = models.CharField(max_length=250)
    requester = models.ForeignKey(User,  on_delete = models.SET_NULL, null=True, related_name='assign_requester')
    Assigned = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='assigned_to')
    Technician = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='Assign_Tech')
    comment = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=st, default='open')
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate the number if the object is being created
            last_object = Assign.objects.order_by('-request_number').first()
            if last_object:
                last_number = last_object.request_number
                new_number = last_number + 1
            else:
                new_number = 1000  # Starting number when no objects exist yet
            self.request_number = new_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.request_number} - {self.request_type} - {self.device} - {self.status}'

class Repair(models.Model):
    request_number = models.IntegerField(unique=True)
    request_type = models.CharField(max_length=100, default='repair')
    device = models.CharField(max_length=100)
    device_serial = models.CharField(max_length=250)
    requester = models.ForeignKey(User,  on_delete = models.SET_NULL, null=True, related_name='repair_requester')
    Assigned = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='assign_repair')
    R_Technician = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='Repair_Tech')
    comment = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=st, default='open')
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate the number if the object is being created
            last_object = Repair.objects.order_by('-request_number').first()
            if last_object:
                last_number = last_object.request_number
                new_number = last_number + 1
            else:
                new_number = 2000  # Starting number when no objects exist yet
            self.request_number = new_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.request_number} - {self.request_type} - {self.device} - {self.status}'
    
class Movement(models.Model):
    request_number = models.IntegerField(unique=True)
    request_type = models.CharField(max_length=100, default='movement')
    device = models.CharField(max_length=100)
    device_serial = models.CharField(max_length=250)
    requester = models.ForeignKey(User,  on_delete = models.SET_NULL, null=True, related_name='move_requesters')
    Assigned = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assign_move')
    move_Technician = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='move_tech')
    comment = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=st, default='open')
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate the number if the object is being created
            last_object = Movement.objects.order_by('-request_number').first()
            if last_object:
                last_number = last_object.request_number
                new_number = last_number + 1
            else:
                new_number = 3000  # Starting number when no objects exist yet
            self.request_number = new_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.request_number} - {self.request_type} - {self.device} - {self.status}'
"""
class Maintenance(models.Model):
    request_number = models.IntegerField(unique=True)
    request_type = models.CharField(max_length=100, default='maintenance')
    device = models.CharField(max_length=100)
    device_serial = models.CharField(max_length=250)
    last_updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=st, default='open')
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate the number if the object is being created
            last_object = Request.objects.order_by('-request_number').first()
            if last_object:
                last_number = last_object.request_number
                new_number = last_number + 1
            else:
                new_number = 4000  # Starting number when no objects exist yet
            self.request_number = new_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.request_number} - {self.request_type} - {self.device} - +{self.status}'
"""

