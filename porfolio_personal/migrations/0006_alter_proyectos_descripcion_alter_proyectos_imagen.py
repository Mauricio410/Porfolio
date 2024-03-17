# Generated by Django 5.0.3 on 2024-03-17 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio_personal', '0005_proyectos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='porfolio/images/'),
        ),
    ]