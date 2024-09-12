export function select_productos(){
    fetch('/producto/listar-productos/').then(res => res.json())
    .then(data => {
        let select_producto = document.getElementById('id_producto');
        select_producto.innerHTML = '';

        select_producto.add(new Option('--------- Seleccione producto ---------', ''));
        Array.from(data.data, (value, index) => {
            select_producto.add(new Option(value.descripcion, value.id));
        });

    }).catch(error => {
        console.error(error);
    });
}