from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Talabalar
from .resources import StudentsRecurse

def index(request):  # sourcery skip: remove-unreachable-code
    if 'q' in request.GET:
        q = request.GET['q']
        data = Talabalar.objects.filter(fish__icontains=q)
    else:
        data = Talabalar.objects.all()
    print(data)
    context = {
        "data":data
    }
    return render(request, 'index.html', context)

def download(request):
    # dt = Talabalar.objects.all()
    student_resource = StudentsRecurse()
    data = student_resource.export()
    response = HttpResponse(data.csv, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="talabalar.csv"'
    return response

def insert(request):  # sourcery skip: extract-method, last-if-guard
    if request.method =="POST":
        hemis_id = request.POST.get('hemis_id')
        fish = request.POST.get('fish')
        jinsi = request.POST.get('jinsi')
        pasport_jshshr = request.POST.get('pasport_jshshr')
        pasport_seriya = request.POST.get('pasport_seriya')
        tugilgan_sana = request.POST.get('tugilgan_sana')
        yonalish_nomi = request.POST.get('yonalish_nomi')
        grant_kontrakt = request.POST.get('grant_kontrakt')
        viloyat = request.POST.get('viloyat')
        tuman = request.POST.get('tuman')
        mfy = request.POST.get('mfy')
        umumiy_manzil = request.POST.get('umumiy_manzil')
        telefon1 = request.POST.get('telefon1')
        telefon2 = request.POST.get('telefon2')
        oila = request.POST.get('oila')
        farzand = request.POST.get('farzand')
        farzand_yoshi = request.POST.get('farzand_yoshi')
        ish_faoliyat = request.POST.get('ish_faoliyat')
        xozirgi_ish = request.POST.get('xozirgi_ish')
        ish_manzil = request.POST.get('ish_manzil')
        ish_masofa = request.POST.get('ish_masofa')
        lavozim = request.POST.get('lavozim')
        qaysi_tizimda_ishlash = request.POST.get('qaysi_tizimda_ishlash')
        qoshimcha_izoh = request.POST.get('qoshimcha_izoh')
        oilaviy_biznes = request.POST.get('oilaviy_biznes')
        oilaviy_biznes2 = request.POST.get('oilaviy_biznes2')
        kredit_olish = request.POST.get('kredit_olish')
        kredit_summa = request.POST.get('kredit_summa')
        kredit_maqsad = request.POST.get('kredit_maqsad')
        biznes_izox = request.POST.get('biznes_izox')
        print(hemis_id,fish,jinsi,pasport_jshshr,pasport_seriya,tugilgan_sana,yonalish_nomi,grant_kontrakt,viloyat,tuman,mfy,umumiy_manzil,telefon1,telefon2,oila,farzand,farzand_yoshi,ish_faoliyat,xozirgi_ish,ish_manzil,ish_masofa,lavozim,qaysi_tizimda_ishlash,qoshimcha_izoh,oilaviy_biznes,oilaviy_biznes2,kredit_olish,kredit_summa,kredit_maqsad,biznes_izox)
        students=Talabalar(hemis_id=hemis_id,fish=fish,jinsi=jinsi,pasport_jshshr=pasport_jshshr,pasport_seriya=pasport_seriya,
        tugilgan_sana=tugilgan_sana,yonalish_nomi=yonalish_nomi,grant_kontrakt=grant_kontrakt,viloyat=viloyat,tuman=tuman,mfy=mfy,umumiy_manzil=umumiy_manzil,telefon1=telefon1,telefon2=telefon2,oila=oila,farzand=farzand,farzand_yoshi=farzand_yoshi,ish_faoliyat=ish_faoliyat,xozirgi_ish=xozirgi_ish,ish_manzil=ish_manzil,ish_masofa=ish_masofa,lavozim=lavozim,qaysi_tizimda_ishlash=qaysi_tizimda_ishlash,qoshimcha_izoh=qoshimcha_izoh,oilaviy_biznes=oilaviy_biznes,oilaviy_biznes2=oilaviy_biznes2,kredit_olish=kredit_olish,kredit_summa=kredit_summa,kredit_maqsad=kredit_maqsad,biznes_izox=biznes_izox)
        students.save()
        return redirect('/')
    return render(request, 'insert.html')

def update(request, id):  # sourcery skip: extract-method, remove-unreachable-code
    if request.method =="POST":
        oila = request.POST['oila']
        farzand = request.POST['farzand']
        farzand_yoshi = request.POST['farzand_yoshi']
        ish_faoliyat = request.POST['ish_faoliyat']
        xozirgi_ish = request.POST['xozirgi_ish']
        ish_manzil = request.POST['ish_manzil']
        ish_masofa = request.POST['ish_masofa']
        lavozim = request.POST['lavozim']
        qaysi_tizimda_ishlash = request.POST['qaysi_tizimda_ishlash']
        qoshimcha_izoh = request.POST['qoshimcha_izoh']
        oilaviy_biznes = request.POST['oilaviy_biznes']
        oilaviy_biznes2 = request.POST['oilaviy_biznes2']
        kredit_olish = request.POST['kredit_olish']
        kredit_summa = request.POST['kredit_summa']
        kredit_maqsad = request.POST['kredit_maqsad']
        biznes_izox = request.POST['biznes_izox']

        

        edit = Talabalar.objects.get(id=id)
        edit.oila = oila
        edit.farzand = farzand
        edit.farzand_yoshi = farzand_yoshi
        edit.ish_faoliyat = ish_faoliyat
        edit.xozirgi_ish = xozirgi_ish
        edit.ish_manzil = ish_manzil
        edit.ish_masofa = ish_masofa
        edit.lavozim = lavozim
        edit.qaysi_tizimda_ishlash = qaysi_tizimda_ishlash
        edit.qoshimcha_izoh = qoshimcha_izoh
        edit.oilaviy_biznes = oilaviy_biznes
        edit.oilaviy_biznes2 = oilaviy_biznes2
        edit.kredit_olish = kredit_olish
        edit.kredit_summa = kredit_summa
        edit.kredit_maqsad = kredit_maqsad
        edit.biznes_izox = biznes_izox
        edit.save()
        return redirect("/")
        
    d = Talabalar.objects.get(id=id)
    context = {
        "d":d
    }
    return render(request, 'edit.html', context)

def detail(request, pk ):
    std = Talabalar.objects.get(id=pk)
    context = {
        'std': std,
    }   
    return render(request, 'detail.html', context)

        
def delete(request, id):
    st = Talabalar.objects.get(id=id)
    st.delete()    
    return redirect("/")

def about(request):
    return render(request, "about.html")