export function listar() {
    // Con API fech solicitamos los datos al servidor
    fetch('/compra/listar-compras/').then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        Array.from(data.data, (item, index) => {
            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.proveedor}</td>
                        <td>Q. ${new Intl.NumberFormat('es-MX').format(item.subtotal)}</td>
                        <td>${item.usuario}</td>
                        <td>${item.fecha}</td>
                        <td><i class="bi bi-info-square-fill btn btn-info btn-sm" id="${item.id}"></i></td>
                    </tr>`
        });

        document.getElementById('tabla_compra').childNodes[3].innerHTML = fila;

    });
}