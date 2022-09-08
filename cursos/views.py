from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.
def createCurso(request):
    if request.method == 'POST':
        #print(request.POST)
        #print(request.POST['descripcion'])
        descripcion = request.POST['descripcion']

        #curso = Curso()
        #curso.descripcion = descripcion
        #curso.save()
        Curso.objects.create(descripcion=descripcion)
        return redirect("/curso/lista/")
    return render(request, 'cursos/create.html')


def list_curso(request):
    curso_list = Curso.objects.all()
    context = {
        'curso_list': curso_list,
    }
    return render(request, 'cursos/list.html',context)

def update_curso(request, pk):
    curso = Curso.objects.get(id=pk)
    #Curso.objects.filter(id=pk).first().update(descripcion=descripcion)
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        curso.descripcion = descripcion
        curso.save()
        print("actualizado Correctamente")
        return redirect("/curso/lista/")

    context = {'curso':curso}
    return render(request, 'cursos/update.html',context)

def delete_curso(request, pk):
    Curso.objects.get(pk=pk).delete()
    print('Se Borró el curso')
    curso_list = Curso.objects.all()
    context = {
        'curso_list': curso_list,
    }
    #return render(request, 'website/index.html',context)
    return redirect("/curso/lista/")