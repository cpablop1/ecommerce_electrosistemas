import { select_productos } from "./select_productos.js";

export function editar(id) {
    let form = document.getElementById('form_descuento');
    form.reset();

    select_productos();

    fetch(`/producto/ver-para-editar-descuento?id=${id}`).then(res => res.json()).then(data => {

        document.getElementById('id').value = data.data.id;
        document.getElementById('fecha_inicio').value = data.data.fecha_inicio;
        document.getElementById('fecha_final').value = data.data.fecha_final;
        document.getElementById('porcentaje').value = data.data.porcentaje;
        setTimeout(() => {
            document.getElementById('id_producto').value = data.data.id_producto;
        }, 500);

        new bootstrap.Modal(document.getElementById('modal_descuento')).show();
    });
}