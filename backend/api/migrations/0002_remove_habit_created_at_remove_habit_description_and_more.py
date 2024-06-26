# Generated by Django 5.0.6 on 2024-06-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='description',
        ),
        migrations.AddField(
            model_name='habit',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='monday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]
