# Generated by Django 3.0.3 on 2021-05-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Short',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('shortcode', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='URL',
        ),
    ]
