import { agregar_venta } from "./agregar_venta.js";
import { select_tipo_pago } from "./select_tipo_pago.js";
import { eliminar_venta } from "./eliminar_venta.js";
import { confirmar_venta } from "./confirmar_venta.js";

window.onload = () => {
    carrito();
    select_tipo_pago();
}

// Evento para listar los elementos del carrito
export function carrito() {
    // Con API fech solicitamos los datos al servidor
    let url = '/venta/listar-detalle-ventas/';

    fetch(url).then(res => {
        return res.json();
    }).then(data => {

        let fila = '';
        let img = '';
        if (data.data.length !== 0) {
            document.getElementById('fila_1').hidden = true;
            document.getElementById('fila_2').hidden = false;
            console.log(data);
            data.data.forEach(element => {
                if (element.img.trim().length === 0) {
                    img = '../../static/img/not_found.png';
                } else {
                    img = `../../media/${element.img}`;
                }
                fila += `<tr class="fw-bold">
                            <td><img src="${img}" class="img-fluid"
                                    style="width: 100px;"></td>
                            <td>${element.producto}</td>
                            <td><input type="number" class="form-control form-control-sm text-center" value="${element.cantidad}" id="${element.id_producto}"></td>
                            <td class="col-sm-1 text-nowrap">Q. ${element.precio}</td>
                            <td class="col-sm-1 text-nowrap">Q. ${element.total}</td>
                            <td><i class="bi bi-trash3-fill btn btn-danger btn-sm" dv="${element.id}"></i></td>
                        </tr>`;
            });

            document.getElementById('subtotal_carrito').innerHTML = `Q. ${new Intl.NumberFormat('es-MX').format(data.subtotal)}`;
            document.getElementById('direccion_cliente').innerHTML = data.direccion_cliente;
            document.getElementById('telefono_cliente').innerHTML = data.telefono_cliente;
            document.getElementById('confirmar_pedido').setAttribute('confirmar_pedido', data.id_venta)

            document.getElementById('tabla_carrito').childNodes[3].innerHTML = fila;
        } else {
            document.getElementById('fila_1').hidden = false;
            document.getElementById('fila_2').hidden = true;
        }


    });
}

// Evento para agregar productos al carrito
document.getElementById('tabla_carrito').addEventListener('keydown', e => {
    let producto = parseInt(e.target.id);
    let cantidad = parseInt(e.target.value);

    if (e.keyCode === 13) {
        if (producto) {
            agregar_venta({ 'id_producto': producto, 'cantidad': cantidad });
            setTimeout(() => carrito(), 500);
        }
    }
});

// Evento para eliminar algun elemento del carrito
document.getElementById('tabla_carrito').addEventListener('click', e => {
    let dv = parseInt(e.target.getAttribute('dv'));
    if (dv) {
        eliminar_venta({ 'id_detalle_venta': dv })

        setTimeout(() => carrito(), 500);
    }
});

// Evento para confirmar la venta.
document.getElementById('confirmar_pedido').addEventListener('click', e => {
    console.log(e.target);
    let id_venta = parseInt(e.target.getAttribute('confirmar_pedido'));
    let id_tipo_pago = parseInt(document.getElementById('select_tipo_pago').value);

    if (id_venta) {
        confirmar_venta({ 'id_venta': id_venta,'id_tipo_pago': id_tipo_pago });

        setTimeout(() => carrito(), 500);
    }
});