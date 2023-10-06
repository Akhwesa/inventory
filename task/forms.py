from django import forms
from .models import Task_Request, Assign, Issuance

class RequestForm(forms.ModelForm):
    # Other fields from the Request model
    class Meta:
        model = Task_Request
        fields = ['request_number', 'request_type', 'device', 'device_serial']

class AssignForm(forms.ModelForm):

    device = forms.ChoiceField(choices=[('phones', 'Phones'), ('desktop', 'Desktop'), ('laptop', 'Laptop')], widget=forms.RadioSelect)

    class Meta:
        model = Assign
        fields = ['request_number', 'request_type', 'device', 'device_serial', 'comment', 'requester', 'Assigned', 'Technician']

class IssuanceForm(forms.ModelForm):

    class Meta:
        model = Issuance
        fields = [  'subject' , 
                  'comment', 'Issued',
                  'Approver', 'Technician'
                  ]

        labels = { 'subject' : 'Subject:' , 
                  'comment': 'Comments:', 'Issued': 'Issue To:',
                  'Approver' : 'Authorized By:', 'Technician': ' Technician:',
        }