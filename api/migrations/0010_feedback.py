# Generated by Django 4.0.2 on 2022-03-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_complaintremarks_complaint_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True, null=True)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('is_delete', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
