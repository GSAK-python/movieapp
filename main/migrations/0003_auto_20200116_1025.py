# Generated by Django 3.0.2 on 2020-01-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200116_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(0, 'Nieznany'), (4, 'Drama'), (2, 'Komedia'), (1, 'Horror'), (3, 'Sci-Fi')], default=0),
        ),
    ]
