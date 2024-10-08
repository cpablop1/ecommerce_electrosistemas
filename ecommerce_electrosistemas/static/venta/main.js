import { listar } from "./listar.js";
import { agregar } from "./agregar.js";
import { listar_productos } from "./listar_productos.js";
import { select_clientes } from "./select_clientes.js";
import { listar_detalle_ventas } from "./listar_detalle_ventas.js";
import { confirmar_venta } from "./confirmar_venta.js";
import { eliminar_venta } from "./eliminar_venta.js";

// Al cargar el DOM ejecutar la funcion de listar
window.onload = () => {
    listar();
}

// Evento para mostrar la ventana modal para agregar venta
document.getElementById('agregar').addEventListener('click', () => {
    new bootstrap.Modal(document.getElementById('modal_venta')).show(); // Instrucción para mostrar la modal

    setTimeout(select_clientes(), 500);

    setTimeout(listar_detalle_ventas(), 1000);

});

// Evento para mostrar la modal de agregar productos al carrito
document.getElementById('agregar_producto').addEventListener('click', e => {
    new bootstrap.Modal(document.getElementById('modal_agregar_producto')).show();
    listar_productos()
});

// Evento para saber a que fila el usurio dio click para agregar el producto en el carrito
document.getElementById('tabla_agregar_producto').addEventListener('click', e => {
    let producto = e.target.parentNode.getAttribute('producto');
    let cliente = document.getElementById('cliente');
    if (producto) {
        agregar({ 'id_producto': producto, 'id_cliente': cliente.value });
    }
});

// Evento para limpiar datos y enviarlo al servidor, actualizar la cantidad del producto
document.getElementById('carrito').addEventListener('keydown', e => {
    let id_producto = e.target.id;
    let cantidad = e.target.value;
    let cliente = document.getElementById('cliente').value;

    if (e.keyCode === 13) {
        if (id_producto) {
            agregar({ 'id_producto': id_producto, 'id_cliente': cliente, 'cantidad': cantidad });
        }
    }
})

// Evento para confirmar la venta
document.getElementById('confirmar_venta').addEventListener('click', e => {
    let tabla = document.getElementById('carrito');
    let id_venta = tabla.getAttribute('carrito');
    confirmar_venta({ 'id_venta': id_venta });
});

// Evento para borrar elementos en el carrito
document.getElementById('carrito').addEventListener('click', e => {
    let id = parseInt(e.target.getAttribute('dt'));
    if (id) {
        eliminar_venta({ 'id_detalle_venta': id })
    }
});

// Evento para borrar la venta completa
document.getElementById('vaciar').addEventListener('click', e => {
    let tabla = document.getElementById('carrito');
    let id_venta = parseInt(tabla.getAttribute('carrito'));

    if (id_venta) {
        eliminar_venta({ 'id_venta': id_venta });
    }
});

// Evento para para ver detalle de la compra
document.getElementById('tabla_venta').addEventListener('click', e => {
    let id = parseInt(e.target.id)
    if (id) {
        listar_detalle_ventas(true, id)
        new bootstrap.Modal(document.getElementById('modal_detalle_venta')).show();
    }
});