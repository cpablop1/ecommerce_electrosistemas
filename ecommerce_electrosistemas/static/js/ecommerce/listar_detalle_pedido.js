export function listar_detalle_pedido(id) {
    // Con API fech solicitamos los datos al servidor

    fetch(`/venta/listar-detalle-ventas?id=${id}`).then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        Array.from(data.data, (item, index) => {

            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.producto}</td>
                        <td>${item.cantidad}</td>
                        <td>${item.marca}</td>
                        <td>${item.precio}</td>
                        <td>${item.total}</td>
                    </tr>`

        });


        document.getElementById('tabla_detalle_pedido').childNodes[3].innerHTML = fila;
        document.getElementById('detalle_pedido_subtotal').innerText = `Cobrar Q. ${data.subtotal}`;

        new bootstrap.Modal(document.getElementById('modal_detalle_pedido')).show();

    });
}