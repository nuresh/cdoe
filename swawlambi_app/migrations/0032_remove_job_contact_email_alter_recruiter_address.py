# Generated by Django 5.1.4 on 2025-03-31 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swawlambi_app', '0031_alter_student_branch_name_alter_student_course_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='contact_email',
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
