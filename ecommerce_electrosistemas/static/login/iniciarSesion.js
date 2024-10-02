export function iniciarSesion(form) {
    let data = new FormData(form); // Creamos un objeto FormDato para enviarlo a servidor

    fetch('/login/iniciar-sesion/', {
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
            form.reset(); // Limpiamos el formulario
            alert(res.msg);
            location.href = '/';
        } else {
            alert(res.msg); // Caso contrario lanzamos una alerta
        }
    }).catch(error => { // Si la petición tuvo problemas
        console.log(error);
        alert('Hubo un error al inicar sesión.');
    });
}