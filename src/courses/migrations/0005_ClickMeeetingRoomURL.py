# Generated by Django 2.2.7 on 2019-11-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_ReceiptNames'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='clickmeeting_room_url',
            field=models.URLField(blank=True, help_text='If set, every user who purcashes this course gets invited', null=True, verbose_name='Clickmeeting room URL'),
        ),
    ]
