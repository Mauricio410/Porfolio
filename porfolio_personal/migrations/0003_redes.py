# Generated by Django 5.0.3 on 2024-03-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio_personal', '0002_alter_proyectos_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='redes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]