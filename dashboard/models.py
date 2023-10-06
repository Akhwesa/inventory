from django.db import models
from user.models import User, Profile
from simple_history.models import HistoricalRecords

# Create your models here.
make = (
    ('Huaweii', 'Huaweii'),
    ('Samsung', 'Samsung'),
    ('Tecno', 'Tecno'),
)
region = (
    ('NE', 'NE'),
    ('HQ', 'HQ'),
    ('ER', 'ER'),
    ('SR','SR'),
    ('WR','WR'),
    ('CR','CR'),
)

model = (
    ('Samsung', 'A13'),
    ('Tecno', 'P3'),
    ('Huaweii', 'GR3 2017'),
)

st = (
    ('Working', 'Working'),
    ('Damaged', 'Damaged'),
    ('Repairs', 'Repairs'),
    ('Inactive', 'Inactive'),
    ('Obsolete', 'Obsolete'),
)

C_status = (
    ('Full', 'Full'),
    ('used', 'used'),
    ('Empty', 'Empty'),
    ('Ingenuine', 'Ingenuine'),
    ('Obsolete', 'Obsolete'),
)

condition =(
    ('ACTIVE', 'ACTIVE'), 
    ('Damaged', 'Damaged'),
    ('INACTIVE', 'INACTIVE'),
)

Hdd_type = (
    ('SSD', 'SSD'),
    ('HDD', 'HDD'),
)

OS = (
    ('Win 10', 'Win 10'),
    ('Win 10 Pro', 'Win 10 Pro'),
    ('Win 8', 'Win 8'),
    ('Win 8.1', 'Win 8.1'),
    ('Win 8 Pro', 'Win 8 Pro'),
    ('Win 7', 'Win 7'),
    ('Win 7 Pro', 'Win 7 Pro'),
)

class Region(models.Model):
    region_name = models.CharField(max_length=100,choices=region, unique=True)

    def __str__(self):
        return f'{self.region_name}'
    
class station(models.Model):
    station_name = models.CharField(max_length=100, unique=True)
    region1 = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.station_name}'
    
class zones(models.Model):
    zone_name = models.CharField(max_length=100, unique=True)
    region1 = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.zone_name}'

class Desktop(models.Model):
    Computer_Name = models.CharField(max_length=100, unique=True)
    Desktop_Make = models.CharField(max_length=100)
    Serial_Number = models.CharField(primary_key=True, max_length=100,unique=True)
    Processor = models.CharField(max_length=100)
    Operating_System = models.CharField(max_length=10, choices=OS)
    Office_Suite = models.CharField(max_length=10)
    anti_virus = models.CharField(max_length=50)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=50)
    station = models.ForeignKey(station, on_delete=models.SET_NULL, null=True, blank=True)
    Location = models.CharField(max_length=50)
    Condition = models.CharField(max_length=100, choices=condition, null=True)
    assign = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.Computer_Name} - {self.Desktop_Make} - {self.assign} - {self.last_updated}'

class Desktop1(models.Model):
    Computer_Name = models.CharField(max_length=100, unique=True)
    Desktop_Make = models.CharField(max_length=100)
    Serial_Number = models.CharField( max_length=100,unique=True)
    Processor = models.CharField(max_length=100)
    Operating_System = models.CharField(max_length=10, choices=OS)
    Office_Suite = models.CharField(max_length=10)
    anti_virus = models.CharField(max_length=50)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=50)
    station = models.ForeignKey(station, on_delete=models.SET_NULL, null=True, blank=True)
    Location = models.CharField(max_length=50)
    Condition = models.CharField(max_length=100, choices=condition, null=True)
    assign = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.Computer_Name}'


class Laptop(models.Model):
    Computer_Name = models.CharField(max_length=100, unique=True, )
    Make = models.CharField(max_length=100)
    Serial_Number = models.CharField(primary_key=True, max_length=100, unique=True)
    Processor = models.CharField(max_length=100)
    Operating_System = models.CharField(max_length=10, choices=OS)
    Office_Suite = models.CharField(max_length=10)
    Location = models.CharField(max_length=50, null=True)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=50)
    station = models.ForeignKey(station, on_delete=models.SET_NULL, null=True, blank=True)
    anti_virus = models.CharField(max_length=50)
    Condition = models.CharField(max_length=100, choices=condition, null=True)
    assign = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.Computer_Name} - {self.Serial_Number}'
    

class Laptop1(models.Model):
    Computer_Name = models.CharField(max_length=100, unique=True, )
    Make = models.CharField(max_length=100)
    Serial_Number = models.CharField(max_length=100, unique=True)
    Processor = models.CharField(max_length=100)
    Operating_System = models.CharField(max_length=10, choices=OS)
    Office_Suite = models.CharField(max_length=10)
    Location = models.CharField(max_length=50, null=True)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=50)
    station = models.ForeignKey(station, on_delete=models.SET_NULL, null=True, blank=True)
    anti_virus = models.CharField(max_length=50)
    Condition = models.CharField(max_length=100, choices=condition, null=True)
    assign = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.Computer_Name} - {self.Serial_Number}'
    
