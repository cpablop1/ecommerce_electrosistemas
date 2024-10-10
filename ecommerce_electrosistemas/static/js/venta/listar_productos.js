export function listar_productos() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-productos/').then(res => {
        return res.json(); // Parseamos los datos obtenidos a formato JSON
    }).then(data => {
        let fila = '';

        Array.from(data.data, (item, index) => {

            fila += `<tr role="button" producto="${item.id}">
                        <td>${index + 1}</td>
                        <td>${item.descripcion}</td>
                        <td>${item.precio_publico}</td>
                        <td>${item.marca}</td>
                        <td>${item.stock}</td>
                    </tr>`
        });

        document.getElementById('tabla_agregar_producto').childNodes[3].innerHTML = fila;

    });
}