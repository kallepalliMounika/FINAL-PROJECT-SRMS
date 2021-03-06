# Generated by Django 3.2.5 on 2021-07-30 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_rename_groups_groups_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester_Teacher', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=20)),
                ('Course_Code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.courses')),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.groups')),
                ('Teacher_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.teacher')),
            ],
        ),
    ]
