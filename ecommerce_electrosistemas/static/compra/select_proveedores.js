export function select_proveedores() {
    // Con API fech solicitamos los datos al servidor
    fetch('/compra/listar-proveedores/').then(res => {
        return res.json(); // Convertir los datos obtenidos a formato JSON y devolver
    }).then(data => { // Capturar los datos convertidos anteriormente
        document.getElementById('proveedor').innerHTML = ''; // Limpiamos el select
        //document.getElementById('proveedor').add(new Option('----- Seleccione proveedor -----', '')); // Agregamos el primer item
        
        Array.from(data.data, (item, index) => { // Recorrer el listado de marcas
            document.getElementById('proveedor').add(new Option(`${item.nombres} ${item.apellidos} ${item.empresa}`, item.id)); // Y con ello crear un option para el select
        });
    });
}