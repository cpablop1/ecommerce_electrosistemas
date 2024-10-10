export function ver_producto(data) {
    let params = new URLSearchParams(data);

    fetch(`/producto/listar-productos?${params.toString()}`).then(data => data.json()).then(data => {
        console.log(data.data[0]);
        document.getElementById('descripcion_producto').innerHTML = data.data[0].descripcion;
        document.getElementById('precio_producto').innerHTML = `Q. ${data.data[0].precio_publico}`;
        document.getElementById('stock_producto').innerHTML = `Existencias: ${data.data[0].stock}`;
        document.getElementById('marca_producto').innerHTML = `Marca: ${data.data[0].marca}`;
        new bootstrap.Modal(document.getElementById('modal_ver_producto')).show(); // Instrucción para mostrar la modal

    });
}