# Generated by Django 2.2.3 on 2020-09-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20200907_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='dissapeared_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
