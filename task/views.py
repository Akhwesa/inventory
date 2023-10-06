from django.shortcuts import render, redirect ,get_object_or_404
from .forms import RequestForm, AssignForm, IssuanceForm
from .models import Task_Request, Issuance, Repair, Movement
from user.models import User
from django.contrib.auth.decorators import login_required
from dashboard.models import Phone, Desktop1, Laptop1

# Create your views here.

DeviceTypeMapping = {
    'phones': Phone,
    'desktop': Desktop1,
    'laptop': Laptop1,
}

@login_required(login_url='user-login')
def task(request):
     tr = Task_Request.objects.all()
     
     context = {
          'tr':tr
     }
     return render(request, 'dashboard/task.html', context )

def create_request(request):
    form = RequestForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Save the request with an "open" status
            instance = form.save(commit=False)
            instance.status = 'open'
            instance.save()
    context = {
        'form': form,

    }

    return render(request, 'request_form.html', context)

@login_required(login_url='user-login')
def assign(request):
    assigned = Issuance.objects.all()
    
    context = {
        'assigned':assigned
    }
    return render(request, 'task/assign.html', context)

@login_required(login_url='user-login')
def repair(request):
    form = RequestForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Save the request with an "open" status
            instance = form.save(commit=False)
            instance.status = 'open'
            instance.save()
    context = {
        'form': form,
    }

    return render(request, 'task/repair.html', context)

@login_required(login_url='user-login')
def movement(request):
    form = RequestForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Save the request with an "open" status
            instance = form.save(commit=False)
            instance.status = 'open'
            instance.save()
    context = {
        'form': form,
    }

    return render(request, 'task/movement.html', context)

@login_required(login_url='user-login')
def desktop_select_move(request):
    items = Desktop1.objects.all()
    
    workstation = []
    for item in items:
        wk_name =  item.Computer_Name
        wk_make = item.Desktop_Make
        wk_SN = item.Serial_Number
        Region = item.region
        cd = item.Condition
        assigned =  item.assign
        
        hard_disks = item.hard_disks.all()
        total_disk_size = sum([hard_disks.Hard_disk_Size for hard_disks in hard_disks])

        rams = item.rams.all()
        total_ram_size = sum([rams.RAM_Size for rams in rams])
        monitor_sn = None
        if hasattr(item, 'monitor'):  # Check if Monitor object exists
            monitor_sn = item.monitor.monitor_SN

        keyboard_sn = None
        if hasattr(item, 'keyboard'):  # Check if keyboard object exists
            keyboard_sn = item.keyboard.keyboard_SN

        mouse_sn = None
        if hasattr(item, 'mouse'):  # Check if mouse object exists
            mouse_sn = item.mouse.mouse_SN
        
        workstation.append({
            'hard_disk':total_disk_size,
            'ram': total_ram_size,
            'name': wk_name,
            'make': wk_make,
            'sn': wk_SN,
            'region':Region,
            'condition': cd,
            'user': assigned,
            'monitor_sn': monitor_sn,
            'keyboard_sn': keyboard_sn, 
            'mouse_sn': mouse_sn,    
            'pk':item.pk,
            
        })

    context = {
       
        'workstation': workstation,
    }
    return render(request, 'task/desktop_select_move.html', context)

def laptop_select_move(request):
    items = Laptop1.objects.all()
    lappy = []
    for item in items:
        wk_name =  item.Computer_Name
        wk_make = item.Make
        wk_SN = item.Serial_Number
        processor =  item.Processor
        os =  item.Operating_System
        office =  item.Office_Suite
        AV = item.anti_virus
        Region = item.region
        dpt = item.department
        st =  item.station
        location = item.Location
        cd = item.Condition
        assigned =  item.assign
        time =  item.last_updated
        
        lt_hdds = item.lt_hdds.all()
        total_disk_size = sum([lt_hdds.LT_Hard_disk_Size for lt_hdds in lt_hdds])

        lt_rams = item.lt_rams.all()
        total_ram_size = sum([lt_rams.LT_RAM_Size for lt_rams in lt_rams])
        
        lappy.append({
            'hard_disk':total_disk_size,
            'ram': total_ram_size,
            'name': wk_name,
            'make': wk_make,
            'sn': wk_SN,
            'processor':processor,
            'os':os,
            'office': office,
            'av': AV,
            'region':Region,
            'department':dpt,
            'station': st,
            'location':location,
            'condition': cd,
            'user': assigned,
            "time":time,    
            
        })

    context = {
        'lappy': lappy,
    }
    return render(request, 'task/laptop_select_move.html', context)

