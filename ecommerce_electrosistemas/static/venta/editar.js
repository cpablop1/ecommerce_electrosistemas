export function editar(id) {
    let form = document.getElementById('form_categoria');
    form.reset();
    fetch(`/producto/ver-para-editar-categoria?id=${id}`).then(res => res.json()).then(data => {
        document.getElementById('nombre').value = data.data.nombre;
        document.getElementById('id').value = data.data.id;
        document.getElementById('descripcion').value = data.data.descripcion;

        new bootstrap.Modal(document.getElementById('modal_categoria')).show();
    });
}