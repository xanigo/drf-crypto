# Generated by Django 4.1 on 2022-08-15 16:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drf_shop', '0001_initial'),
        ('drf_crypto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='block_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='transactions', to='drf_shop.currency'),
            preserve_default=False,
        ),
    ]
