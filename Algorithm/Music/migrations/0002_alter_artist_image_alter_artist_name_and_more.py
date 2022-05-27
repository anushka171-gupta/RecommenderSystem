# Generated by Django 4.0.4 on 2022-05-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='cover_art_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='popularity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='preview_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
