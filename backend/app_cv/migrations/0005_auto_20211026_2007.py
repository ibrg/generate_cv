# Generated by Django 3.2.8 on 2021-10-26 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_cv', '0004_auto_20211026_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='cv',
        ),
        migrations.AddField(
            model_name='cv',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edu', to='app_cv.education'),
        ),
        migrations.AddField(
            model_name='cv',
            name='work_experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='work', to='app_cv.workexperience'),
        ),
    ]