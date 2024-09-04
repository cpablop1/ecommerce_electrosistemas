export function select_marcas() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-marcas/').then(res => {
        return res.json();
    }).then(data => {
        let fila = '';
        document.getElementById('id_marca').innerHTML = '';
        document.getElementById('id_marca').add(new Option('----- Seleccione marca -----', ''));
        Array.from(data.data, (item, index) => {
            document.getElementById('id_marca').add(new Option(item.nombre, item.id));
        });

    });
}