export function listar() {
    // Con API fech solicitamos los datos al servidor
    fetch('/venta/listar-ventas/').then(res => {
        return res.json();
    }).then(async data => {
        let fila = '';
        const seguimientos = await fetch('/venta/listar-seguimientos/').then(res => res.json()).then(data => data);


        Array.from(data.data, (item, index) => {
            const select = document.createElement('select');
            select.classList.add('form-select', 'form-select-sm');

            Array.from(seguimientos.data, seg => {
                let option = new Option(seg.nombre, seg.id);

                if (seg.id === item.id_seguimiento) {
                    option.setAttribute('selected', 'selected');
                }

                select.add(option);
            });
            select.setAttribute('id_venta', item.id)

            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.cliente}</td>
                        <td>Q. ${new Intl.NumberFormat('es-MX').format(item.subtotal)}</td>
                        <td>${select.outerHTML}</td>
                        <td>${item.estado}</td>
                        <td>${item.tipo_pago}</td>
                        <td>${item.usuario}</td>
                        <td>${item.fecha}</td>
                        <td><i class="bi bi-info-square-fill btn btn-info btn-sm" id="${item.id}"></i></td>
                    </tr>`
        });

        document.getElementById('tabla_venta').childNodes[3].innerHTML = fila;

    });
}