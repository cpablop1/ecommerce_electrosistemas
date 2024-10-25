export function listar() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-descuentos/').then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        Array.from(data.data, (item, index) => {
            let estado = 0
            
            if (item.estado) {
                estado = `<span class="btn btn-danger btn-sm"><i class="bi bi-calendar-date-fill"></i></span>`;
            } else {
                estado = `<span class="btn btn-success btn-sm"><i class="bi bi-infinity"></i></span>`;
            }
            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.producto}</td>
                        <td>${item.fecha_inicio}</td>
                        <td>${item.fecha_final}</td>
                        <td>${item.porcentaje}</td>
                        <td>${estado}</td>
                        <td>${item.usuario}</td>
                        <td>${item.fecha_registro}</td>
                        <td><button type="button" class="btn btn-info btn-sm" onclick="editar(${item.id})"><i class="bi bi-pencil-square"></i></button></td>
                        <td><i role="button" class="bi bi-trash3-fill btn btn-danger btn-sm" desc="${item.id}"></i></td>
                    </tr>`
        });
        document.getElementById('tabla_descuento').childNodes[3].innerHTML = fila;

    });
}