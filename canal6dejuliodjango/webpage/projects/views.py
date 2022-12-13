from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Tag, Entrada
from .forms import ContactoForm
from django.views import generic

def home(request):
    estatus = 'renta'
    projects = Project.objects.all().order_by('-year')
    entradas = Entrada.objects.all()
    tags = Project.objects.filter(tags__name='Estreno')
    form = ContactoForm()
    if request.method == 'POST':
        form =ContactoForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'estatus':estatus, 'projects': projects, 'estrenos':tags, 'entradas':entradas, 'form':form}
    return render(request, 'main.html', context)


def project(request, slug=None):
    entradas = Entrada.objects.get(slug=slug)
    context = {'entradas':entradas,}
    return render(request, 'projects/blogpost.html', context)

def post(request,slug):
    post = Entrada.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'projects/blogpost.html', context)

def projects(request):
    projects = Project.objects.all()
    context =  {'projects': projects}
    return render(request, 'projects/projects.html' , context)