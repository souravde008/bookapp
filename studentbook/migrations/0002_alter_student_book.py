# Generated by Django 5.1.4 on 2024-12-12 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_book', to='studentbook.book'),
        ),
    ]
