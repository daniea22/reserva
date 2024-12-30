from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import EspacioDeEstudio, Cliente, Reserva


# Presentar el inicio
def inicio(request):
    espacios = EspacioDeEstudio.objects.all()  # Obtenemos todos los espacios
    return render(request, 'inicio.html', {'espacios': espacios})
#########################################
######
def crear_espacio(request):
    return render(request, 'crear_espacio.html')

# Guardar un nuevo espacio

def guardar_espacio(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('txt_nombre')
        ubicacion = request.POST.get('txt_ubicacion')
        capacidad = request.POST.get('txt_capacidad')
        descripcion = request.POST.get('txt_descripcion')
        disponible = request.POST.get('disponible') == 'SI'
        imagen = request.FILES.get('imagen', None)

        # Crear el nuevo espacio y guardarlo en la base de datos
        nuevoespacio = EspacioDeEstudio.objects.create(
            nombre=nombre,
            ubicacion=ubicacion,
            capacidad=capacidad,
            descripcion=descripcion,
            disponible=disponible,
            imagen=imagen
        )

        # Mensaje de éxito
        messages.success(request, "Espacio agregado exitosamente.")

        # Redirigir a la lista de espacios
        return redirect('lista_espacios')  # Aquí rediriges a la vista que tiene el nombre 'lista_espacios'

# Editar un espacio existente
def editar_espacio(request, id):
    espacio = get_object_or_404(EspacioDeEstudio, id=id)
    if request.method == 'POST':
        espacio.nombre = request.POST.get('txt_nombre')
        espacio.ubicacion = request.POST.get('txt_ubicacion')
        espacio.capacidad = request.POST.get('txt_capacidad')
        espacio.descripcion = request.POST.get('txt_descripcion')
        espacio.disponible = request.POST.get('disponible') == 'SI'
        espacio.imagen=request.FILES.get('imagen', None)
        espacio.save()
        messages.success(request, "Espacio actualizado exitosamente.")
        return redirect('lista_espacios')

    return render(request, 'editar_espacio.html', {'espacio': espacio})

# Eliminar un espacio
def eliminar_espacio(request, id):
    try:
        # Obtener el espacio por id
        espacio_a_eliminar = EspacioDeEstudio.objects.get(id=id)
        # Eliminar el espacio
        espacio_a_eliminar.delete()
        messages.success(request, "Espacio eliminado exitosamente.")
    except EspacioDeEstudio.DoesNotExist:
        # Si no existe el espacio con ese id
        messages.error(request, "El espacio que intentas eliminar no existe.")
        return redirect('lista_espacios')  # Redirige a la lista de espacios si no se encuentra el espacio

    # Redirige a la lista de espacios después de eliminar
    return redirect('lista_espacios')


def lista_espacios(request):
    espaciosBdd = EspacioDeEstudio.objects.all()
    return render(request, 'lista_espacios.html', {'espacios': espaciosBdd})

######################################################################################################################################################
#crear cliente
def crear_cliente(request):
    return render(request, 'crear_cliente.html')

####################################
#guardar cliente
def guardar_cliente(request):
    if request.method == 'POST':
        # Capturar los datos del formulario
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')

        # Crear un nuevo cliente y guardar en la base de datos
        nuevocliente = Cliente.objects.create(
            nombre=nombre,
            correo=correo,
            telefono=telefono
        )
        nuevocliente.save()

        # Mensaje de éxito
        messages.success(request, "Cliente creado exitosamente.")
        return redirect('lista_cliente')  # Redirigir a la lista de clientes

    return render(request, 'crear_cliente.html')
###################################################################################
#editar clientes
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')

        # Actualizar el cliente
        cliente.nombre = nombre
        cliente.correo = correo
        cliente.telefono = telefono
        cliente.save()

        messages.success(request, "Cliente actualizado exitosamente.")
        return redirect('lista_cliente')

    return render(request, 'editar_cliente.html', {'cliente': cliente})
##########################################################
#listar cliente 
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Obtiene todos los clientes
    return render(request, 'lista_cliente.html', {'clientes': clientes})
##################################################################################
#Elimnar cliente
def eliminar_cliente(request, id):
    # Obtener el cliente a eliminar
    cliente = get_object_or_404(Cliente, id=id)

    # Eliminar el cliente
    cliente.delete()

    # Mensaje de éxito
    messages.success(request, "Cliente eliminado exitosamente.")
    
    # Redirigir a la lista de clientes
    return redirect('lista_cliente')

####################################################################################################
#Crear reserva
def crear_reserva(request):
    clientes = Cliente.objects.all()
    espacios = EspacioDeEstudio.objects.all()
    return render(request, 'crear_reserva.html', {
        'clientes': clientes,
        'espacios': espacios
    })



#crear reserva
def guardar_reserva(request):
    clientes = Cliente.objects.all()
    espacios = EspacioDeEstudio.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('sel_cliente')
        espacio_id = request.POST.get('sel_espacio')
        fecha_reserva = request.POST.get('fecha_reserva')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fin = request.POST.get('hora_fin')

        print(f"Cliente ID: {cliente_id}, Espacio ID: {espacio_id}")  # Depuración

        try:
            cliente = Cliente.objects.get(id=cliente_id)
            espacio = EspacioDeEstudio.objects.get(id=espacio_id)
        except Cliente.DoesNotExist:
            messages.error(request, "El cliente seleccionado no existe.")
            return redirect('crear_reserva')
        except EspacioDeEstudio.DoesNotExist:
            messages.error(request, "El espacio seleccionado no existe.")
            return redirect('crear_reserva')

        Reserva.objects.create(
            cliente=cliente,
            espacio=espacio,
            fecha_reserva=fecha_reserva,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin
        )

        messages.success(request, "Reserva creada exitosamente.")
        return redirect('lista_reserva')
    
    return render(request, 'crear_reserva.html', {
        'clientes': clientes,
        'espacios': espacios
    })


###############################################################
#listar reserva
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'lista_reserva.html', {'reservas': reservas})
####################################################################################3
#Eliminar
def eliminar_reserva(request, id):
    reservaeliminar = get_object_or_404(Reserva, id=id)
    reservaeliminar .delete()
    messages.success(request, "Reserva eliminada exitosamente.")
    return redirect('lista_reserva')

##################################################################
#editar reserva
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    clientes = Cliente.objects.all()
    espacios = EspacioDeEstudio.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('sel_cliente')
        espacio_id = request.POST.get('sel_espacio')
        fecha_reserva = request.POST.get('fecha_reserva')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fin = request.POST.get('hora_fin')

        cliente = get_object_or_404(Cliente, id=cliente_id)
        espacio = get_object_or_404(EspacioDeEstudio, id=espacio_id)

        # Actualiza los campos de la reserva
        reserva.cliente = cliente
        reserva.espacio = espacio
        reserva.fecha_reserva = fecha_reserva
        reserva.hora_inicio = hora_inicio
        reserva.hora_fin = hora_fin
        reserva.save()

        # Redirige a la lista de reservas con un mensaje de éxito
        messages.success(request, "Reserva actualizada exitosamente.")
        return redirect('lista_reserva')

    return render(request, 'editar_reserva.html', {
        'reserva': reserva,
        'clientes': clientes,
        'espacios': espacios
    })

#####################


