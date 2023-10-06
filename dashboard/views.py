from django.shortcuts import render, redirect
from django.db.models import Sum, Value
from .models import Phone, Desktop1, Laptop1, Monitor, Mouse,Keyboard, HDD, RAM, LT_HDD, LT_RAM, Printer, catrilage, Networking
from django.contrib.auth.decorators import login_required
from .forms import PhoneForm, LaptopForm, DesktopForm, HDDForm, RAMForm, MonitorForm, KeyboardForm, mouseForm, LTRAMForm, LTHDDForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='user-login')
def index(request):  
    return render(request,'dashboard/index.html')

@login_required(login_url='user-login')
def devices(request):  
    wks = Desktop1.objects.all()
    lt = Laptop1.objects.all()
    mp = Phone.objects.all()
    pt = Printer.objects.all()
    nw = Networking.objects.all()

    wks_count = wks.count()
    lt_count = lt.count()
    mp_count = mp.count()
    pt_count = pt.count()
    nw_count = nw.count()

    context = {
        'wks_count' : wks_count,
        'lt_count' : lt_count,
        'mp_count' : mp_count,
        'pt_count' : pt_count,
        'nw_count' : nw_count,

    }
    return render(request,'dashboard/devices.html', context)

@login_required(login_url='user-login')
def phone(request):
    items = Phone.objects.all()


    context = {
        'items' : items,
        
    }
    return render(request, 'dashboard/phone.html', context)

@login_required(login_url='user-login')
def add_phone(request):
    items = Phone.objects.all()
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard-phone')
    else:
        form = PhoneForm()
    context = {
        'items': items,
        'form' : form,
    }
    return render(request, 'dashboard/add_phone.html', context) 

@login_required(login_url='user-login')
def desktop(request):
    items = Desktop1.objects.all()
    
    workstation = []
    for item in items:
        wk_name =  item.Computer_Name
        wk_make = item.Desktop_Make
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
            'monitor_sn': monitor_sn,
            'keyboard_sn': keyboard_sn, 
            'mouse_sn': mouse_sn,  
            'pk':item.pk      
            
        })

    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        filtered_items = [item for item in workstation if search_query.lower() in item['name'].lower()]
        return render(request, 'dashboard/desktop.html', {'query':search_query, 'workstation':filtered_items})

    context = {
       
        'workstation': workstation,
    }
    return render(request, 'dashboard/desktop.html', context)

@login_required(login_url='user-login')
def add_desktop(request):
    items = Desktop1.objects.all()
    if request.method == 'POST':
        dp_form = DesktopForm(request.POST)
        if dp_form.is_valid:
            dp_form.save()
            return redirect('dashboard-desktop')
    else:
        dp_form = DesktopForm()
       
    context = {
        'dp_form' : dp_form,
        'items' : items,
    }
    return render(request, 'dashboard/add_desktop.html', context)

@login_required(login_url='user-login')
def laptop(request):
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
            'time':time,  
            'pk': item.pk  
            
        })

        if request.method == 'POST':
            # Retrieve the search query entered by the user
            search_query = request.POST['search_query']
            # Filter your model by the search query
            filtered_items = [item for item in lappy if search_query.lower() in item['name'].lower()]
            return render(request, 'dashboard/laptop.html', {'query':search_query, 'lappy':filtered_items})

    context = {
        'items' : items,
        'lappy': lappy,
    }
    return render(request, 'dashboard/laptop.html', context)

@login_required(login_url='user-login')
def add_laptop(request):
    items = Laptop1.objects.all()
    if request.method == 'POST':
        lp_form = LaptopForm(request.POST)
        if lp_form.is_valid:
            lp_form.save()
            return redirect('dashboard-laptop')
    else:
        lp_form = LaptopForm()
    context = {
        'lp_form' : lp_form,
        'items' : items,
    }
    return render(request, 'dashboard/add_laptop.html', context)

@login_required(login_url='user-login')
def hdd(request):
    disks = HDD.objects.all()
    wks = Desktop1.objects.all()

    items=[]
    for i in disks:
        sn = i.HDD_SN
        mk = i.HDD_model
        size = i.Hard_disk_Size
        type = i.Hard_disk_type
        try:
            pc = i.wk
            pc_pk = pc.pk
            pc1 = wks.get(pk = pc_pk)
            pc_name = pc1.Computer_Name
        except:
             pc_name = None

        items.append({
            'HDD_model':mk,
            'HDD_SN':sn,
            'size':size,
            'type':type,
            'mouse_pc':pc_name,
        })

    
    if request.method == 'POST':
            add_hdd_form = HDDForm(request.POST)
            if add_hdd_form.is_valid():
                add_hdd_form.save()
                return redirect('dashboard-hdd')
    else:
            add_hdd_form = HDDForm()

    context = {
        'items' : items,
        'add_hdd_form':add_hdd_form,
    }
    return render(request, 'dashboard/hdd.html', context)