class Phone(models.Model):
    Device_number = models.IntegerField(  unique=True)
    man_no = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='man_number')
    Make = models.CharField(max_length=100, choices=make)
    Model = models.CharField(max_length=100)
    Serial_Number = models.CharField(primary_key=True, max_length=100, unique=True)
    Phone_number = models.CharField(max_length=10, unique=True, null=True)
    apk_version = models.CharField(max_length=100, null=True)
    android_version = models.CharField(max_length=100)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=50)
    zone = models.ForeignKey(zones, on_delete=models.SET_NULL, null=True, blank=True)
    Condition = models.CharField(max_length=100, choices=condition, null=True)
    assign = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.Device_number} - {self.man_no} - {self.Make} - {self.Model} - {self.Serial_Number} - {self.Phone_number} - {self.Condition} - {self.last_updated}'

class Monitor(models.Model):
    monitor_SN = models.CharField(max_length=100, unique=True)
    monitor_make = models.CharField(max_length=50, null=True)
    wk = models.OneToOneField(Desktop1, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.monitor_make} - {self.monitor_SN} - {self.wk}'
    
class Keyboard(models.Model):
    keyboard_SN = models.CharField(max_length=100, unique=True)
    Keyboard_make = models.CharField(max_length=50, null=True)
    wk = models.OneToOneField(Desktop1, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.Keyboard_make} - {self.keyboard_SN} - {self.wk}'

class Mouse(models.Model):
    mouse_SN = models.CharField(max_length=100, unique=True)
    Mouse_make = models.CharField(max_length=50, null=True)
    wk = models.OneToOneField(Desktop1, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.Mouse_make} - {self.mouse_SN} - {self.wk}'

class  HDD(models.Model):
    HDD_SN = models.CharField(max_length=100, unique=True)
    HDD_model = models.CharField(max_length=50)
    Hard_disk_Size = models.IntegerField()
    Hard_disk_type = models.CharField(max_length=10, choices=Hdd_type)
    wk = models.ForeignKey(Desktop1, on_delete=models.SET_NULL, null=True, blank=True, related_name='hard_disks')

    def __str__(self):
        return f'{self.HDD_SN} - {self.HDD_model} - {self.wk}'
    
class  RAM(models.Model):
    RAM_SN = models.CharField(max_length=100, unique=True)
    RAM_Size = models.IntegerField( null=True)
    RAM_make = models.CharField(max_length=50, null=True)
    wk = models.ForeignKey(Desktop1, on_delete=models.SET_NULL, null=True, blank=True, related_name='rams')
    def __str__(self):
        return f'{self.RAM_Size} - {self.RAM_SN}-{self.wk}'

class  LT_RAM(models.Model):
    LT_RAM_SN = models.CharField(max_length=100, unique=True)
    LT_RAM_Size = models.IntegerField( null=True)
    LT_RAM_make = models.CharField(max_length=50, null=True)
    LT = models.ForeignKey(Laptop1, on_delete=models.SET_NULL, null=True, blank=True, related_name='lt_rams')
    def __str__(self):
        return f'{self.LT_RAM_Size} - {self.LT_RAM_SN} - {self.LT}'

class  LT_HDD(models.Model):
    LT_HDD_SN = models.CharField(max_length=100, unique=True)
    LT_HDD_model = models.CharField(max_length=50)
    LT_Hard_disk_Size = models.IntegerField()
    LT_Hard_disk_type = models.CharField(max_length=10, choices=Hdd_type)
    LT = models.ForeignKey(Laptop1, on_delete=models.SET_NULL, null=True, blank=True, related_name='lt_hdds')

    def __str__(self):
        return f'{self.LT_HDD_SN} - {self.LT_HDD_model} - {self.LT}'
    

class Printer(models.Model):
    P_SN =models.CharField(max_length=150, unique=True)
    p_make = models.CharField(max_length=100)
    p_model = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    No_Toner = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='printerRegion')
    status = models.CharField(max_length=50, choices=st)
    assign = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

class Networking(models.Model):
    N_type = models.CharField(max_length=50)
    N_SN =models.CharField(max_length=150, unique=True)
    N_make = models.CharField(max_length=100)
    N_model = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='NetworkRegion')
    status = models.CharField(max_length=50, choices=st)
    assign = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

class catrilage(models.Model):
    C_SN = models.CharField(max_length=100, unique=True)
    C_model = models.CharField(max_length=50)
    C_make = models.CharField(max_length=50)
    C_color = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='TonerRegion')
    status = models.CharField(max_length=50, choices=C_status)
    assign = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

