from django.db import models
from datetime import datetime, date
# Create your models here.

class Talabalar(models.Model):
    hemis_id = models.IntegerField(verbose_name="Hemis Id", help_text="Bu yerga faqat raqam yozish kerak !")
    fish = models.CharField(max_length=100, verbose_name="Bitiruvchi to'liq ismi", blank=False, null=False)
    jinsi = models.CharField(max_length=5, verbose_name="Bitiruvchi jinsi", blank=False, null=False)
    pasport_jshshr = models.IntegerField(verbose_name="Bitiruvchi pasport jshshr raqami", help_text="Bu yerga faqat raqam yozish kerak")
    pasport_seriya = models.CharField(max_length=9, verbose_name="Bitiruvchi pasport seriya belgilari", blank=False, null=False)
    tugilgan_sana = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Bitiruvchi tug'ilgan sanasi", help_text="shu tariqa yozing 2000-03-09", blank=True)
    yonalish_nomi = models.CharField(max_length=100, verbose_name="Bitiruvchi mutaxassisligi (yo'nalishi)", help_text="Iltimos to'liq nomini yozing", blank=False, null=False)
    grant_kontrakt = models.CharField(max_length=22, verbose_name="O'qish turi", help_text="Grand yoki Kontrakt", blank=False, null=False)
    viloyat = models.CharField(max_length=25, verbose_name="Bitiruvchi viloyati", blank=False, null=False)
    tuman = models.CharField(max_length=80, verbose_name="Bitiruvchi tumani", blank=False, null=False)
    mfy = models.CharField(max_length=80, verbose_name="Bitiruvchi MFY nomi", blank=False, null=False)
    umumiy_manzil = models.CharField(max_length=200, blank=False, verbose_name="Bitiruvchi to'liq manzili", help_text="viloyati tumani mahallasi kocha nomi", null=False)
    telefon1 = models.CharField(max_length=13, verbose_name="Bitiruvchi telefon raqami", help_text="1-telefon raqam", blank=False, null=False)
    telefon2 = models.CharField(max_length=14, verbose_name="Bitiruvchi telefon raqami", help_text="2-telefon raqam", blank=False, null=False)
    oila = models.CharField(max_length=18, verbose_name="Oilaviy holati", help_text="turmush qurgan yoki qurmagan", blank=True, null=True)
    farzand = models.CharField(max_length=12, verbose_name="Farzandingiz yoshi", help_text="nechi yosh atrofida", blank=True, null=True)
    farzand_yoshi = models.IntegerField(verbose_name="Farzandingiz yoshi", help_text="frazandingiz yo'q bo'lsa iltimos 0 raqamini kiriting ")
    ish_faoliyat = models.CharField(max_length=30, verbose_name="Ish faoliyatingiz", help_text="buyruq asosida, soatbay yoki ishsiz shulardan birini yozing", blank=True, null=True)
    xozirgi_ish = models.CharField(max_length=3, verbose_name="Xozirgi ishlaysizmi", help_text="ha yoki yoq", blank=True, null=True)
    ish_manzil = models.CharField(max_length=200, verbose_name="Ish joyingiz manzili", help_text="iltimos to'liq kiritng", blank=True, null=True)
    ish_masofa = models.CharField(max_length=20, verbose_name="Ish joyingizgacha masofa", help_text="uyingizdan ishingizgacha masofa", blank=True, null=True)
    lavozim = models.CharField(max_length=15, verbose_name="Ish joyingizdagi lavozimingiz", blank=True, null=True)
    qaysi_tizimda_ishlash = models.CharField(max_length=120, verbose_name="Qaysi tizimda ishlamoqchisiz", help_text="agar hozirda ishsiz bo'lsangiz kelajakda qaysi tizimda ishlamoqchisiz", blank=True, null=True)
    qoshimcha_izoh = models.TextField(verbose_name="Ishlash borasida izoxingiz", help_text="to'liqroq va aniqroq", blank=True, null=True)
    oilaviy_biznes = models.CharField(max_length=3, verbose_name="Oilaviz biznesga imkoniyatingiz bormi", help_text="ha yoki yo'q", blank=True, null=True)
    oilaviy_biznes2 = models.CharField(max_length=22, verbose_name="Qaysi biznes bilan shug'ullanmoqchisiz", help_text="dehqonchilik chorvachilik, ...", blank=True, null=True)
    kredit_olish = models.CharField(max_length=3, verbose_name="Kredit olishga ehtiyojingiz bormi", blank=True, help_text="ha yoki yo'q", null=True)
    kredit_summa = models.FloatField(verbose_name="Kredit miqdorini kiritng", help_text="agra kredit olmoqchi bo'lmasangiz iltimos 0 sonini kiritng")
    kredit_maqsad = models.CharField(max_length=150, verbose_name="Kredit olishdan maqsadingiz", help_text="maqsadingiz haqida qisqacha", blank=True, null=True)
    biznes_izox = models.TextField(verbose_name="Biznes qilish borasida izoxlaringiz", help_text="to'liqroq va aniqroq", blank=True, null=True)

    def __str__(self):
        return self.fish

    objects = models.Manager()
    
