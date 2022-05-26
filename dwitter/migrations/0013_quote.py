# Generated by Django 4.0.4 on 2022-05-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0012_alter_quote_pdf_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.IntegerField()),
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
            ],
        ),
    ]
