# Generated by Django 3.0.2 on 2020-01-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200121_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(1, 'Horror'), (4, 'Drama'), (3, 'Sci-Fi'), (2, 'Komedia'), (0, 'Nieznany')], default=0),
        ),
    ]