# Generated by Django 4.2.4 on 2023-08-23 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_historicaldesktop1_desktop1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdd',
            name='wk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hard_disks', to='dashboard.desktop1'),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='wk',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.desktop1'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='wk',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.desktop1'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='wk',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.desktop1'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='wk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rams', to='dashboard.desktop1'),
        ),
    ]
