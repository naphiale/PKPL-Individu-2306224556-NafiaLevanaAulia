# Generated by Django 5.1.7 on 2025-03-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('tanggal_lahir', models.DateField()),
                ('nomor_hp', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('url_blog', models.URLField(max_length=255)),
                ('deskripsi_diri', models.TextField(max_length=1000)),
                ('nomor_rekening', models.CharField(max_length=10)),
                ('kode_mata_uang', models.CharField(max_length=3)),
            ],
        ),
    ]