@login_required(login_url='user-login')
def ram(request):
    rm = RAM.objects.all()
    wks = Desktop1.objects.all()

    items=[]
    for i in rm:
        sn = i.RAM_SN
        mk = i.RAM_make
        size = i.RAM_Size
        try:
            pc = i.wk
            pc_pk = pc.pk
            pc1 = wks.get(pk = pc_pk)
            pc_name = pc1.Computer_Name
        except:
             pc_name = None

        items.append({
            'RAM_model':mk,
            'RAM_SN':sn,
            'size':size,
            'ram_pc':pc_name,
        })

    
    if request.method == 'POST':
            add_ram_form = RAMForm(request.POST)
            if add_ram_form.is_valid():
                add_ram_form.save()
                return redirect('dashboard-ram')
    else:
            add_ram_form = RAMForm()

    context = {
        'items' : items,
        'add_ram_form':add_ram_form,
    }
    return render(request, 'dashboard/ram.html', context)

@login_required(login_url='user-login')
def LThdd(request):
    disks = LT_HDD.objects.all()
    wks = Laptop1.objects.all()

    items=[]
    for i in disks:
        sn = i.LT_HDD_SN
        mk = i.LT_HDD_model
        size = i.LT_Hard_disk_Size
        type = i.LT_Hard_disk_type
        try:
            pc = i.LT
            pc_pk = pc.pk
            pc1 = wks.get(pk = pc_pk)
            pc_name = pc1.Computer_Name
        except:
             pc_name = None

        items.append({
            'LT_HDD_model':mk,
            'LT_HDD_SN':sn,
            'size':size,
            'type':type,
            'HDD_pc':pc_name,
        })
   
    if request.method == 'POST':
            add_hdd_form = LTHDDForm(request.POST)
            if add_hdd_form.is_valid():
                add_hdd_form.save()
                return redirect('dashboard-lthdd')
    else:
            add_hdd_form = LTHDDForm()

    context = {
        'items' : items,
        'add_hdd_form':add_hdd_form,
    }
    return render(request, 'dashboard/lthdd.html', context)

@login_required(login_url='user-login')
def LTram(request):
    rm = LT_RAM.objects.all()
    wks = Laptop1.objects.all()

    items=[]
    for i in rm:
        sn = i.LT_RAM_SN
        mk = i.LT_RAM_make
        size = i.LT_RAM_Size
        try:
            pc = i.LT
            pc_pk = pc.pk
            pc1 = wks.get(pk = pc_pk)
            pc_name = pc1.Computer_Name
        except:
             pc_name = None

        items.append({
            'LT_RAM_model':mk,
            'LT_RAM_SN':sn,
            'size':size,
            'ram_pc':pc_name,
        })

    
    if request.method == 'POST':
            add_ram_form = LTRAMForm(request.POST)
            if add_ram_form.is_valid():
                add_ram_form.save()
                return redirect('dashboard-ltram')
    else:
            add_ram_form = LTRAMForm()

    context = {
        'items' : items,
        'add_ram_form':add_ram_form,
    }
    return render(request, 'dashboard/ltram.html', context)

@login_required(login_url='user-login')
def desktop_details(request, pk):
    item = Desktop1.objects.get(pk=pk)
    drive = HDD.objects.filter(wk = item)
    rm = RAM.objects.filter(wk = item)

    try:
        mt = Monitor.objects.get(wk=item) 
    except ObjectDoesNotExist:
        # Handle the case when there is no associated monitor
        mt = None
    
    try:
        ky = Keyboard.objects.get(wk=item) 
    except ObjectDoesNotExist:
        # Handle the case when there is no associated monitor
        ky = None
    
    try:
        ms = Mouse.objects.get(wk=item) 
    except ObjectDoesNotExist:
        # Handle the case when there is no associated monitor
        ms = None
    

    rm_count = rm.count()
    dr_count = drive.count()

    context = {
            'item' : item,
            'mt': mt,
            'ky': ky,
            'ms' : ms,
            'drive': drive,
            'dr_count': dr_count,
            'rm' : rm,
            'rm_count':rm_count,
        }

    return render (request, 'dashboard/desktop_detail.html', context)

