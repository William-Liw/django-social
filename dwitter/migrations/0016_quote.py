# Generated by Django 4.0.4 on 2022-05-26 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dwitter', '0015_quote_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(default='', max_length=16)),
                ('school_name', models.CharField(max_length=256)),
                ('to_name', models.CharField(max_length=256)),
                ('school_address', models.CharField(max_length=2048)),
                ('school_country', models.CharField(max_length=256)),
                ('to_email', models.EmailField(max_length=254)),
                ('school_size', models.IntegerField()),
                ('price_per_student', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateField()),
                ('currency', models.CharField(max_length=3)),
                ('bank_detail', models.CharField(blank=True, max_length=2048)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='')),
                ('special_comments', models.CharField(blank=True, max_length=2048, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]