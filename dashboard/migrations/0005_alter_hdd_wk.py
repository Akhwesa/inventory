# Generated by Django 4.1.5 on 2023-04-19 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_hdd_wk_alter_keyboard_wk_alter_mouse_wk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdd',
            name='wk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hard_disks', to='dashboard.desktop'),
        ),
    ]