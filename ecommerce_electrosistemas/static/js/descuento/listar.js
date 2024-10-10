export function listar() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-descuentos/').then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        Array.from(data.data, (item, index) => {
            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.producto}</td>
                        <td>${item.fecha_inicio}</td>
                        <td>${item.fecha_final}</td>
                        <td>${item.porcentaje}</td>
                        <td>${item.usuario}</td>
                        <td>${item.fecha_registro}</td>
                        <td><button type="button" class="btn btn-info btn-sm" onclick="editar(${item.id})"><i class="bi bi-pencil-square"></i></button></td>
                    </tr>`
        });
        document.getElementById('tabla_descuento').childNodes[3].innerHTML = fila;

    });
}