# Generated by Django 4.0.4 on 2022-05-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0005_remove_quote_pdf_file_quote_school_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='pdf_file',
            field=models.FileField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]
