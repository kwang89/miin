# Generated by Django 3.1.3 on 2020-11-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone_num', models.CharField(max_length=13, unique=True)),
                ('user_name', models.CharField(max_length=128)),
                ('user_address', models.CharField(max_length=128, null=True)),
                ('user_password', models.CharField(max_length=256)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-update_date'],
            },
        ),
    ]
