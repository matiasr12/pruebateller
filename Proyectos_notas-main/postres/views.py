from django.shortcuts import render,redirect
import firebase_admin
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.db import transaction




import firebase_admin
from firebase_admin import credentials, storage
from firebase_admin import db , auth
from firebase_admin import storage
from .models import Profesor

# Create your views here.
def index(request):
    return render(request, 'index.html')


def profesor(request):
    return render(request,'profesor.html')



def anotaciones (request):
    return render(request,'anotaciones.html')

def actividadesp(request):
    return render(request,'actividadesp.html')


def alumno(request):
    return render(request,'alumno.html')


def notasal(request):
    return render(request,'notasal.html')

def actividadesal(request):
    return render(request,'actividadesal.html')

def logina(request):
    return render(request,'loginalumno.html')

def loginp(request):
    return render(request,'login_profesor.html')

def loginap(request):
    return render(request,"loginapoderado.html")

def apoderados(request):
    return render(request,"apoderados.html")

def registrarapo(request):
    return render(request,"registrarapo.html")


def registroalumno(request):
    return render(request,"registroalumn.html")

def notasap(request):
    return render(request,"notasapode.html")



def anotacionesapo(request):
    return render(request,"anotacionesapo.html")

def index2(request):
    return render(request,"idenx1.html.html")





cred = credentials.Certificate('./proyectonotas-41662-firebase-adminsdk-496e1-1732814dcb.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyectonotas-41662-default-rtdb.firebaseio.com',
    'storageBucket': 'proyectonotas-41662.appspot.com'
    
})



def mostrar_datos(request):
    # Accede a la referencia de la base de datos Firebase
    ref = db.reference('/Data')  # Ajusta la referencia según tu estructura de datos


    # Recupera los datos de Firebase
    data = ref.get()

    # Pasa los datos a tu plantilla HTML
    return render(request, 'idenx1.html', {'data': data})


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auth.create_user(email=email, password=password)
            # Usuario creado exitosamente en Firebase Authentication

            # Ahora, guardamos los datos del usuario en la base de datos en tiempo real
            user_data = {
                'email': email,
                'username': request.POST.get('username'),  # Agrega el campo username si lo deseas
                # Otros campos personalizados que quieras guardar
            }
            ref = db.reference('usuarios')  # Reemplaza 'usuarios' con la ruta en tu base de datos
            ref.child(user.uid).set(user_data)

        except Exception as e:
            # Manejo de errores
            pass

    return render(request, 'registro.html')

from django.shortcuts import render
from firebase_admin import auth
from firebase_admin import db

def register_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=f"{first_name} {last_name}"
            )
            
            # Usuario creado exitosamente en Firebase Authentication
            
            # Ahora, guardamos los datos del alumno en la base de datos en tiempo real
            student_data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                # Otros campos personalizados que quieras guardar
            }
            ref = db.reference('usuarios')  # Reemplaza 'alumnos' con la ruta correcta en tu base de datos
            ref.child(user.uid).set(student_data)
            
        except Exception as e:
            # Puedes manejar errores de manera más específica, como imprimirlos o registrarlos
            print("Error al registrar alumno:"), str(e)

    return render(request, 'registroalumn.html')


def register_profesor(request):
    if request.method == 'POST':
        nombreap = request.POST.get('nombreap')
        apellidoap = request.POST.get('apellidoap')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=f"{nombreap} {apellidoap}"
            )
            
            # Usuario creado exitosamente en Firebase Authentication
            
            # Ahora, guardamos los datos del alumno en la base de datos en tiempo real
            Apoderados_data = {
                'nombreap': nombreap,
                'apellidoap': apellidoap,
                'email': email,
                # Otros campos personalizados que quieras guardar
            }
            ref = db.reference('Apoderados')  # Reemplaza 'alumnos' con la ruta correcta en tu base de datos
            ref.child(user.uid).set(Apoderados_data)
            
        except Exception as e:
            # Puedes manejar errores de manera más específica, como imprimirlos o registrarlos
            print("Error al registrar alumno:"), str(e)

    return render(request, 'registrarapo.html')





