import { listar } from "./listar.js";

export function confirmar_venta(data) {

    fetch('/venta/confirmar-venta/', {
        method: 'POST',
        body: JSON.stringify(data), // El cuerpo de la peticion enviamos el fulumario formateado
        headers: {
            'Content-Type': 'application/json', // Indicamos que estamos enviando JSON
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // En el encabezado de la petición incluimos el token de seguridad
        }
    }).then((res) => {
        return res.json(); // Convertimos la respuesta del servidor a un objecto JSON
    }).then((res) => {
        if (res.res) { // Si la respuesta fue exitosa
            listar();
            bootstrap.Modal.getInstance(document.getElementById('modal_venta')).hide()
        } else {
            alert('Hubo un en el servidor'); // Caso contrario lanzamos una alerta
        }
    }).catch(error => { // Si la petición tuvo problemas
        console.log(error);
        alert('Hubo un error al confirmar la venta');
    });

}