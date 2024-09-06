export function select_marcas() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-marcas/').then(res => {
        return res.json(); // Convertir los datos obtenidos a formato JSON y devolver
    }).then(data => { // Capturar los datos convertidos anteriormente
        document.getElementById('id_marca').innerHTML = ''; // Limpiamos el select
        document.getElementById('id_marca').add(new Option('----- Seleccione marca -----', '')); // Agregamos el primer item
        Array.from(data.data, (item, index) => { // Recorrer el listado de marcas
            document.getElementById('id_marca').add(new Option(item.nombre, item.id)); // Y con ello crear un option para el select
        });
    });
}