@login_required(login_url='user-login')
def desktop_history(request, pk):
     
     des = Desktop1.objects.get(pk = pk)
     his = des.history.all()

     
     context = {
          'his':his,
          'des': des,
     }
     return render (request, 'dashboard/desktop_history.html', context)

@login_required(login_url='user-login')
def disconnect_desktop_monitor(request, pk , pk1):
     
     mt = Monitor.objects.get(pk = pk1)
     dsk = Desktop1.objects.get(pk = pk)

     if request.method=='POST':
          mt.wk = None    
          mt.save()      
          return redirect('dashboard-desktop-detail', pk=dsk.pk)
     context = {
          'mt': mt,
          'dsk': dsk,
     }

     return render (request, 'dashboard/disconnect_desktop_monitor.html', context)

@login_required(login_url='user-login')
def connect_desktop_monitor (request, pk):
     dsk = Desktop1.objects.get(pk = pk)
     not_connected_mt = Monitor.objects.filter(wk=None)

     context = {
          'not_connected_mt':not_connected_mt,
          'dsk':dsk,
     }

     return render(request, 'dashboard/connect_desktop_monitor.html', context)

@login_required(login_url='user-login')
def save_connect_monitor(request, pk, pk1):
     mt = Monitor.objects.get(pk=pk1)
     dsk1 = Desktop1.objects.get(pk=pk)
     mt.wk = dsk1
     mt.save()
     return redirect('dashboard-desktop-detail', pk=dsk1.pk)

@login_required(login_url='user-login')
def disconnect_desktop_hdd(request, pk , pk1):
     
     mt = HDD.objects.get(pk = pk1)
     dsk = Desktop1.objects.get(pk = pk)

     if request.method=='POST':
          mt.wk = None    
          mt.save()      
          return redirect('dashboard-desktop-detail', pk=dsk.pk)
     context = {
          'mt': mt,
          'dsk': dsk,
     }

     return render (request, 'dashboard/disconnect_desktop_hdd.html', context)

@login_required(login_url='user-login')
def connect_desktop_hdd (request, pk):
     dsk = Desktop1.objects.get(pk = pk)
     not_connected_mt = HDD.objects.filter(wk=None)

     context = {
          'not_connected_mt':not_connected_mt,
          'dsk':dsk,
     }

     return render(request, 'dashboard/connect_desktop_hdd.html', context)

@login_required(login_url='user-login')
def save_connect_hdd(request, pk, pk1):
     mt = HDD.objects.get(pk=pk1)
     dsk1 = Desktop1.objects.get(pk=pk)
     mt.wk = dsk1
     mt.save()
     return redirect('dashboard-desktop-detail', pk=dsk1.pk)

@login_required(login_url='user-login')
def disconnect_desktop_ram(request, pk , pk1):
     
     mt = RAM.objects.get(pk = pk1)
     dsk = Desktop1.objects.get(pk = pk)

     if request.method=='POST':
          mt.wk = None    
          mt.save()      
          return redirect('dashboard-desktop-detail', pk=dsk.pk)
     context = {
          'mt': mt,
          'dsk': dsk,
     }

     return render (request, 'dashboard/disconnect_desktop_ram.html', context)

@login_required(login_url='user-login')
def connect_desktop_ram(request, pk):
     dsk = Desktop1.objects.get(pk = pk)
     not_connected_mt = RAM.objects.filter(wk=None)

     context = {
          'not_connected_mt':not_connected_mt,
          'dsk':dsk,
     }

     return render(request, 'dashboard/connect_desktop_ram.html', context)

@login_required(login_url='user-login')
def save_connect_ram(request, pk, pk1):
     mt = RAM.objects.get(pk=pk1)
     dsk1 = Desktop1.objects.get(pk=pk)
     mt.wk = dsk1
     mt.save()
     return redirect('dashboard-desktop-detail', pk=dsk1.pk)

@login_required(login_url='user-login')
def disconnect_desktop_keyboard(request, pk , pk1):
     
     mt = Keyboard.objects.get(pk = pk1)
     dsk = Desktop1.objects.get(pk = pk)

     if request.method=='POST':
          mt.wk = None    
          mt.save()      
          return redirect('dashboard-desktop-detail', pk=dsk.pk)
     context = {
          'mt': mt,
          'dsk': dsk,
     }

     return render (request, 'dashboard/disconnect_desktop_keyboard.html', context)

@login_required(login_url='user-login')
def connect_desktop_keyboard(request, pk):
     dsk = Desktop1.objects.get(pk = pk)
     not_connected_mt = Keyboard.objects.filter(wk=None)

     context = {
          'not_connected_mt':not_connected_mt,
          'dsk':dsk,
     }

     return render(request, 'dashboard/connect_desktop_keyboard.html', context)

