# Generated by Django 4.1.4 on 2023-01-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_submission_is_correct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submitted_answer',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
