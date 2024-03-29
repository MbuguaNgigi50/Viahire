 # Generated by Django 2.2.6 on 2019-10-30 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_Name', models.CharField(max_length=100)),
                ('Job_Description', models.TextField()),
                ('Job_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Job_Requirements', models.TextField()),
                ('Job_Qualifications', models.TextField()),
                ('Employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
