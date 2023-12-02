from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.views.generic import ListView
from .models import Item, Objeto, Usuario
from django.core.mail import send_mail
from django.conf import settings
from .forms import FormularioContacto, FormularioItems
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def salir(request):
    logout(request)
    return redirect('Inicio')

def nada(request):
    return render(request, 'nope.html', {})

def inicio(request):
    return render(request, 'inicio.html', {})

def seccionItems(request):
    itemsListado = Item.objects.all()
    #itemsListado = Item.objects.filter(nombre__contains='key')
    data = {
        'titulo': 'Gestion de Items',
        'items': itemsListado
    }
    #return render(request, 'item.html', {"item":itemsListado})
    return render(request, 'item.html', data)

class ItemsListaView(ListView):
    model = Item
    template_name = 'item.html'
 
@login_required   
def formularioItems(request):
    return render(request, "formItems.html")

@login_required
def itemBusqueda(request):
    return render(request, "buscarItems.html")

@login_required
def buscarItem(request):
    if request.GET["nombre"]:
        mensaje = ""
        nombre = request.GET["nombre"]
        if len(nombre)>20:
            mensaje = "El texto es demasiado largo"
        else:
            item = Item.objects.filter(nombre__icontains=nombre)
            return render(request, "resultadoItem.html", 
            {"item": item, "nombre": nombre, "mensaje": mensaje})
    else:
        mensaje = "No has introducido nada"
        
    return render(request, "resultadoItem.html", {"mensaje": mensaje})

@login_required
def itemFormulario(request):
    if request.method == 'POST':
        miForm = FormularioItems(request.POST)
        print(miForm)
        if miForm.is_valid():
            info = miForm.cleaned_data
            item = Item(nombre=info['nombre'], precio=info['precio'])
            item.save()
            return render(request, "item.html")
    else:
        miForm = FormularioItems()
    return render(request, "formItems.html", {"form": miForm})

@login_required
def contacto(request):
    if request.method=="POST":
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'], 
            infForm.get('email',''), ['gonzalo8457@gmail.com'],)
            
            return render(request, "gracias.html")
        #subject = request.POST["asunto"]
        #message = request.POST["mensaje"] + " " + request.POST["email"]
        #email_from = settings.EMAIL_HOST_USER
        #recipient_list = ["gonzalo8457@gmail.com"]
        #send_mail(subject, message, email_from, recipient_list)
        #return render(request, "gracias.html")
    else:
        miFormulario = FormularioContacto()
        
    return render(request, "contacto.html", {"form": miFormulario})