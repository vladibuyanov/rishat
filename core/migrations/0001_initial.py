# Generated by Django 4.1.1 on 2022-09-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Модель Item',
                'verbose_name_plural': 'Модель Items',
            },
        ),
    ]