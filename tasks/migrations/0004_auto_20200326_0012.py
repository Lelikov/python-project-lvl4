# Generated by Django 3.0.4 on 2020-03-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200325_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='tasks.Tag'),
        ),
    ]