@login_required(login_url='user-login')
def maintenance(request):
    form = RequestForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Save the request with an "open" status
            instance = form.save(commit=False)
            instance.status = 'open'
            instance.save()
    context = {
        'form': form,
    }

    return render(request, 'task/maintenance.html', context)

@login_required(login_url='user-login')
def desktop_select(request):
    items = Desktop1.objects.all()
    
    workstation = []
    for item in items:
        wk_name =  item.Computer_Name
        wk_make = item.Desktop_Make
        wk_SN = item.Serial_Number
        Region = item.region
        cd = item.Condition
        assigned =  item.assign
        
        hard_disks = item.hard_disks.all()
        total_disk_size = sum([hard_disks.Hard_disk_Size for hard_disks in hard_disks])

        rams = item.rams.all()
        total_ram_size = sum([rams.RAM_Size for rams in rams])
        monitor_sn = None
        if hasattr(item, 'monitor'):  # Check if Monitor object exists
            monitor_sn = item.monitor.monitor_SN

        keyboard_sn = None
        if hasattr(item, 'keyboard'):  # Check if keyboard object exists
            keyboard_sn = item.keyboard.keyboard_SN

        mouse_sn = None
        if hasattr(item, 'mouse'):  # Check if mouse object exists
            mouse_sn = item.mouse.mouse_SN
        
        workstation.append({
            'hard_disk':total_disk_size,
            'ram': total_ram_size,
            'name': wk_name,
            'make': wk_make,
            'sn': wk_SN,
            'region':Region,
            'condition': cd,
            'user': assigned,
            'monitor_sn': monitor_sn,
            'keyboard_sn': keyboard_sn, 
            'mouse_sn': mouse_sn,    
            'pk':item.pk,
            
        })

    context = {
       
        'workstation': workstation,
    }
    return render(request, 'task/desktop_select.html', context)



@login_required(login_url='user-login')
def desktop_issuance(request, pk):

    requester = request.user
    item = Desktop1.objects.get(id=pk)
    sn = item.Serial_Number
    dv = 'desktop'
    
    if request.method == 'POST':
        issueform = IssuanceForm(request.POST)
        if issueform.is_valid():
            issue = issueform.save(commit=False)
            issue.device = dv
            issue.device_serial = sn
            issue.requester = requester
            issue.save()
 
            taskRequest = Task_Request.objects.create(
                request_number = issue.request_number,
                request_type = 'issuance',
                device = 'desktop',
                device_serial = issue.device_serial,
                assigned = issue.Approver,
                subject = issue.subject,                
            )
            taskRequest.save()
            return redirect('task-assign')
        
    else:
        issueform = IssuanceForm()
    
    context = {
        'issueform': issueform,
        'item': item,
    }

    return render(request, 'task/issuance.html', context )

def laptop_select_issue(request):
    items = Laptop1.objects.all()
    lappy = []
    for item in items:
        wk_name =  item.Computer_Name
        wk_make = item.Make
        wk_SN = item.Serial_Number
        processor =  item.Processor
        os =  item.Operating_System
        office =  item.Office_Suite
        AV = item.anti_virus
        Region = item.region
        dpt = item.department
        st =  item.station
        location = item.Location
        cd = item.Condition
        assigned =  item.assign
        time =  item.last_updated
        
        lt_hdds = item.lt_hdds.all()
        total_disk_size = sum([lt_hdds.LT_Hard_disk_Size for lt_hdds in lt_hdds])

        lt_rams = item.lt_rams.all()
        total_ram_size = sum([lt_rams.LT_RAM_Size for lt_rams in lt_rams])
        
        lappy.append({
            'hard_disk':total_disk_size,
            'ram': total_ram_size,
            'name': wk_name,
            'make': wk_make,
            'sn': wk_SN,
            'processor':processor,
            'os':os,
            'office': office,
            'av': AV,
            'region':Region,
            'department':dpt,
            'station': st,
            'location':location,
            'condition': cd,
            'user': assigned,
            "time":time,    
            
        })

    context = {
        'lappy': lappy,
    }
    return render(request, 'task/laptop_select_issue.html', context)

