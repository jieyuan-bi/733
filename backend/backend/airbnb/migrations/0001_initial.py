# Generated by Django 4.1.3 on 2022-12-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avg_Price_License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(max_length=100)),
                ('avg_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Corela_Rooms_Beds_Accommodates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.FloatField()),
                ('beds', models.FloatField()),
                ('accommodates', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Price_NumberOfBedRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms_nums', models.IntegerField()),
                ('min', models.FloatField()),
                ('q1', models.FloatField()),
                ('median', models.FloatField()),
                ('q3', models.FloatField()),
                ('max', models.FloatField()),
            ],
        ),
    ]