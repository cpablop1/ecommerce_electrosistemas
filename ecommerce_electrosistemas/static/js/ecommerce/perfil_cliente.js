window.onload = () => {
    perfil_cliente();
}

export function perfil_cliente() {
    // Con API fech solicitamos los datos al servidor
    fetch('/ecommerce/perfil-cliente/').then(res => {
        return res.json();
    }).then(data => {
        document.getElementById('nombres').innerHTML = `${data.data[0].nombres} ${data.data[0].apellidos}`;
        document.getElementById('nit').innerHTML = data.data[0].nit;
        document.getElementById('cui').innerHTML = data.data[0].cui;
        document.getElementById('empresa').innerHTML = data.data[0].empresa;
        document.getElementById('telefono').innerHTML = data.data[0].telefono;
        document.getElementById('direccion').innerHTML = data.data[0].direccion;
        document.getElementById('fecha').innerHTML = data.data[0].fecha_registro;
        document.getElementById('editar_perfil').setAttribute('cliente', data.data[0].id);
    });
}

// Evento para invocar actualización de perfil del usuario
document.getElementById('editar_perfil').addEventListener('click', e => {
    let id = parseInt(e.target.getAttribute('cliente'));
    if (id) {
        window.location.href = `/ecommerce/crear-usuario?id=${id}`;
    }
});