# Generated by Django 4.2 on 2023-04-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('working', models.BooleanField(default=True)),
            ],
        ),
    ]
