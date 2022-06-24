# Generated by Django 3.2.5 on 2021-09-13 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_alter_student_marks_marks_alloted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='Roll_Number_Attendance',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AlterField(
            model_name='student_marks',
            name='Roll_Number_Marks',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]