def register_profesor2(request):
    if request.method == 'POST':
        nombreap = request.POST.get('nombreap')
        apellidoap = request.POST.get('apellidoap')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=f"{nombreap} {apellidoap}"
            )
            
            # Usuario creado exitosamente en Firebase Authentication
            
            # Ahora, guardamos los datos del alumno en la base de datos en tiempo real
            Apoderados_data = {
                'nombreap': nombreap,
                'apellidoap': apellidoap,
                'email': email,
                # Otros campos personalizados que quieras guardar
            }
            ref = db.reference('Profesor')  # Reemplaza 'alumnos' con la ruta correcta en tu base de datos
            ref.child(user.uid).set(Apoderados_data)
            
        except Exception as e:
            # Puedes manejar errores de manera más específica, como imprimirlos o registrarlos
            print("Error al registrar Profesor:"), str(e)

    return render(request, 'regristroprofesor.html')




from firebase_admin import exceptions

from django.shortcuts import render
from django.http import HttpResponse
from firebase_admin import db , initialize_app



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def create_annotation(request):
    if request.method == 'POST':
        user = request.user  # El usuario actual
        text = request.POST.get('text')
        
        # Almacena la anotación en Firebase
        ref = db.reference(f'anotaciones_usuario/{user.id}')
        new_annotation = ref.push()
        new_annotation.set({'text': text})

        return redirect('alumno')
    return render(request, 'anotaciones.html')


def get_all_user_data(request):
    # Recupera todos los datos de usuarios desde Firebase Realtime Database
    ref = db.reference('usuarios')
    users_data = ref.get()

    users = []  # Lista para almacenar los datos de usuarios

    # Itera a través de los datos de usuarios y extrae first_name y last_name
    if users_data:
        for user_id, user_info in users_data.items():
            first_name = user_info.get('first_name', '')
            last_name = user_info.get('last_name', '')
            users.append({'first_name': first_name, 'last_name': last_name})

    return render(request, 'all_users.html', {'users': users})




def anotaciones_form1(request):
    # Recupera los datos de usuarios desde Firebase Realtime Database
    ref = db.reference('usuarios')
    users_data = ref.get()

    users = []  # Lista para almacenar los datos de usuarios

    # Itera a través de los datos de usuarios y extrae first_name y last_name
    if users_data:
        for user_id, user_info in users_data.items():
            first_name = user_info.get('first_name', '')
            last_name = user_info.get('last_name', '')
            users.append({'first_name': first_name, 'last_name': last_name})

    if request.method == 'POST':
        usuario = request.POST['usuario']
        anotacion = request.POST['anotacion']
        
        # Procesa y guarda la anotación en tu base de datos de Firebase
        # Supongamos que deseas guardar la anotación en una ubicación llamada "anotaciones"
        ref_anotaciones = db.reference('anotaciones')
        new_anotacion_ref = ref_anotaciones.push()
        new_anotacion_ref.set({
            "usuario": usuario,
            "anotacion": anotacion
        })

    return render(request, 'anotaciones.html', {'users': users})



def anotaciones_form(request):
    # Recupera los datos de anotaciones desde Firebase Realtime Database
    ref_anotaciones = db.reference('anotaciones')
    anotaciones_data = ref_anotaciones.get()

    anotaciones = []  # Lista para almacenar los datos de anotaciones

    # Itera a través de los datos de anotaciones y extrae la información
    if anotaciones_data:
        for anotacion_id, anotacion_info in anotaciones_data.items():
            anotacion = anotacion_info.get('anotacion', '')
            usuario = anotacion_info.get('usuario', '')
            anotaciones.append({'anotacion': anotacion, 'usuario': usuario})

    return render(request, 'anotacionesapo.html', {'anotaciones': anotaciones})



def listar_materias(request):
    # Recupera los datos de las materias desde Firebase Realtime Database
    ref = db.reference('asignaturas')

    materias = {}
    for i in range(1, 8):
        materia_ref = ref.child(f'materia{i}')
        materia_data = materia_ref.get()
        if materia_data:
            materias[f'materia{i}'] = materia_data

    return render(request, 'asignaturas.html', {'materias': materias})






