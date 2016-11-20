from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.models import *

#Normal Sites
def home(request):
    assert isinstance(request, HttpRequest)
    #user = User.objects.create_user('admin', None, 'rws_pw123')
    #user.save()
    return render(
        request,
        'app/index.html'
    )

def atelier(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/atelier.html',
        {
            'title':'atelier'
        }
    )

def galerie(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/galerie.html',
        {
            'title':'galerie 16.1'
        }
    )

def vita(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vita.html',
        {
            'title':'vita'
        }
    )

def kontakt(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/kontakt.html',
        {
            'title':'kontakt'
        }
    )

def anfahrt(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/anfahrt.html',
        {
            'title':'anfahrt'
        }
    )

def bilder(request):
    assert isinstance(request, HttpRequest)
    bilder = R_Bild.objects.all()
    return render(
        request,
        'app/bilder.html',
        {
            'title':'bilder',
            'db': bilder[::-1]
        }
    )

def buecher(request):
    assert isinstance(request, HttpRequest)
    buecher = R_Buch.objects.all()
    return render(
        request,
        'app/buecher.html',
        {
            'title':'buecher',
            'db':buecher[::-1]
        }
    )

def objekte(request):
    assert isinstance(request, HttpRequest)
    bilder = R_Objekt.objects.all()
    return render(
        request,
        'app/objekte.html',
        {
            'title':'objekte',
            'db': bilder[::-1]
        }
    )

def projekte(request):
    assert isinstance(request, HttpRequest)
    projekte = R_Projekt.objects.all()
    return render(
        request,
        'app/projekte.html',
        {
            'title':'projekte',
            'db':projekte[::-1]
        }
    )

def projektview(request):
    assert isinstance(request, HttpRequest)
    p_id = request.GET.get('p', '')
    dedicated_project = R_Projekt.objects.get(pk=p_id)
    bilder = R_Projektbild.objects.filter(projekt_f_id=p_id)
    return render(
        request,
        'app/_projekt.html',
        {
            'title':dedicated_project.name,
            'db':bilder[::-1],
            'p':dedicated_project
        }
    )

####################################################################################################
#Authentication/Login
def auth(request):
    assert isinstance(request, HttpRequest)
    username_p = request.POST.get('username', '')
    password_p = request.POST.get('password', '')
    
    user = authenticate(username=username_p, password=password_p)

    if user is not None:          
        login(request, user)
        return HttpResponseRedirect('/admin/admin_bilder')
    else:
        return HttpResponseRedirect('/login')


####################################################################################################
#Admin Pages
def admin_bilder(request):
    assert isinstance(request, HttpRequest)
    bilder = R_Bild.objects.all()
    if request.user.is_authenticated:
        return render(
            request,
            'app/admin/admin_bilder.html',
            { 'db':bilder[::-1] }
        )    
    else:
        return HttpResponseRedirect('/login')

