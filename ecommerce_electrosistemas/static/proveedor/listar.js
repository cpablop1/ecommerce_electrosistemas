export function listar() {
    // Con API fech solicitamos los datos al servidor
    fetch('/compra/listar-proveedores/').then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        Array.from(data.data, (item, index) => {
            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.nombres}</td>
                        <td>${item.apellidos}</td>
                        <td>${item.nit}</td>
                        <td>${item.dpi}</td>
                        <td>${item.empresa}</td>
                        <td>${item.telefono}</td>
                        <td>${item.direccion}</td>
                        <td>${item.observaciones}</td>
                        <td>${item.usuario}</td>
                        <td>${item.fecha_registro}</td>
                        <td><button type="button" class="btn btn-info btn-sm" onclick="editar(${item.id})"><i class="bi bi-pencil-square"></i></button></td>
                    </tr>`
        });
        document.getElementById('tabla_proveedor').childNodes[3].innerHTML = fila;

    });
}