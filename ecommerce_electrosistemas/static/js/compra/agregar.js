import { listar_detalle_compras } from "./listar_detalle_compras.js";

export function agregar(data) {
    //let form_data = new FormData(data); // Creamos un objeto FormDato para enviarlo a servidor

    fetch('/compra/agregar-compra/', {
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
            listar_detalle_compras();
            //alert(res.msg);
        } else {
            alert('Hubo un en el servidor'); // Caso contrario lanzamos una alerta
        }
    }).catch(error => { // Si la petición tuvo problemas
        console.log(error);
        alert('Hubo un error al agregar productos al carrito');
    });

}