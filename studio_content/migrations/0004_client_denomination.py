# Generated by Django 3.2.23 on 2025-07-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_content', '0003_auto_20250717_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='denomination',
            field=models.CharField(blank=True, help_text='Denomination of the client (optional).', max_length=100, null=True),
        ),
    ]
