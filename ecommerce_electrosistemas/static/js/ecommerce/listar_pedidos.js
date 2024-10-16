window.onload = () => {
    listar_pedidos();
}

export function listar_pedidos() {
    // Con API fech solicitamos los datos al servidor
    fetch('/venta/listar-ventas/').then(res => {
        return res.json();
    }).then(data => {
        let venta = '';
        data.data.forEach(pedido => {
            console.log(pedido);
            venta += `<div class="row p-2 m-2 border border-2 rounded-3">
                        <div class="col">
                            <div class="row">
                                <div class="col-auto p-0 m-0">
                                    <img src="../../static/img/paquete.png" class="img-fluid" style="width: 100px;">
                                </div>
                                <div class="col-auto">
                                    <h3>Pedido #00000${pedido.id}</h3>
                                    <h4>${pedido.fecha}</h4>
                                    <h4 class="alert alert-primary m-0 p-0 text-center">${pedido.seguimiento}</h4>
                                </div>
                            </div>
                        </div>
                        <div class="col d-flex align-items-center justify-content-end">
                            <h2>Q. ${pedido.subtotal}</h2>
                        </div>
                    </div>`;
        });

        document.getElementById('listar_pedidos').innerHTML = venta;
    });
}