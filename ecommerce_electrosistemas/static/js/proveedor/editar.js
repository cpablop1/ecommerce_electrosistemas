export function editar(id) {
    let form = document.getElementById('form_proveedor');
    form.reset();
    fetch(`/compra/ver-para-editar-proveedor?id=${id}`).then(res => res.json()).then(data => {
        document.getElementById('id').value = data.data.id;
        document.getElementById('nombres').value = data.data.nombres;
        document.getElementById('apellidos').value = data.data.apellidos;
        document.getElementById('nit').value = data.data.nit;
        document.getElementById('dpi').value = data.data.dpi;
        document.getElementById('empresa').value = data.data.empresa;
        document.getElementById('telefono').value = data.data.telefono;
        document.getElementById('direccion').value = data.data.direccion;
        document.getElementById('observaciones').value = data.data.observaciones;

        new bootstrap.Modal(document.getElementById('modal_proveedor')).show();
    });
}