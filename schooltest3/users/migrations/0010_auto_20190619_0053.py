# Generated by Django 2.2.2 on 2019-06-18 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190615_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='department_name',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Department'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Usersdb'),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Usersdb'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='course_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Courses'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='teacher_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
    ]