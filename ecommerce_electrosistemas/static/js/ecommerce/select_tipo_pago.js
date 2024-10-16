export function select_tipo_pago() {
    fetch(`/venta/listar-tipo-pagos/`).then(data => data.json()).then(data => {
        let select = document.getElementById('select_tipo_pago');
        select.innerHTML = '';

        for (let tipo_pago of data.data) {
            select.add(new Option(tipo_pago.nombre, tipo_pago.id))
        }
    });

}