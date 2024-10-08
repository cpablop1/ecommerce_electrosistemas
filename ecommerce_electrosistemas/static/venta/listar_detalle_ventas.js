export function listar_detalle_ventas(modal = false, id = false) {
    // Con API fech solicitamos los datos al servidor
    let url = id ? `/venta/listar-detalle-ventas?id=${id}` : '/venta/listar-detalle-ventas/';

    fetch(url).then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        
        Array.from(data.data, (item, index) => {

            if (modal) {
                fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.producto}</td>
                        <td>${item.cantidad}</td>
                        <td>${item.marca}</td>
                        <td>${item.precio}</td>
                        <td>${item.total}</td>
                    </tr>`
            } else {
                fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.producto}</td>
                        <td>${item.marca}</td>
                        <td class="col-sm-1"><input type="number" class="form-control form-control-sm" id="${item.id_producto}" value="${item.cantidad}"></td>
                        <td>${item.precio}</td>
                        <td>${item.total}</td>
                        <td><i class="bi bi-trash3-fill btn btn-danger btn-sm" dt="${item.id}"></i></td>
                    </tr>`
            }
        });

        if (!modal) {
            document.getElementById('carrito').childNodes[3].innerHTML = fila;
            document.getElementById('carrito').setAttribute('carrito', data.id_venta);
            document.getElementById('subtotal').innerText = `Cobrar Q. ${data.subtotal}`;
            document.getElementById('cliente').value = data.id_cliente;
        } else {
            document.getElementById('tabla_detalle_venta').childNodes[3].innerHTML = fila;
            document.getElementById('detalle_venta_subtotal').innerHTML = `Subtotal: Q. ${new Intl.NumberFormat('es-MX').format(data.subtotal)}`;
        }

    });
}