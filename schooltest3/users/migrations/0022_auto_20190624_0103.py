# Generated by Django 2.2.2 on 2019-06-23 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20190624_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
    ]