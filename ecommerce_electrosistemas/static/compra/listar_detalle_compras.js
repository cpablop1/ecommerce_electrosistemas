export function listar_detalle_compras() {
    // Con API fech solicitamos los datos al servidor
    fetch('/compra/listar-detalle-compras/').then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        console.log(data.data);
        Array.from(data.data, (item, index) => {
            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.id_producto}</td>
                        <td>${item.marca}</td>
                        <td>${item.cantidad}</td>
                        <td>${item.costo}</td>
                        <td>${item.precio_publico}</td>
                        <td>${item.precio_mayorista}</td>
                        <td>${item.total}</td>
                    </tr>`
        });
        document.getElementById('carrito').childNodes[3].innerHTML = fila;

    });
}