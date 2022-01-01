from django.shortcuts import render, redirect
from findcafe.models import Cafe
from findcafe.forms import CafeForm
from django.contrib import messages

# Create your views here.

def edit_cafe(request, id_cafe):
    cafe = Cafe.objects.get(id=id_cafe)
    template = 'edit-cafe.html'
    if request.POST:
        form = CafeForm(request.POST, instance=cafe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data changed successfully')
            return redirect('edit_cafe', id_cafe=id_cafe)
    else:
        form = CafeForm(instance=cafe)
        content = {
            'form' : form,
            'cafe': cafe,
            }
        return render(request, template, content)

def list_cafe(request):
    cafes = Cafe.objects.all()

    content = {
        'cafes' : cafes,
    }

    return render(request,'list-cafe.html', content)


def tambah_cafe(request):
    if request.POST:
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            form = CafeForm
            massage = 'Data saved successfully'
            content = {
            'form' : form,
            'massage': massage
            }
            return render(request, 'tambah-cafe.html', content)
        else:
            form = CafeForm
            massage = 'data was not saved successfully, something wrong!'
            content = {
            'form' : form,
            'massage': massage
            }
            return render(request, 'tambah-cafe.html', content)
    else:
        form = CafeForm
        
        content = {
            'form' : form,
        }
        return render(request, 'tambah-cafe.html', content)
