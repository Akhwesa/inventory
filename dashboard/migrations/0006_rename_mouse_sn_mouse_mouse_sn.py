# Generated by Django 4.1.5 on 2023-06-05 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_hdd_wk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mouse',
            old_name='Mouse_SN',
            new_name='mouse_SN',
        ),
    ]
