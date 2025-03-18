from django.db import models

# Create your models here.
class User(models.Model):
    nama = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    nomor_hp = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    url_blog = models.URLField(max_length=255)
    deskripsi_diri = models.TextField(max_length=1000)
    nomor_rekening = models.CharField(max_length=10)
    kode_mata_uang = models.CharField(max_length=3)

    def __str__(self):
        return self.nama