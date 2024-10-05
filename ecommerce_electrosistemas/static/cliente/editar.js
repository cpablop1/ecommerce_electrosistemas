export function editar(id) {
    let form = document.getElementById('form_cliente');
    form.reset();
    fetch(`/venta/ver-para-editar-cliente?id=${id}`).then(res => res.json()).then(data => {
        document.getElementById('id').value = data.data.id;
        document.getElementById('nombres').value = data.data.nombres;
        document.getElementById('apellidos').value = data.data.apellidos;
        document.getElementById('nit').value = data.data.nit;
        document.getElementById('cui').value = data.data.cui;
        document.getElementById('empresa').value = data.data.empresa;
        document.getElementById('telefono').value = data.data.telefono;
        document.getElementById('direccion').value = data.data.direccion;
        document.getElementById('observaciones').value = data.data.observaciones;

        new bootstrap.Modal(document.getElementById('modal_cliente')).show();
    });
}