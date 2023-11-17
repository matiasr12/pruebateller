"""Proyectos_notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from postres import views

urlpatterns = [
 path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    
    # principal de usuarios
    path('apoderados/',views.apoderados,name='apoderados'),
    path('profesores/',views.profesor, name='profesor'),
    path('alumno/',views.alumno,name='alumno'),
    # registro de usuarios
    path('registrarapo/',views.register_profesor, name='registrarapo'),
    path('registroprofesor/',views.register_profesor2, name='registroprofesor'),
    path('registroalumno/',views.register_student, name='registroalumno'),
    # login de usuarios
    path('loginalumno/',views.logina,name="loginalu"),
    path('loginprofesor/',views.loginp,name='loginprofesor'),
    path('loginapoderado/',views.loginap,name='loginapoderado'),
    path('login/', views.login, name='login'),
    
    # guardar y recuperar notas
    path('notas/', views.guardar_nota,  name='guardar_nota'),
    path('notasapo/',views.notasap, name='notasapo'),
    path('notasal/',views.obtener_notas,name='notasal'),
    path('notasapode/',views.obtener_notas2,name='notasprofe'),
    path('notasedit/', views.notasedit, name='notasedit'),
    
    # guardar y recuperar anotaciones
    path('anotaciones/', views.anotaciones_form1, name='guardar_anotacion'),
    path('anotacionesapo/',views.anotaciones_form, name='anotacionesapode'),
    
    # gestion  de archivos
    path('actividadesp/',views.subir_archivo,name='subir_archivo'),
    path('actividadesalumno/',views.gestionar_archivos, name='actividades'),
    path('actividadapoderado/',views.gestionar_archivos2, name='actividades1'),
    path('subir-archivo/', views.upload_file, name='upload_file'),

    path('cargar_asignaturas/', views.listar_materias, name='cargar_asignaturas'),

    path('gestionar_notas/', views.gestionar_notas, name='gestionar_notas'),


]
   
 
