# Generated by Django 4.1.2 on 2022-11-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='aciklama',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
