# Generated by Django 4.0.4 on 2022-07-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='id',
        ),
        migrations.AddField(
            model_name='lecturer',
            name='lec_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False, unique=True),
        ),
    ]
