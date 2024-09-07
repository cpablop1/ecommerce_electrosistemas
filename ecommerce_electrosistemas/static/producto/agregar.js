import { listar } from "./listar.js";

export function agregar(formulario) {
    let data = new FormData(formulario); // Creamos un objeto FormDato para enviarlo a servidor

    fetch('/producto/agregar-producto/', {
        method: 'POST',
        body: data, // El cuerpo de la peticion enviamos el fulumario formateado
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // En el encabezado de la petición incluimos el token de seguridad
        }
    }).then((res) => {
        return res.json(); // Convertimos la respuesta del servidor a un objecto JSON
    }).then((res) => {
        if (res.res) { // Si la respuesta fue exitosa
            formulario.reset(); // Limpiamos el formulario
            bootstrap.Modal.getInstance(document.getElementById('modal_producto')).hide(); // Y Ocultamos la ventana modal
            listar();
            alert(res.msg);
        } else {
            alert('Hubo un en el servidor'); // Caso contrario lanzamos una alerta
        }
    }).catch(error => { // Si la petición tuvo problemas
        console.log(error);
        alert('Hubo un error al registrar el producto');
    });

}