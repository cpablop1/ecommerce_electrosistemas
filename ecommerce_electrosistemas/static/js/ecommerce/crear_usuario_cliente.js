import { validar_usuario_cliente } from "./validar_usuario_cliente.js";

export function crear_usuario_cliente(formulario) {
    let data = new FormData(formulario); // Creamos un objeto FormDato para enviarlo a servidor

    fetch('/ecommerce/crear-usuario-cliente/', {
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
            alert(res.msg);
            window.location.href = '/ecommerce/iniciar-sesion/';
        } else {
            alert(res.msg); // Caso contrario lanzamos una alerta
        }
    }).catch(error => { // Si la petición tuvo problemas
        console.log(error);
        alert('Hubo un error al registrarte');
    });

}

window.onload = () => {
    document.getElementById('nombres').focus();
}

// Evento para crear usuario para el cliente
document.getElementById('form_crear_usuario_cliente').addEventListener('submit', e => {
    e.preventDefault();

    if (validar_usuario_cliente(e.target)) {
        crear_usuario_cliente(e.target);
    }
});