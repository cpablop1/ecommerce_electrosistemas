import { listar_detalle_pedido } from "./listar_detalle_pedido.js";
import { listar_detalle_seguimiento } from "./listar_detalle_seguimiento.js";

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
                                    <h6 role="button" class="alert alert-info mt-1 p-0 text-center" venta="${pedido.id}"><i class="bi bi-eye-fill" venta="${pedido.id}"></i> Ver</h6>
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

document.getElementById('listar_pedidos').addEventListener('click', e => {
    let id_venta = parseInt(e.target.getAttribute('venta'));
    if (id_venta) {
        listar_detalle_pedido(id_venta);
        listar_detalle_seguimiento(id_venta);
    }
});