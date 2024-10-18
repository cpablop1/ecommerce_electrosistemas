export function listar_detalle_seguimiento(id) {
    // Con API fech solicitamos los datos al servidor

    fetch(`/venta/listar-detalle-seguimiento?id_venta=${id}`).then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        console.log(data);
        Array.from(data.data, (item, index) => {

            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.seguimiento}</td>
                        <td>${item.descripcion}</td>
                        <td>${item.fecha}</td>
                    </tr>`

        });

        document.getElementById('tabla_detalle_seguimiento').childNodes[3].innerHTML = fila;

    });
}