@login_required(login_url='user-login')
def save_connect_keyboard(request, pk, pk1):
     mt = Keyboard.objects.get(pk=pk1)
     dsk1 = Desktop1.objects.get(pk=pk)
     mt.wk = dsk1
     mt.save()
     return redirect('dashboard-desktop-detail', pk=dsk1.pk)

@login_required(login_url='user-login')
def disconnect_desktop_mouse(request, pk , pk1):
     
     mt = Mouse.objects.get(pk = pk1)
     dsk = Desktop1.objects.get(pk = pk)

     if request.method=='POST':
          mt.wk = None    
          mt.save()      
          return redirect('dashboard-desktop-detail', pk=dsk.pk)
     context = {
          'mt': mt,
          'dsk': dsk,
     }

     return render (request, 'dashboard/disconnect_desktop_mouse.html', context)

@login_required(login_url='user-login')
def connect_desktop_mouse(request, pk):
     dsk = Desktop1.objects.get(pk = pk)
     not_connected_mt = Mouse.objects.filter(wk=None)

     context = {
          'not_connected_mt':not_connected_mt,
          'dsk':dsk,
     }

     return render(request, 'dashboard/connect_desktop_mouse.html', context)

@login_required(login_url='user-login')
def save_connect_mouse(request, pk, pk1):
     mt = Mouse.objects.get(pk=pk1)
     dsk1 = Desktop1.objects.get(pk=pk)
     mt.wk = dsk1
     mt.save()
     return redirect('dashboard-desktop-detail', pk=dsk1.pk)

@login_required(login_url='user-login')
def laptop_details(request, pk):
    item = Laptop1.objects.get(pk=pk)
    drive = LT_HDD.objects.filter(LT = item)
    rm = LT_RAM.objects.filter(LT = item)

    rm_count = rm.count()
    dr_count = drive.count()

    context = {
            'item' : item,
            'drive': drive,
            'dr_count': dr_count,
            'rm' : rm,
            'rm_count':rm_count,
        }

    return render (request, 'dashboard/laptop_detail.html', context)

@login_required(login_url='user-login')
def disconnect_laptop_lthdd(request, pk , pk1):
     
     mt = LT_HDD.objects.get(pk = pk1)
     dsk = Laptop1.objects.get(pk = pk)

     if request.method=='POST':
          mt.LT = None    
          mt.save()      
          return redirect('dashboard-laptop-detail', pk=dsk.pk)
     context = {
          'mt': mt,
          'dsk': dsk,
     }

     return render (request, 'dashboard/disconnect_laptop_lthdd.html', context)

@login_required(login_url='user-login')
def connect_laptop_lthdd (request, pk):
     dsk = Laptop1.objects.get(pk = pk)
     not_connected_mt = LT_HDD.objects.filter(LT=None)

     context = {
          'not_connected_mt':not_connected_mt,
          'dsk':dsk,
     }

     return render(request, 'dashboard/connect_laptop_lthdd.html', context)

@login_required(login_url='user-login')
def save_connect_lthdd(request, pk, pk1):
     mt = LT_HDD.objects.get(pk=pk1)
     dsk1 = Laptop1.objects.get(pk=pk)
     mt.LT = dsk1
     mt.save()
     return redirect('dashboard-laptop-detail', pk=dsk1.pk)

@login_required(login_url='user-login')
def disconnect_laptop_ltram(request, pk , pk1):
     
     mt = LT_RAM.objects.get(pk = pk1)
     dsk = Laptop1.objects.get(pk = pk)

     if request.method=='POST':
          mt.LT = None    
          mt.save()      
          return redirect('dashboard-laptop-detail', pk=dsk.pk)
     context = {
          'mt': mt,
          'dsk': dsk,
     }

     return render (request, 'dashboard/disconnect_laptop_ltram.html', context)

@login_required(login_url='user-login')
def connect_laptop_ltram(request, pk):
     dsk = Laptop1.objects.get(pk = pk)
     not_connected_mt = LT_RAM.objects.filter(LT=None)

     context = {
          'not_connected_mt':not_connected_mt,
          'dsk':dsk,
     }

     return render(request, 'dashboard/connect_laptop_ltram.html', context)

@login_required(login_url='user-login')
def save_connect_ltram(request, pk, pk1):
     mt = LT_RAM.objects.get(pk=pk1)
     dsk1 = Laptop1.objects.get(pk=pk)
     mt.LT = dsk1
     mt.save()
     return redirect('dashboard-laptop-detail', pk=dsk1.pk)

