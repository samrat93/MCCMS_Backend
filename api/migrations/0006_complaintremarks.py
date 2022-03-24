# Generated by Django 4.0.2 on 2022-03-24 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_complain_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintRemarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_status', models.CharField(blank=True, choices=[('1', 'Pending'), ('2', 'Processing'), ('3', 'Closed')], max_length=10, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('remarks_date', models.DateTimeField()),
                ('complaint_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.complain')),
            ],
        ),
    ]