def admin_buecher(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        buecher = R_Buch.objects.all()
        return render(
            request,
            'app/admin/admin_buecher.html',
            { 'db':buecher[::-1] }
        )    
    else:
        return HttpResponseRedirect('/login')

def admin_objekte(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        bilder = R_Objekt.objects.all()
        return render(
            request,
            'app/admin/admin_objekte.html',
            { 'db':bilder[::-1] }
        )    
    else:
        return HttpResponseRedirect('/login')

def admin_projekte(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        projekte = R_Projekt.objects.all()
        return render(
            request,
            'app/admin/admin_projekte.html',
            { 'db':projekte[::-1] }
        )    
    else:
        return HttpResponseRedirect('/login')

def admin_projektbilder(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        projektbilder = R_Projektbild.objects.filter(projekt_f_id=request.GET.get('p', ''))   
        dedicated_project = R_Projekt.objects.get(pk=request.GET.get('p', ''))     
        return render(
            request,
            'app/admin/admin_projektbilder.html',
            { 'db':projektbilder[::-1], 'p':dedicated_project}
        )    
    else:
        return HttpResponseRedirect('/login')

####################################################################################################
### Actions BILDER
def new_r_bild(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        img_p = request.POST.get('img', '')
        caption_p = request.POST.get('caption', '')
        date_p = request.POST.get('date', '')

        n = R_Bild(
            img = img_p,
            caption = caption_p,
            date = date_p
        )
        n.save()  
        return HttpResponseRedirect('/admin/admin_bilder')

    else: return HttpResponseRedirect('/login')

def r_bilder_save(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        new_caption = request.POST.get('caption_edit', '')
        s = R_Bild.objects.get(pk=request.POST.get('bild_id', ''))
        s.caption = new_caption
        s.save()
        return HttpResponseRedirect('/admin/admin_bilder')
    else: return HttpResponseRedirect('/login')

def r_bilder_delete(request):
    assert isinstance(request, HttpRequest)   
    if request.user.is_authenticated: 
        s = R_Bild.objects.get(pk=request.POST.get('bild_id', ''))
        s.delete()
        return HttpResponseRedirect('/admin/admin_bilder')
    else: return HttpResponseRedirect('/login')

### Actions BÜCHER
def new_r_buch(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        title_p = request.POST.get('title', '')
        src_p = request.POST.get('src', '')
        img_p = request.POST.get('img', '')

        n = R_Buch(
            title = title_p,
            src = src_p,
            img = img_p
        )
        n.save()  
        return HttpResponseRedirect('/admin/admin_buecher')

    else: return HttpResponseRedirect('/login')

def r_buecher_save(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        new_title = request.POST.get('title_edit', '')
        s = R_Buch.objects.get(pk=request.POST.get('buch_id', ''))
        s.title = new_title
        s.save()
        return HttpResponseRedirect('/admin/admin_buecher')
    else: return HttpResponseRedirect('/login')

def r_buecher_delete(request):
    assert isinstance(request, HttpRequest)   
    if request.user.is_authenticated: 
        s = R_Buch.objects.get(pk=request.POST.get('buch_id', ''))
        s.delete()
        return HttpResponseRedirect('/admin/admin_buecher')
    else: return HttpResponseRedirect('/login')
    
 ### Actions Objekte
def new_r_objekt(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        img_p = request.POST.get('img', '')
        caption_p = request.POST.get('caption', '')
        date_p = request.POST.get('date', '')

        n = R_Objekt(
            img = img_p,
            caption = caption_p,
            date = date_p
        )
        n.save()  
        return HttpResponseRedirect('/admin/admin_objekte')

    else: return HttpResponseRedirect('/login')

def r_objekte_save(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        new_caption = request.POST.get('caption_edit', '')
        s = R_Objekt.objects.get(pk=request.POST.get('bild_id', ''))
        s.caption = new_caption
        s.save()
        return HttpResponseRedirect('/admin/admin_objekte')
    else: return HttpResponseRedirect('/login')

def r_objekte_delete(request):
    assert isinstance(request, HttpRequest)   
    if request.user.is_authenticated: 
        s = R_Objekt.objects.get(pk=request.POST.get('bild_id', ''))
        s.delete()
        return HttpResponseRedirect('/admin/admin_objekte')
    else: return HttpResponseRedirect('/login')

 ### Actions Projekte
def new_r_projekt(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        img_p = request.POST.get('img', '')
        name_p = request.POST.get('name', '')

        n = R_Projekt(
            img = img_p,
            name = name_p
        )
        n.save()  
        return HttpResponseRedirect('/admin/admin_projekte')

    else: return HttpResponseRedirect('/login')

def r_projekte_save(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        new_name = request.POST.get('name_edit', '')
        s = R_Projekt.objects.get(pk=request.POST.get('projekt_id', ''))
        s.name = new_name
        s.save()
        return HttpResponseRedirect('/admin/admin_projekte')
    else: return HttpResponseRedirect('/login')

def r_projekte_delete(request):
    assert isinstance(request, HttpRequest)   
    if request.user.is_authenticated: 
        s = R_Projekt.objects.get(pk=request.POST.get('projekt_id', ''))
        s.delete()
        return HttpResponseRedirect('/admin/admin_projekte')
    else: return HttpResponseRedirect('/login')

#Actions Projektbilder
def new_r_projektbild(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        img_p = request.POST.get('img', '')
        caption_p = request.POST.get('caption', '')
        date_p = request.POST.get('date', '')
        projekt_f_p = request.POST.get('projekt_f', '')
        p = R_Projekt.objects.get(pk = projekt_f_p)
        
        n = R_Projektbild(
            img = img_p,
            caption = caption_p,
            date = date_p,
            projekt_f = p
        )
        n.save()  
        return HttpResponseRedirect('/admin/admin_projektbilder/?p='+projekt_f_p)
    else: return HttpResponseRedirect('/login')

def r_projektbilder_save(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        new_caption = request.POST.get('caption_edit', '')
        projekt_f_p = request.POST.get('projekt_f', '')
        s = R_Projektbild.objects.get(pk=request.POST.get('bild_id', ''))
        s.caption = new_caption
        s.save()
        return HttpResponseRedirect('/admin/admin_projektbilder/?p='+projekt_f_p)
    else: return HttpResponseRedirect('/login')

def r_projektbilder_delete(request):
    assert isinstance(request, HttpRequest)   
    if request.user.is_authenticated: 
        projekt_f_p = request.POST.get('projekt_f', '')
        s = R_Projektbild.objects.get(pk=request.POST.get('bild_id', ''))
        s.delete()
        return HttpResponseRedirect('/admin/admin_projektbilder/?p='+projekt_f_p)
    else: return HttpResponseRedirect('/login')