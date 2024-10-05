export function select_clientes() {
    // Con API fech solicitamos los datos al servidor
    fetch('/venta/listar-clientes/').then(res => {
        return res.json(); // Convertir los datos obtenidos a formato JSON y devolver
    }).then(data => { // Capturar los datos convertidos anteriormente
        document.getElementById('cliente').innerHTML = ''; // Limpiamos el select
        
        Array.from(data.data, (item, index) => { // Recorrer el listado de marcas
            document.getElementById('cliente').add(new Option(`${item.nombres} ${item.apellidos} ${item.empresa}`, item.id)); // Y con ello crear un option para el select
        });
    });
}