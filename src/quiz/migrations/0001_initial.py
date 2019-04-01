# Generated by Django 2.1.7 on 2019-04-01 05:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('type', models.CharField(choices=[('s', 'Subjective Question'), ('m', 'Multiple Choice Single-Correct'), ('o', 'Multiple Choice Multi-Correct')], default='s', max_length=1)),
                ('marks', models.IntegerField(default=4)),
                ('time_limit', models.IntegerField(default=3600)),
                ('level', models.CharField(choices=[('e', 'Easy'), ('m', 'Medium'), ('h', 'Hard'), ('d', 'Difficult')], default='m', max_length=1)),
                ('max_words', models.IntegerField(default=1000)),
                ('subjective_answer', models.TextField(max_length=models.IntegerField(default=1000))),
                ('option_A', models.TextField(default='', max_length=300)),
                ('option_B', models.TextField(default='', max_length=300)),
                ('option_C', models.TextField(default='', max_length=300)),
                ('option_D', models.TextField(default='', max_length=300)),
                ('correct', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name': 'Questions',
                'verbose_name_plural': 'Questions',
                'db_table': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('quiz_name', models.CharField(max_length=100)),
                ('quiz_password', models.CharField(max_length=50)),
                ('quiz_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.IntegerField(default=120)),
                ('description', models.TextField(max_length=400)),
                ('instructions', models.TextField(max_length=400)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
                'db_table': 'Quiz',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
        ),
    ]
