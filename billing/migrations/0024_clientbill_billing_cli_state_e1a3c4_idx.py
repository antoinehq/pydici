# Generated by Django 3.2.18 on 2023-03-03 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0023_clientbill_allow_duplicate_expense'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='clientbill',
            index=models.Index(fields=['state', 'due_date'], name='billing_cli_state_e1a3c4_idx'),
        ),
    ]
