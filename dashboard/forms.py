from django import forms
from .models import Phone, Laptop1, Desktop1, RAM, HDD, Monitor, Keyboard, Mouse, LT_HDD, LT_RAM

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['Device_number','man_no', 'Make', 'Model', 'Serial_Number', 'Phone_number','apk_version', 'android_version','region','department', 'zone', 'Condition','assign',]

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop1
        fields = ['Computer_Name', 'Make', 'Serial_Number', 'Processor', 'Operating_System','anti_virus', 'Office_Suite', 'Location','region','station', 'Condition', 'assign',]


class DesktopForm(forms.ModelForm):
    
    class Meta:
        model = Desktop1
        fields = ['Computer_Name', 'Desktop_Make', 'Serial_Number', 'Processor',  'Operating_System', 'Office_Suite','anti_virus','region', 'station', 'Location', 'Condition','assign',]

class HDDForm(forms.ModelForm):
    
    class Meta:
        model = HDD
        fields = ['HDD_model','HDD_SN', 'Hard_disk_type','Hard_disk_Size', 'wk']
        labels = {'HDD_model':'Hard drive Model', 'HDD_SN':'Serial No:', 'Hard_disk_type':'Disk Type', 'Hard_disk_Size':'Size (GB)', 'wk': 'PC Assigned:'}

class LTRAMForm(forms.ModelForm):
    
    class Meta:
        model = LT_RAM
        fields = ['LT_RAM_make','LT_RAM_SN', 'LT_RAM_Size', 'LT']
        labels = {'LT_RAM_make':'Drive Model', 'LT_RAM_SN':'Serial No:',  'LT_RAM_Size':'RAM Size', 'LT': 'PC Assigned:'}

class LTHDDForm(forms.ModelForm):
    
    class Meta:
        model = LT_HDD
        fields = ['LT_HDD_model','LT_HDD_SN', 'LT_Hard_disk_type','LT_Hard_disk_Size', 'LT']
        labels = {'LT_HDD_model':'Hard drive Model', 'LT_HDD_SN':'Serial No:', 'LT_Hard_disk_type':'Disk Type', 'LT_Hard_disk_Size':'Size (GB)', 'LT': 'PC Assigned:'}

class RAMForm(forms.ModelForm):
    
    class Meta:
        model = RAM
        fields = ['RAM_make','RAM_SN', 'RAM_Size', 'wk']
        labels = {'RAM_make':'Drive Model', 'RAM_SN':'Serial No:',  'RAM_Size':'RAM Size', 'wk': 'PC Assigned:'}



class MonitorForm(forms.ModelForm):
    
    class Meta:
        model = Monitor
        fields = ['monitor_SN', 'monitor_make', 'wk']
        labels = {'monitor_make':'Monitor Make:', 'monitor_SN':'Serial No:', 'wk': 'PC Assigned:'}


class KeyboardForm(forms.ModelForm):
    
    class Meta:
        model = Keyboard
        fields = ['keyboard_SN', 'Keyboard_make', 'wk']
        labels = {'Keyboard_make':'keyboard Make:', 'keyboard_SN':'Serial No:', 'wk': 'PC Assigned:'}
        
class mouseForm(forms.ModelForm):
    
    class Meta:
        model = Mouse
        fields = ['mouse_SN', 'Mouse_make', 'wk']
        labels = {'Mouse_make':'Mouse Make:', 'mouse_SN':'Serial No:', 'wk': 'PC Assigned:'}