# Generated by Django 4.1.3 on 2024-06-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GREEN_OASIS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250, verbose_name='title')),
                ('title_de', models.CharField(max_length=250, verbose_name='title')),
                ('title_pl', models.CharField(max_length=250, verbose_name='title')),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
