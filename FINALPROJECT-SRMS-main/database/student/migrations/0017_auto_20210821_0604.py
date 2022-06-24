# Generated by Django 3.2.5 on 2021-08-21 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20210816_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='Date_Time_Original',
            field=models.DateTimeField(default=''),
        ),
        migrations.RemoveField(
            model_name='student_marks',
            name='Course_Code_Marks',
        ),
        migrations.AddField(
            model_name='student_marks',
            name='Course_Code_Marks',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='student.courses'),
        ),
        migrations.RemoveField(
            model_name='student_marks',
            name='Roll_Number_Marks',
        ),
        migrations.AddField(
            model_name='student_marks',
            name='Roll_Number_Marks',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='student.student'),
        ),
        migrations.AlterField(
            model_name='student_marks',
            name='Semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=20, null=True),
        ),
        migrations.RemoveField(
            model_name='student_marks',
            name='Teacher_Id_Marks',
        ),
        migrations.AddField(
            model_name='student_marks',
            name='Teacher_Id_Marks',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='student.teacher'),
        ),
    ]
