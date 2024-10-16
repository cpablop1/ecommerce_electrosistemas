export function iniciar_sesion(formulario) {
    let data = new FormData(formulario); // Creamos un objeto FormDato para enviarlo a servidor

    fetch('/ecommerce/sesion/', {
        method: 'POST',
        body: data, // El cuerpo de la peticion enviamos el fulumario formateado
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // En el encabezado de la petición incluimos el token de seguridad
        }
    }).then((res) => {
        return res.json(); // Convertimos la respuesta del servidor a un objecto JSON
    }).then((res) => {
        console.log(res);
        if (res.res) { // Si la respuesta fue exitosa
            formulario.reset(); // Limpiamos el formulario
            window.location.href = '/ecommerce';
            alert(res.msg);
        } else {
            alert(res.msg); // Caso contrario lanzamos una alerta
            formulario.elements['usuario'].select();
        }
    }).catch(error => { // Si la petición tuvo problemas
        console.log(error);
        alert('Hubo un error al registrarte');
    });

}

window.onload = () => {
    document.getElementById('usuario').focus();
}

document.getElementById('form_iniciar_sesion').addEventListener('submit', e => {
    e.preventDefault();
    iniciar_sesion(e.target);
});