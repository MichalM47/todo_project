# Generated by Django 4.2.6 on 2023-10-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_status_remove_task_status_alter_todolists_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pictures'),
        ),
    ]
