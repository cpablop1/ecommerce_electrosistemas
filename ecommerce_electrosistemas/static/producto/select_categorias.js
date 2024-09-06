export function select_categorias() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-categorias/').then(res => {
        return res.json(); // Convertir los datos obtenidos a formato JSON y devolver
    }).then(data => { // Capturar los datos convertidos anteriormente
        document.getElementById('id_categoria').innerHTML = ''; // Limpiamos el select
        document.getElementById('id_categoria').add(new Option('----- Seleccione categoría -----', '')); // Agregamos el primer item
        Array.from(data.data, (item, index) => { // Recorrer el listado de marcas
            document.getElementById('id_categoria').add(new Option(item.nombre, item.id)); // Y con ello crear un option para el select
        });
    });
}