from django.contrib import admin
from .models import Talabalar

# Register your models here.

@admin.register(Talabalar)
class TalabalarAdmin(admin.ModelAdmin):
    list_display = ['id', 'hemis_id', 'fish', 'jinsi', 'pasport_jshshr', 'pasport_seriya', 'tugilgan_sana', 'yonalish_nomi', 'grant_kontrakt', 'viloyat', 'tuman', 'mfy', 'umumiy_manzil', 'telefon1', 'telefon2', 'oila', 'farzand', 'farzand_yoshi', 'ish_faoliyat', 'xozirgi_ish', 'ish_manzil', 'ish_masofa', 'lavozim', 'qaysi_tizimda_ishlash', 'qoshimcha_izoh', 'oilaviy_biznes', 'oilaviy_biznes2', 'kredit_olish', 'kredit_summa', 'kredit_maqsad', 'biznes_izox']
    list_per_page = 10