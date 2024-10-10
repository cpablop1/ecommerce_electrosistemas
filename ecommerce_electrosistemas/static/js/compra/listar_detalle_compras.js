export function listar_detalle_compras(modal = false, id = false) {
    // Con API fech solicitamos los datos al servidor
    let url = id ? `/compra/listar-detalle-compras?id=${id}` : '/compra/listar-detalle-compras/';

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
                        <td>${item.costo}</td>
                        <td>${item.total}</td>
                    </tr>`
            } else {
                fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.producto}</td>
                        <td>${item.marca}</td>
                        <td class="col-sm-1"><input type="number" class="form-control form-control-sm" id="${item.id_producto}" value="${item.cantidad}"></td>
                        <td>${item.costo}</td>
                        <td>${item.precio_publico}</td>
                        <td>${item.precio_mayorista}</td>
                        <td>${item.total}</td>
                        <td><i class="bi bi-trash3-fill btn btn-danger btn-sm" dt="${item.id}"></i></td>
                    </tr>`
            }
        });

        if (!modal) {
            document.getElementById('carrito').childNodes[3].innerHTML = fila;
            document.getElementById('carrito').setAttribute('carrito', data.id_compra);
            document.getElementById('subtotal').innerText = `Cancelar Q. ${data.subtotal}`;
            document.getElementById('proveedor').value = data.id_proveedor;
        } else {
            document.getElementById('tabla_detalle_compra').childNodes[3].innerHTML = fila;
            document.getElementById('detalle_compra_subtotal').innerHTML = `Subtotal: Q. ${new Intl.NumberFormat('es-MX').format(data.subtotal)}`;
        }


    });
}