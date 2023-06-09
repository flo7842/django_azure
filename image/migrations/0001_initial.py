# Generated by Django 4.1.4 on 2023-04-28 10:24

from django.db import migrations, models
import image.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('base64', models.TextField(blank=True, null=True, validators=[image.models.validate_unique_textfield])),
            ],
        ),
    ]