@login_required(login_url='user-login')
def laptop_history(request, pk):
     
     des = Laptop1.objects.get(pk = pk)
     his = des.history.all()

     
     context = {
          'his':his,
          'des': des,
     }
     return render (request, 'dashboard/laptop_history.html', context)


@login_required(login_url='user-login')
def printer (request):

    pt = Printer.objects.all()

    context = {
        'pt':pt
    }
    return render(request,'dashboard/printer.html', context)

@login_required(login_url='user-login')
def network(request):

    NW = Networking.objects.all()

    context = {
        'NW':NW
    }
    return render(request,'dashboard/network.html', context)

@login_required(login_url='user-login')
def accessory(request):

    NWk = Networking.objects.all()
    mt = Monitor.objects.all()
    ky = Keyboard.objects.all()
    ms = Mouse.objects.all()
    disk = HDD.objects.all()
    rm = RAM.objects.all()
    LT_disk = LT_HDD.objects.all()
    LT_rm = LT_RAM.objects.all()

    ky_count = ky.count()
    ms_count = ms.count()
    disk_count = disk.count()
    rm_count = rm.count()
    LT_disk_count = LT_disk.count()
    LT_rm_count = LT_rm.count()
    mt_count = mt.count()

    context = {
        'NWk':NWk,
        'mt_count':mt_count,
        'ky_count':ky_count,
        'ms_count':ms_count,
        'disk_count':disk_count,
        'rm_count':rm_count,
        'lt_disk_count':LT_disk_count,
        'lt_rm_count':LT_rm_count,
    }
    return render(request,'dashboard/accessory.html', context)

@login_required(login_url='user-login')
def monitor(request):

    mt = Monitor.objects.all()
    wks = Desktop1.objects.all()

    items=[]
    for i in mt:
        sn = i.monitor_SN
        mk = i.monitor_make
        try:
            pc = i.wk
            pc_pk = pc.pk
            pc1 = wks.get(pk = pc_pk)
            pc_name = pc1.Computer_Name
        except:
             pc_name = None

        items.append({
            'monitor_make':mk,
            'monitor_SN':sn,
            'monitor_pc':pc_name,
        })

    
    if request.method == 'POST':
            add_monitor_form = MonitorForm(request.POST)
            if add_monitor_form.is_valid():
                add_monitor_form.save()
                return redirect('dashboard-monitor')
    else:
            add_monitor_form = MonitorForm()

    

    context = {
        'items':items,
        'add_monitor_form': add_monitor_form,
    }
    return render (request, 'dashboard/monitor.html', context)

@login_required(login_url='user-login')
def keyboard(request):

    ky = Keyboard.objects.all()
    wks = Desktop1.objects.all()

    items=[]
    for i in ky:
        sn = i.keyboard_SN
        mk = i.Keyboard_make
        try:
            pc = i.wk
            pc_pk = pc.pk
            pc1 = wks.get(pk = pc_pk)
            pc_name = pc1.Computer_Name
        except:
             pc_name = None

        items.append({
            'keyboard_make':mk,
            'keyboard_SN':sn,
            'keyboard_pc':pc_name,
        })

    
    if request.method == 'POST':
            add_keyboard_form = KeyboardForm(request.POST)
            if add_keyboard_form.is_valid():
                add_keyboard_form.save()
                return redirect('dashboard-keyboard')
    else:
            add_keyboard_form = KeyboardForm()

    context = {
        'items':items,
        'add_keyboard_form': add_keyboard_form,
    }
    return render (request, 'dashboard/keyboard.html', context)

@login_required(login_url='user-login')
def mouse(request):

    ky = Mouse.objects.all()
    wks = Desktop1.objects.all()

    items=[]
    for i in ky:
        sn = i.mouse_SN
        mk = i.Mouse_make
        try:
            pc = i.wk
            pc_pk = pc.pk
            pc1 = wks.get(pk = pc_pk)
            pc_name = pc1.Computer_Name
        except:
             pc_name = None

        items.append({
            'Mouse_make':mk,
            'mouse_SN':sn,
            'mouse_pc':pc_name,
        })

    
    if request.method == 'POST':
            add_mouse_form = mouseForm(request.POST)
            if add_mouse_form.is_valid():
                add_mouse_form.save()
                return redirect('dashboard-mouse')
    else:
            add_mouse_form = mouseForm()

    context = {
        'items':items,
        'add_mouse_form': add_mouse_form,
    }
    return render (request, 'dashboard/mouse.html', context)