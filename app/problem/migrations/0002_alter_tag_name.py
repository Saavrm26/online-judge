# Generated by Django 4.1.10 on 2023-07-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='general', max_length=30, primary_key=True, serialize=False),
        ),
    ]