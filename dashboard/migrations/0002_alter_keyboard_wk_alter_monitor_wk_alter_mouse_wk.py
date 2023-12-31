# Generated by Django 4.1.5 on 2023-04-19 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyboard',
            name='wk',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='keyboards', to='dashboard.desktop'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='wk',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.desktop'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='wk',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mouses', to='dashboard.desktop'),
        ),
    ]
