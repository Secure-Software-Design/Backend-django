# Generated by Django 3.2.5 on 2022-12-13 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_student_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='codice_fiscal',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='country',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='region_of_birth',
        ),
    ]
