# Generated by Django 4.2.4 on 2023-08-23 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0008_rename_desktop_sn_desktop_serial_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDesktop1',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Computer_Name', models.CharField(db_index=True, max_length=100)),
                ('Desktop_Make', models.CharField(max_length=100)),
                ('Serial_Number', models.CharField(db_index=True, max_length=100)),
                ('Processor', models.CharField(max_length=100)),
                ('Operating_System', models.CharField(choices=[('Win 10', 'Win 10'), ('Win 10 Pro', 'Win 10 Pro'), ('Win 8', 'Win 8'), ('Win 8.1', 'Win 8.1'), ('Win 8 Pro', 'Win 8 Pro'), ('Win 7', 'Win 7'), ('Win 7 Pro', 'Win 7 Pro')], max_length=10)),
                ('Office_Suite', models.CharField(max_length=10)),
                ('anti_virus', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
                ('Condition', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('Damaged', 'Damaged'), ('INACTIVE', 'INACTIVE')], max_length=100, null=True)),
                ('last_updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('assign', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dashboard.region')),
                ('station', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dashboard.station')),
            ],
            options={
                'verbose_name': 'historical desktop1',
                'verbose_name_plural': 'historical desktop1s',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Desktop1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Computer_Name', models.CharField(max_length=100, unique=True)),
                ('Desktop_Make', models.CharField(max_length=100)),
                ('Serial_Number', models.CharField(max_length=100, unique=True)),
                ('Processor', models.CharField(max_length=100)),
                ('Operating_System', models.CharField(choices=[('Win 10', 'Win 10'), ('Win 10 Pro', 'Win 10 Pro'), ('Win 8', 'Win 8'), ('Win 8.1', 'Win 8.1'), ('Win 8 Pro', 'Win 8 Pro'), ('Win 7', 'Win 7'), ('Win 7 Pro', 'Win 7 Pro')], max_length=10)),
                ('Office_Suite', models.CharField(max_length=10)),
                ('anti_virus', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
                ('Condition', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('Damaged', 'Damaged'), ('INACTIVE', 'INACTIVE')], max_length=100, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('assign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.region')),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.station')),
            ],
        ),
    ]
