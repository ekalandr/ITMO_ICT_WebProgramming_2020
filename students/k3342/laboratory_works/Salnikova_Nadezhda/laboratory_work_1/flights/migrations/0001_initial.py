# Generated by Django 3.0.4 on 2020-04-17 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Airport',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('ticket_type', models.CharField(choices=[('st', 'standard'), ('bu', 'business'), ('fi', 'first')], max_length=10)),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('bonus_card', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('dep_time', models.DateTimeField()),
                ('dep_terminal', models.IntegerField(blank=True)),
                ('arr_time', models.DateTimeField()),
                ('arr_terminal', models.IntegerField(blank=True)),
                ('flight_type', models.CharField(choices=[(('straight', 'straight'), ('charter', 'charter'), ('transfer', 'transfer'), ('stopover', 'stopover'))], max_length=10)),
                ('gate', models.CharField(max_length=5)),
                ('arr_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arr_airport', to='flights.Airport')),
                ('dep_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dep_airport', to='flights.Airport')),
                ('passengers', models.ManyToManyField(through='flights.Booking', to='flights.Client')),
            ],
            options={
                'db_table': 'Flight',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_type', models.CharField(blank=True, choices=[('Delay', 'Departure_delay'), ('Gate', 'Gate_changed'), ('Review', 'Review'), ('Other', 'Other')], max_length=30)),
                ('text', models.CharField(max_length=5000)),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Flight')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Client'),
        ),
        migrations.AddField(
            model_name='booking',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Flight'),
        ),
    ]