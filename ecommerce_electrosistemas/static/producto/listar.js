export function listar() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-productos/').then(res => {
        return res.json(); // Parseamos los datos obtenidos a formato JSON
    }).then(data => {
        let fila = '';

        Array.from(data.data, (item, index) => {
            let img = '';
            
            if (item.img_1 && item.img_1.trim() !== '') {
                img = `<img src="../../media/${item.img_1}" alt="" width="50"></img>`
            }

            fila += `<tr>
                        <td>${index + 1}</td>
                        <td>${img}</td>
                        <td>${item.descripcion}</td>
                        <td>${item.costo}</td>
                        <td>${item.precio_publico}</td>
                        <td>${item.precio_mayorista}</td>
                        <td>${item.estante}</td>
                        <td>${item.marca}</td>
                        <td>${item.categoria}</td>
                        <td>${item.stock}</td>
                        <td>${item.usuario}</td>
                        <td>${item.fecha_registro}</td>
                        <td><button type="button" class="btn btn-info btn-sm" onclick="editar(${item.id})"><i class="bi bi-pencil-square"></i></button></td>
                    </tr>`
        });

        document.getElementById('tabla_producto').childNodes[3].innerHTML = fila;
        
    });
}