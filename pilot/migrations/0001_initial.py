# Generated by Django 2.1.2 on 2018-11-01 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('altitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shipping_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_ordered', models.DateTimeField()),
                ('time_dispatched', models.DateTimeField()),
                ('time_delivered', models.DateTimeField()),
                ('priority', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('items', models.ManyToManyField(to='pilot.Item')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_clinic_manager', models.BooleanField(default=False)),
                ('is_dispatcher', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClinicManager',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pilot.UserProfile')),
            ],
            bases=('pilot.userprofile',),
        ),
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pilot.UserProfile')),
            ],
            bases=('pilot.userprofile',),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='clinic_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pilot.ClinicManager'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='clinic_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pilot.ClinicManager'),
        ),
    ]
