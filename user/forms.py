from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re
from datetime import date

class UserForm(forms.Form):
    nama = forms.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9._-]+$',
                message="Nama hanya boleh diisi oleh huruf, angka, dan karakter (‘.’,’_’,’-’)."
            )
        ]
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput
    )
    tanggal_lahir = forms.DateField()
    nomor_hp = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=255)
    url_blog = forms.URLField(max_length=255)
    deskripsi_diri = forms.CharField(
        max_length=1000,
        min_length=5,
        widget=forms.Textarea
    )
    nomor_rekening = forms.CharField(max_length=10, min_length=8)
    kode_mata_uang = forms.CharField(max_length=3, min_length=3)

    def clean_password(self):
        password = self.cleaned_data['password']
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+{}|<>?]).{8,}$'
        if not re.match(pattern, password):
            raise ValidationError(
                "Password harus minimal 8 karakter dan mengandung huruf, angka, serta karakter spesial."
            )
        return password

    def clean_tanggal_lahir(self):
        tanggal_lahir = self.cleaned_data['tanggal_lahir']
        today = date.today()
        umur = today.year - tanggal_lahir.year
        if (today.month, today.day) < (tanggal_lahir.month, tanggal_lahir.day):
            umur -= 1

        if umur < 12:
            raise ValidationError("Usia pengguna minimal 12 tahun.")
        return tanggal_lahir

    def clean_nomor_hp(self):
        nomor_hp = self.cleaned_data['nomor_hp']
        nomor_hp_sanitized = re.sub(r'[^\d]', '', nomor_hp)
        if not (8 <= len(nomor_hp_sanitized) <= 15):
            raise ValidationError(
                "Nomor HP harus memiliki panjang 8-15 digit setelah menghilangkan karakter non-digit."
            )
        return nomor_hp_sanitized

    def clean_nomor_rekening(self):
        nomor_rekening = self.cleaned_data['nomor_rekening']
        if not re.match(r'^\d{8,10}$', nomor_rekening):
            raise ValidationError("Nomor rekening harus terdiri dari 8 hingga 10 digit angka.")
        return nomor_rekening

    def clean_kode_mata_uang(self):
        kode_mata_uang = self.cleaned_data['kode_mata_uang'].upper()
        if not re.match(r'^[A-Z]{3}$', kode_mata_uang):
            raise ValidationError("Kode mata uang harus terdiri dari 3 huruf.")
        return kode_mata_uang
