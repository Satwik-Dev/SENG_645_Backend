# Generated by Django 4.2.16 on 2024-11-10 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Type of inventory item (e.g., Food, Hygiene)', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('barcode', models.CharField(max_length=50, unique=True)),
                ('availability', models.CharField(choices=[('in-stock', 'In Stock'), ('out-of-stock', 'Out of Stock')], max_length=20)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.itemclassification')),
            ],
        ),
    ]
