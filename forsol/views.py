# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404 
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Media, subir_media
from django.db.models import Q
from .forms import ContactoForm, FormPost, FormSubirMedia
import os

# Create your views here.
def home(request):
    post = Post.objects.filter(categoria__icontains="Principal")
    return render(request, 'forsol/ver.html', {'posteos':post, 'titulos':'Home'})

def galeria(request):
    fotos = Media.objects.all()
    titulos = Media.objects.values_list('nombre', flat=True).distinct()
    print titulos
    return render(request, 'forsol/galeria.html', {'fotos':fotos, 'titulos':titulos})
    
def cargar_galeria(request):
    if request.method == 'GET':
        form = FormSubirMedia()
    else:
        form = FormSubirMedia(request.POST, request.FILES)
        if form.is_valid():
            subir = form.save(commit=False)
            #post.autor = request.user
            subir.save()
        return render(request, 'forsol/mensaje.html', {'msj':"<p><h1>Su imagen se cargo con exito!!</h2></p>"})
    
    return render(request, 'forsol/cargar.html', {'form':form})

def vista_contacto(request):
    mensaje = '<h2>Hemos recibido tu mensaje con exito!!</h2><p>Gracias por contactarnos, recibiras una respuesta muy pronto.</p>'
    if request.method == 'GET':
        form = ContactoForm()
    else:
        form = ContactoForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Nombre']
            from_email = form.cleaned_data['Correo']
            message = form.cleaned_data['Mensaje']
            try:
                send_mail(subject, message, from_email, ['galeanolukas@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            return render(request, 'forsol/mensaje.html', {'msj':mensaje})
    return render(request, "forsol/contacto.html", {'form': form})


@login_required
def post_nuevo(request):
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.autor = request.user
            post.fecha_post = timezone.now()
            post.save()
            return render(request, 'forsol/mensaje.html', {'msj':'<h2>Se publico con exito!!</h2>'})
    else:
        form = FormPost()
    return render(request, 'forsol/publicar.html', {'form': form})

@login_required
def editar_post(request, ID):
    instancia = Post.objects.get(id=ID)
    if request.method == "POST":
        form = FormPost(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            post = form.save(commit=False)
            post.fecha_post = timezone.now()
            post.save()
            return render(request, 'forsol/mensaje.html', {'msj':'<h2>Post editado con exito!!</h2>'})
    else:
        form = FormPost(instance=instancia)
        return render(request, 'forsol/editar.html', {'form': form, 'post':instancia})

def mostrar_post(request):
    busqueda = request.GET.get('search', '')
    querys = (Q(categoria__icontains=busqueda) |
              Q(titulo__icontains=busqueda) |
              Q(id__icontains=busqueda)
             )
    if busqueda == "todas":
        form = Post.objects.all()
    else:
        form = Post.objects.filter(querys)
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'forsol/ver.html', {'posteos':form, 'titulos':busqueda})
    
def borrar_post(request, ID):
        instancia = Post.objects.get(id=ID)
        instancia.delete()
        return render(request, 'forsol/mensaje.html', {'msj':'<h2>Se elimino el Post con exito!</h2>'})

        #return redirect('/')

@login_required
def registro(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)

        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "forsol/registro.html", {'form': form})


@login_required
def usuarios(request):
	return render(request, 'forsol/miembros.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    #messages.warning(request, "Deseas cerrar la sesion?")
    return redirect("/") 
