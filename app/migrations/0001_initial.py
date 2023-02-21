# Generated by Django 4.1.7 on 2023-02-21 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talabalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hemis_id', models.IntegerField(help_text='Bu yerga faqat raqam yozish kerak !', verbose_name='Hemis Id')),
                ('fish', models.CharField(max_length=100, verbose_name="Bitiruvchi to'liq ismi")),
                ('jinsi', models.CharField(max_length=5, verbose_name='Bitiruvchi jinsi')),
                ('pasport_jshshr', models.IntegerField(help_text='Bu yerga faqat raqam yozish kerak', verbose_name='Bitiruvchi pasport jshshr raqami')),
                ('pasport_seriya', models.CharField(max_length=9, verbose_name='Bitiruvchi pasport seriya belgilari')),
                ('tugilgan_sana', models.DateField(blank=True, help_text='shu tariqa yozing 2000-03-09', verbose_name="Bitiruvchi tug'ilgan sanasi")),
                ('yonalish_nomi', models.CharField(help_text="Iltimos to'liq nomini yozing", max_length=100, verbose_name="Bitiruvchi mutaxassisligi (yo'nalishi)")),
                ('grant_kontrakt', models.CharField(help_text='Grand yoki Kontrakt', max_length=22, verbose_name="O'qish turi")),
                ('viloyat', models.CharField(max_length=25, verbose_name='Bitiruvchi viloyati')),
                ('tuman', models.CharField(max_length=80, verbose_name='Bitiruvchi tumani')),
                ('mfy', models.CharField(max_length=80, verbose_name='Bitiruvchi MFY nomi')),
                ('umumiy_manzil', models.CharField(help_text='viloyati tumani mahallasi kocha nomi', max_length=200, verbose_name="Bitiruvchi to'liq manzili")),
                ('telefon1', models.CharField(help_text='1-telefon raqam', max_length=13, verbose_name='Bitiruvchi telefon raqami')),
                ('telefon2', models.CharField(help_text='2-telefon raqam', max_length=14, verbose_name='Bitiruvchi telefon raqami')),
                ('oila', models.CharField(blank=True, help_text='turmush qurgan yoki qurmagan', max_length=18, null=True, verbose_name='Oilaviy holati')),
                ('farzand', models.CharField(blank=True, help_text='nechi yosh atrofida', max_length=12, null=True, verbose_name='Farzandingiz yoshi')),
                ('farzand_yoshi', models.IntegerField(help_text="frazandingiz yo'q bo'lsa iltimos 0 raqamini kiriting ", verbose_name='Farzandingiz yoshi')),
                ('ish_faoliyat', models.CharField(blank=True, help_text='buyruq asosida, soatbay yoki ishsiz shulardan birini yozing', max_length=30, null=True, verbose_name='Ish faoliyatingiz')),
                ('xozirgi_ish', models.CharField(blank=True, help_text='ha yoki yoq', max_length=3, null=True, verbose_name='Xozirgi ishlaysizmi')),
                ('ish_manzil', models.CharField(blank=True, help_text="iltimos to'liq kiritng", max_length=200, null=True, verbose_name='Ish joyingiz manzili')),
                ('ish_masofa', models.CharField(blank=True, help_text='uyingizdan ishingizgacha masofa', max_length=20, null=True, verbose_name='Ish joyingizgacha masofa')),
                ('lavozim', models.CharField(blank=True, max_length=15, null=True, verbose_name='Ish joyingizdagi lavozimingiz')),
                ('qaysi_tizimda_ishlash', models.CharField(blank=True, help_text="agar hozirda ishsiz bo'lsangiz kelajakda qaysi tizimda ishlamoqchisiz", max_length=120, null=True, verbose_name='Qaysi tizimda ishlamoqchisiz')),
                ('qoshimcha_izoh', models.TextField(blank=True, help_text="to'liqroq va aniqroq", null=True, verbose_name='Ishlash borasida izoxingiz')),
                ('oilaviy_biznes', models.CharField(blank=True, help_text="ha yoki yo'q", max_length=3, null=True, verbose_name='Oilaviz biznesga imkoniyatingiz bormi')),
                ('oilaviy_biznes2', models.CharField(blank=True, help_text='dehqonchilik chorvachilik, ...', max_length=22, null=True, verbose_name="Qaysi biznes bilan shug'ullanmoqchisiz")),
                ('kredit_olish', models.CharField(blank=True, help_text="ha yoki yo'q", max_length=3, null=True, verbose_name='Kredit olishga ehtiyojingiz bormi')),
                ('kredit_summa', models.FloatField(help_text="agra kredit olmoqchi bo'lmasangiz iltimos 0 sonini kiritng", verbose_name='Kredit miqdorini kiritng')),
                ('kredit_maqsad', models.CharField(blank=True, help_text='maqsadingiz haqida qisqacha', max_length=150, null=True, verbose_name='Kredit olishdan maqsadingiz')),
                ('biznes_izox', models.TextField(blank=True, help_text="to'liqroq va aniqroq", null=True, verbose_name='Biznes qilish borasida izoxlaringiz')),
            ],
        ),
    ]
