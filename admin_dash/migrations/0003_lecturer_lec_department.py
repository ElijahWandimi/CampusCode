# Generated by Django 4.0.4 on 2022-07-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0002_remove_lecturer_id_lecturer_lec_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='lec_department',
            field=models.CharField(default='Computer Science', max_length=100),
        ),
    ]
