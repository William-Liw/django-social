# Generated by Django 4.0.4 on 2022-05-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0018_alter_quote_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
