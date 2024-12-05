from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomLoginForm, CustomSignupForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import Persona, Curso

def index(request):
    return render(request, 'index.html')

def myaccount(request):
    return render(request, 'myaccount.html')

def get(self, request, *args, **kwargs):
    if 'login_error' in request.session:
        del request.session['login_error']
    return super().get(request, *args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm
    def form_invalid(self, form):
        previous_url = self.request.META.get('HTTP_REFERER', '/')
        self.request.session['login_error'] = "Usuario o contraseña incorrectos"
        return HttpResponseRedirect(previous_url)

class SignUpView(CreateView):
    form_class = CustomSignupForm
    success_url = '/'
    template_name = "registration/signup.html"
    def form_invalid(self, form):
        previous_url = self.request.META.get('HTTP_REFERER', '/')
        self.request.session['signup_error'] = "Hubo un error en el registro. Por favor, verifica los campos."
        return HttpResponseRedirect(previous_url)

def crear_persona(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        if nombre and apellido and edad:
            Persona.objects.create(nombre=nombre, apellido=apellido, edad=int(edad))
            return redirect('listar_personas')     
    return render(request, 'crear_persona.html')

def listar_personas(request):
    personas = Persona.objects.all()
    return render(request, 'listar_personas.html', {'personas': personas})

def actualizar_persona(request, rut):
    persona = get_object_or_404(Persona, rut=rut)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        if nombre and apellido and edad:
            persona.nombre = nombre
            persona.apellido = apellido
            persona.edad = int(edad)
            persona.save()
            return redirect('listar_personas')
    return render(request, 'actualizar_persona.html', {'persona': persona})

def eliminar_persona(request, rut):
    persona = get_object_or_404(Persona, rut=rut)
    if request.method == 'POST':
        persona.delete()
        return redirect('listar_personas')
    return render(request, 'eliminar_persona.html', {'persona': persona})

def crear_curso(request):
    personas = Persona.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        id_profesor = request.POST['id_profesor']
        if nombre and descripcion and id_profesor:
            Curso.objects.create(nombre=nombre, descripcion=descripcion, id_profesor_id=int(id_profesor))
            return redirect('listar_cursos')
    return render(request, 'crear_curso.html', {'personas': personas})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

def actualizar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    personas = Persona.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        id_profesor = request.POST['id_profesor']
        if nombre and descripcion and id_profesor:
            curso.nombre = nombre
            curso.descripcion = descripcion
            curso.id_profesor_id = int(id_profesor)
            curso.save()
            return redirect('listar_cursos')
    return render(request, 'actualizar_curso.html', {'curso': curso, 'personas': personas})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'eliminar_curso.html', {'curso': curso})



