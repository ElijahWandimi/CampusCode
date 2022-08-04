# Generated by Django 4.0.4 on 2022-07-21 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_dash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=32)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.student')),
                ('q_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dash.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_text', models.TextField(max_length=2000)),
                ('student_answer', models.TextField(max_length=2000)),
                ('q_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dash.question')),
            ],
        ),
    ]