export function listar_detalle_compras() {
    // Con API fech solicitamos los datos al servidor
    fetch('/compra/listar-detalle-compras/').then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        Array.from(data.data, (item, index) => {
            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.producto}</td>
                        <td>${item.marca}</td>
                        <td class="col-sm-1"><input type="number" class="form-control form-control-sm" id="${item.id_producto}" value="${item.cantidad}"></td>
                        <td>${item.costo}</td>
                        <td>${item.precio_publico}</td>
                        <td>${item.precio_mayorista}</td>
                        <td>${item.total}</td>
                    </tr>`
        });

        document.getElementById('carrito').childNodes[3].innerHTML = fila;
        document.getElementById('subtotal').innerText = `Cancelar Q. ${data.subtotal}`;
        document.getElementById('proveedor').value = data.id_proveedor;

    });
}