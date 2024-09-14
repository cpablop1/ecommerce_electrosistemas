export function listar() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-categorias/').then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        Array.from(data.data, (item, index) => {
            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${item.nombre}</td>
                        <td>${item.descripcion}</td>
                        <td><button type="button" class="btn btn-info btn-sm" onclick="editar(${item.id})"><i class="bi bi-pencil-square"></i></button></td>
                    </tr>`
        });
        document.getElementById('tabla_categoria').childNodes[3].innerHTML = fila;

    });
}