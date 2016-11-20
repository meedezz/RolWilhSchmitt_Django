from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

urlpatterns = [
    # Normal Sites
    url(r'^$', app.views.home, name='home'),
    url(r'^atelier', app.views.atelier, name='atelier'),
    url(r'^galerie', app.views.galerie, name='galerie'),
    url(r'^vita', app.views.vita, name='vita'),
    url(r'^kontakt', app.views.kontakt, name='kontakt'),
    url(r'^anfahrt', app.views.anfahrt, name='anfahrt'),
    url(r'^bilder', app.views.bilder, name='bilder'),
    url(r'^buecher', app.views.buecher, name='buecher'),
    url(r'^objekte', app.views.objekte, name='objekte'),
    url(r'^projekte', app.views.projekte, name='projekte'),

    url(r'^projekt/$', app.views.projektview, name='projektview'),
    
    #Admin Pages
    url(r'^admin/admin_bilder', app.views.admin_bilder, name='admin_bilder'),
    url(r'^admin/admin_buecher', app.views.admin_buecher, name='admin_buecher'),
    url(r'^admin/admin_objekte', app.views.admin_objekte, name='admin_objekte'),
    url(r'^admin/admin_projekte', app.views.admin_projekte, name='admin_projekte'),
    url(r'^admin/admin_projektbilder/$', app.views.admin_projektbilder, name='admin_projektbilder'),
    
    #Bilder verwalten
    url(r'^admin/new_r_bild/$', app.views.new_r_bild, name='new_r_bild'), 
    url(r'^admin/r_bilder_save$', app.views.r_bilder_save, name='r_bilder_save'),
    url(r'^admin/r_bilder_delete$', app.views.r_bilder_delete, name='r_bilder_delete'),

    #Bücher verwalten
    url(r'^admin/new_r_buch/$', app.views.new_r_buch, name='new_r_buch'), 
    url(r'^admin/r_buecher_save$', app.views.r_buecher_save, name='r_buecher_save'),
    url(r'^admin/r_buecher_delete$', app.views.r_buecher_delete, name='r_buecher_delete'),
    
    #Objekte verwalten
    url(r'^admin/new_r_objekt/$', app.views.new_r_objekt, name='new_r_objekt'), 
    url(r'^admin/r_objekte_save$', app.views.r_objekte_save, name='r_objekte_save'),
    url(r'^admin/r_objekte_delete$', app.views.r_objekte_delete, name='r_objekte_delete'),

    #Projekte verwalten
    url(r'^admin/new_r_projekt/$', app.views.new_r_projekt, name='new_r_projekt'), 
    url(r'^admin/r_projekte_save$', app.views.r_projekte_save, name='r_projekte_save'),
    url(r'^admin/r_projekte_delete$', app.views.r_projekte_delete, name='r_projekte_delete'),

    #Projektbilder verwalten
    url(r'^admin/new_r_projektbild/$', app.views.new_r_projektbild, name='new_r_projektbild'), 
    url(r'^admin/r_projektbilder_save$', app.views.r_projektbilder_save, name='r_projektbilder_save'),
    url(r'^admin/r_projektbilder_delete$', app.views.r_projektbilder_delete, name='r_projektbilder_delete'),

    ######################################
    #Login/Authentication
    url(r'^admin/auth/$', app.views.auth, name='auth'), 
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
                
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
]
