# Generated by Django 2.2.14 on 2022-03-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
