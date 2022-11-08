from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from gestion.models import Informacion
from gestion.forms import formularioInformacion
from django.contrib import messages

# Create your views here.

class FormularioInformacionView(HttpRequest):
    def index(request):
        data = {
            'form': formularioInformacion()
        }
        if request.method == 'POST':
            formulario = formularioInformacion(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Producto registrado correctamente")
                return redirect(to='http://127.0.0.1:8000/lista/')
            else:
                data["form"] = formulario
        return render(request, 'informacionIndex.html', data)

    def modificar_producto(request, id):
        producto = get_object_or_404(Informacion, id=id)
        # print('producto:',producto.cantidad_productos)
        data = {
            'form': formularioInformacion(instance=producto),
            'info': Informacion.objects.get(id=id)
        }
        # print(data['info'])
        # print('data:', data['info'].cantidad_productos)
        # print('data:',data['form'])
        if request.method == 'POST':
            formulario = formularioInformacion(data=request.POST, instance=producto, files = request.FILES)
            if formulario.is_valid():
                # producto.update(**formulario.cleaned_data)
                producto.save()
                messages.success(request, "Producto modificado correctamente")
                return redirect(to='http://127.0.0.1:8000/lista/')
            data["form"] = formulario
        return render(request, 'modificar_producto.html', data)
    
    def eliminar_producto(request, id):
        producto = get_object_or_404(Informacion, id=id)
        producto.delete()
        messages.success(request, "Producto eliminado correctamente")
        return redirect(to='http://127.0.0.1:8000/lista/')