def guardar_nota(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        usuario_id = request.POST['usuario']
        apoderado_id = request.POST['apoderado']
        curso_id = request.POST['curso']
        nota = request.POST['nota']
        asignatura_id = request.POST['asignatura']

        # Crear un nuevo nodo en la colección 'notas'
        ref_notas = db.reference('notas')
        nueva_nota = {
            'usuario_id': usuario_id,
            'apoderado_id': apoderado_id,
            'curso_id': curso_id,
            'nota': nota,
            'asignatura_id': asignatura_id,  # Agregar el campo de asignatura
        }

        # Genera una nueva clave única para la anotación
        nueva_clave = ref_notas.push(nueva_nota)

        # Puedes almacenar la clave generada para futuras referencias si es necesario
        nueva_clave_id = nueva_clave.key

        # Resto del código para manejar la respuesta, redireccionar, etc.

    # Recupera los datos de usuarios, apoderados, cursos y asignaturas desde Firebase Realtime Database
    ref_usuarios = db.reference('usuarios')
    ref_apoderados = db.reference('Apoderados')
    ref_cursos = db.reference('Curso')
    ref_asignaturas = db.reference('asignaturas')  # Nueva referencia para 'asignaturas'

    usuarios_data = ref_usuarios.get()
    apoderados_data = ref_apoderados.get()
    curso_data = ref_cursos.get()
    asignaturas_data = ref_asignaturas.get()  # Nuevos datos de asignaturas

    usuarios = []  # Lista para almacenar los datos de usuarios
    apoderados = []  # Lista para almacenar los datos de apoderados
    curso = []  # Lista para almacenar los datos de "Curso"
    asignaturas = []  # Nueva lista para almacenar los datos de asignaturas

    # Itera a través de los datos de usuarios y extrae first_name y last_name
    if usuarios_data:
        for user_id, user_info in usuarios_data.items():
            first_name = user_info.get('first_name', '')
            last_name = user_info.get('last_name', '')
            usuarios.append({'id': user_id, 'first_name': first_name, 'last_name': last_name})

    # Itera a través de los datos de apoderados y extrae nombreap y apellidoap
    if apoderados_data:
        for apoderado_id, apoderado_info in apoderados_data.items():
            nombreap = apoderado_info.get('nombreap', '')
            apellidoap = apoderado_info.get('apellidoap', '')
            apoderados.append({'id': apoderado_id, 'nombreap': nombreap, 'apellidoap': apellidoap})

    # Itera a través de los datos de "Curso"
    if curso_data:
        for curso_id, curso_info in curso_data.items():
            curso.append({'id': curso_id, 'data': curso_info})

    # Itera a través de los datos de asignaturas
    if asignaturas_data:
        for asignatura_id, asignatura_info in asignaturas_data.items():
            asignaturas.append({'id': asignatura_id, 'data': asignatura_info})

    return render(request, 'notas.html', {'usuarios': usuarios, 'apoderados': apoderados, 'curso': curso, 'asignaturas': asignaturas})











from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials 
import io


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = auth.get_user_by_email(email)
            auth.sign_in_with_email_and_password(email, password)
            # El usuario ha iniciado sesión exitosamente

            # Redirigir al usuario a la vista de alumno (o donde desees)
            return redirect('alumno')  # 'alumno' es el nombre de la vista de alumno

        except Exception as e:
            # Manejo de errores
            messages.error(request, 'Error al iniciar sesión. Verifica tu correo y contraseña.')
            print()

    return render(request, 'login.html')
#necesimaos recueprar la contraseña encriptada 

def subir_archivo(request):

    return render(request, 'actividadesp.html')


def descargar_archivo(request):
    return render(request, 'actividaesAlmno.html')


def obtener_notas(request):
    # Accede a la referencia de la colección 'notas' en Firebase
    ref_notas = db.reference('notas')

    # Obtiene todos los datos de la colección 'notas'
    notas_data = ref_notas.get()

    # Inicializa una lista para almacenar las notas con información de usuario, apoderado, curso y asignatura
    notas_con_usuario_apoderado_curso_asignatura = []

    if notas_data:
        for nota_id, nota_info in notas_data.items():
            usuario_id = nota_info.get('usuario_id', '')
            usuario_data = obtener_informacion_usuario(usuario_id)

            apoderado_id = nota_info.get('apoderado_id', '')
            apoderado_data = obtener_informacion_apoderado(apoderado_id)

            curso_id = nota_info.get('curso_id', '')
            curso_data = obtener_informacion_curso(curso_id)

            asignatura_id = nota_info.get('asignatura_id', '')
            asignatura_data = obtener_informacion_asignatura(asignatura_id)

            notas_con_usuario_apoderado_curso_asignatura.append({
                'id': nota_id,
                'data': nota_info,
                'usuario': usuario_data,
                'apoderado': apoderado_data,
                'curso': curso_data,
                'asignatura': asignatura_data
            })

    return render(request, 'notasal.html', {'notas': notas_con_usuario_apoderado_curso_asignatura})



def obtener_notas2(request):
    # Accede a la referencia de la colección 'notas' en Firebase
    ref_notas = db.reference('notas')

    # Obtiene todos los datos de la colección 'notas'
    notas_data = ref_notas.get()

    # Inicializa una lista para almacenar las notas con información de usuario, apoderado, curso y asignatura
    notas_con_usuario_apoderado_curso_asignatura = []

    if notas_data:
        for nota_id, nota_info in notas_data.items():
            usuario_id = nota_info.get('usuario_id', '')
            usuario_data = obtener_informacion_usuario(usuario_id)

            apoderado_id = nota_info.get('apoderado_id', '')
            apoderado_data = obtener_informacion_apoderado(apoderado_id)

            curso_id = nota_info.get('curso_id', '')
            curso_data = obtener_informacion_curso(curso_id)

            asignatura_id = nota_info.get('asignatura_id', '')
            asignatura_data = obtener_informacion_asignatura(asignatura_id)

            notas_con_usuario_apoderado_curso_asignatura.append({
                'id': nota_id,
                'data': nota_info,
                'usuario': usuario_data,
                'apoderado': apoderado_data,
                'curso': curso_data,
                'asignatura': asignatura_data
            })

    return render(request, 'notasprofe.html', {'notas': notas_con_usuario_apoderado_curso_asignatura})
def obtener_informacion_usuario(usuario_id):
    # Accede a la referencia de la colección 'usuarios' en Firebase
    ref_usuarios = db.reference('usuarios')

    # Realiza una consulta para obtener los datos del usuario por su ID
    usuario_data = ref_usuarios.child(usuario_id).get()

    if usuario_data:
        # Suponiendo que el campo 'first_name' y 'last_name' existen en los datos del usuario
        first_name = usuario_data.get('first_name', '')
        last_name = usuario_data.get('last_name', '')
        return {'first_name': first_name, 'last_name': last_name}
    else:
        return {'first_name': '', 'last_name': ''}
    


def obtener_informacion_apoderado(apoderado_id):
    # Realiza una consulta a la colección de apoderados en Firebase y obtén los datos del apoderado
    ref_apoderados = db.reference('Apoderados')
    apoderado_data = ref_apoderados.child(apoderado_id).get()

    if apoderado_data:
        # Suponiendo que el campo 'nombreap' y 'apellidoap' existen en los datos del apoderado
        nombreap = apoderado_data.get('nombreap', '')
        apellidoap = apoderado_data.get('apellidoap', '')
        return {'nombreap': nombreap, 'apellidoap': apellidoap}
    else:
        return {'nombreap': '', 'apellidoap': ''}
    
def obtener_informacion_asignatura(asignatura_id):
    if not asignatura_id:
        return {'nombre_asignatura': ''}

    # Realiza una consulta a la colección de asignaturas en Firebase y obtén el nombre de la asignatura directamente
    ref_asignaturas = db.reference('asignaturas')
    nombre_asignatura = ref_asignaturas.child(asignatura_id).get()

    if nombre_asignatura:
        return {'nombre_asignatura': nombre_asignatura}
    else:
        return {'nombre_asignatura': ''}
    
def obtener_informacion_curso(curso_id):
    if not curso_id:
        return {'nombre_curso': ''}

    # Realiza una consulta a la colección de cursos en Firebase y obtén el nombre del curso directamente
    ref_cursos = db.reference('Curso')
    nombre_curso = ref_cursos.child(curso_id).get()

    if nombre_curso:
        return {'nombre_curso': nombre_curso}
    else:
        return {'nombre_curso': ''}
    
def upload_file(request):
    if request.method == 'POST' and request.FILES['archivo']:
        archivo = request.FILES['archivo']
        bucket = storage.bucket()
        carpeta_destino = 'actividades/'  # Nombre de la carpeta 'actividades'
        archivo_destino = f'{carpeta_destino}{archivo.name}'  # Ruta completa al archivo

        # Sube el archivo a Firebase Storage
        blob = bucket.blob(archivo_destino)
        blob.upload_from_file(archivo)

        # Redirige a la URL 'profesores/' después de subir el archivo
        return HttpResponseRedirect('/profesores/')

    return render(request, 'upload_form.html')



from datetime import timedelta  # Agrega esta importación


def gestionar_archivos(request):
    # Crea una instancia del cliente de Firebase Storage
    bucket = storage.bucket()

    # Listar archivos en un directorio específico
    directory_path = 'actividades/'  # Reemplaza con la carpeta que deseas listar
    blobs = bucket.list_blobs(prefix=directory_path)

    # Crea una lista de enlaces de descarga para cada archivo
    archivos = []
    for blob in blobs:
        archivo_name = blob.name
        archivo_url = blob.generate_signed_url(
            version="v4",
            expiration=timedelta(minutes=15),  # Puedes ajustar el tiempo de expiración
            method="GET",
        )
        archivos.append({'nombre': archivo_name, 'url': archivo_url})

    # Puedes procesar los resultados como desees, por ejemplo, pasarlos al template HTML
    context = {'archivos': archivos}

    # Llama a la función para gestionar archivos cuando sea necesario y devuelve la lista de archivos
    return render(request, 'actividaesAlmno.html', context)



def gestionar_archivos2(request):
    # Crea una instancia del cliente de Firebase Storage
    bucket = storage.bucket()

    # Listar archivos en un directorio específico
    directory_path = 'archivo/'  # Reemplaza con la carpeta que deseas listar
    blobs = bucket.list_blobs(prefix=directory_path)

    # Crea una lista de enlaces de descarga para cada archivo
    archivos = []
    for blob in blobs:
        archivo_name = blob.name
        archivo_url = blob.generate_signed_url(
            version="v4",
            expiration=timedelta(minutes=15),  # Puedes ajustar el tiempo de expiración
            method="GET",
        )
        archivos.append({'nombre': archivo_name, 'url': archivo_url})

    # Puedes procesar los resultados como desees, por ejemplo, pasarlos al template HTML
    context = {'archivos': archivos}

    # Llama a la función para gestionar archivos cuando sea necesario y devuelve la lista de archivos
    return render(request, 'asusntosestudiantiles.html', context)





def notasedit(request):
    # Recuperar una referencia a la colección "notas"
    notas_ref = db.reference('notas')
    
    if request.method == 'POST':
        accion = request.POST.get('accion')
        nota_id = request.POST.get('nota_id')
        
        if accion == 'editar':
            # Aquí puedes implementar la lógica para editar una nota específica
            # Puedes recuperar la nota por su ID y luego procesar la edición
            apoderado_id = request.POST.get('apoderado_id')
            asignatura_id = request.POST.get('asignatura_id')
            curso_id = request.POST.get('curso_id')
            nota = request.POST.get('nota')
            usuario_id = request.POST.get('usuario_id')
            
            # Verificar si algún campo es None y asignar un valor predeterminado si es necesario
            apoderado_id = apoderado_id or 'valor_predeterminado_apoderado'
            asignatura_id = asignatura_id or 'valor_predeterminado_asignatura'
            curso_id = curso_id or 'valor_predeterminado_curso'
            nota = nota or 'valor_predeterminado_nota'
            usuario_id = usuario_id or 'valor_predeterminado_usuario'
            
            notas_ref.child(nota_id).update({
                'apoderado_id': apoderado_id,
                'asignatura_id': asignatura_id,
                'curso_id': curso_id,
                'nota': nota,
                'usuario_id': usuario_id
            })
            
        elif accion == 'eliminar':
            # Aquí puedes implementar la lógica para eliminar una nota específica
            notas_ref.child(nota_id).delete()

        return redirect('notas')

    # Recuperar todos los registros de la colección
    notas_data = notas_ref.get()
    
    campos_notas = []
    if notas_data:
        for nota_id, nota_info in notas_data.items():
            apoderado_id = nota_info.get('apoderado_id')
            asignatura_id = nota_info.get('asignatura_id')
            curso_id = nota_info.get('curso_id')
            nota = nota_info.get('nota')
            usuario_id = nota_info.get('usuario_id')
            
            # Utiliza las funciones auxiliares para obtener los datos específicos
            apoderado_info = obtener_informacion_apoderado(apoderado_id)
            asignatura_info = obtener_informacion_asignatura(asignatura_id)
            curso_info = obtener_informacion_curso(curso_id)
            usuario_info = obtener_informacion_usuario(usuario_id)
            
            campos_notas.append({
                'apoderado_info': apoderado_info,
                'asignatura_info': asignatura_info,
                'curso_info': curso_info,
                'nota': nota,
                'usuario_info': usuario_info,
                'nota_id': nota_id
            })

    asignaturas = obtener_todas_las_asignaturas()
    cursos = obtener_todos_los_cursos()

    return render(request, 'notas.html', {'notas_data': campos_notas, 'asignaturas': asignaturas, 'cursos': cursos})



def obtener_todas_las_asignaturas():
    ref_asignaturas = db.reference('asignaturas')
    asignaturas_data = ref_asignaturas.get()

    asignaturas = []
    if asignaturas_data:
        for asignatura_id in asignaturas_data.keys():
            asignaturas.append({'id': asignatura_id})

    return 

def obtener_todos_los_cursos():
    ref_cursos = db.reference('Curso')
    cursos_data = ref_cursos.get()

    cursos = []
    if cursos_data:
        for curso_id in cursos_data.keys():
            cursos.append({'id': curso_id})

    return cursos


def gestionar_notas(request):
    # Recuperar una referencia a la colección "notas"
    notas_ref = db.reference('notas')

    if request.method == 'POST':
        # Verificar si se envió una solicitud POST para eliminar una nota
        nota_id_a_eliminar = request.POST.get('nota_id_a_eliminar')
        if nota_id_a_eliminar:
            # Eliminar la nota de la base de datos
            notas_ref.child(nota_id_a_eliminar).delete()
            return redirect('gestionar_notas')

    # Recuperar todas las notas
    notas_data = notas_ref.get()

    # Crear una lista para almacenar las notas con información de usuario, apoderado, curso y asignatura
    notas_con_usuario_apoderado_curso_asignatura = []

    if notas_data:
        for nota_id, nota_info in notas_data.items():
            usuario_id = nota_info.get('usuario_id', '')
            usuario_data = obtener_informacion_usuario(usuario_id)

            apoderado_id = nota_info.get('apoderado_id', '')
            apoderado_data = obtener_informacion_apoderado(apoderado_id)

            curso_id = nota_info.get('curso_id', '')
            curso_data = obtener_informacion_curso(curso_id)

            asignatura_id = nota_info.get('asignatura_id', '')
            asignatura_data = obtener_informacion_asignatura(asignatura_id)

            notas_con_usuario_apoderado_curso_asignatura.append({
                'id': nota_id,
                'data': nota_info,
                'usuario': usuario_data,
                'apoderado': apoderado_data,
                'curso': curso_data,
                'asignatura': asignatura_data
            })

    return render(request, 'editar_nota.html', {'notas_data': notas_con_usuario_apoderado_curso_asignatura})




def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Inicia sesión con correo y contraseña usando Firebase Authentication
            user = auth.get_user_by_email(email)
            auth_user = auth.sign_in_with_email_and_password(email, password)
            
            # Puedes realizar acciones adicionales, como comprobar si el usuario existe en tu base de datos local.
            
            # Redirige a la página 'alumno' después del inicio de sesión exitoso
            return redirect('alumno')
            
        except auth.AuthError:
            # Maneja errores de autenticación, por ejemplo, credenciales incorrectas
            return render(request, 'login.html', {'error_message': 'Error de autenticación'})

    return render(request, 'login.html')



