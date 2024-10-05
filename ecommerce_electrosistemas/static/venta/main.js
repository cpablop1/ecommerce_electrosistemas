/* import { listar } from "./listar.js"; */
/* import { editar } from "./editar.js"; */
/* import { agregar } from "./agregar.js"; */
import { listar_productos } from "./listar_productos.js";
import { select_clientes } from "./select_clientes.js";
/* import { listar_detalle_compras } from "./listar_detalle_compras.js"; */
/* import { confirmar_compra } from "./confirmar_compra.js"; */
/* import { eliminar_compra } from "./eliminar_compra.js"; */

// Al cargar el DOM ejecutar la funcion de listar
window.onload = () => {
    //listar();
}

window.editar = id => {
    //editar(id);
}

// Evento para mostrar la ventana modal para agregar venta
document.getElementById('agregar').addEventListener('click', () => {
    new bootstrap.Modal(document.getElementById('modal_venta')).show(); // Instrucción para mostrar la modal

    setTimeout(select_clientes(), 500);

    //setTimeout(listar_detalle_compras(), 1000);

});

// Evento para mostrar la modal de agregar productos al carrito
document.getElementById('agregar_producto').addEventListener('click', e => {
    new bootstrap.Modal(document.getElementById('modal_agregar_producto')).show();
    listar_productos()
});

// Evento para saber a que fila el usurio dio click para agregar el producto en el carrito
document.getElementById('tabla_agregar_producto').addEventListener('click', e => {
    let producto = e.target.parentNode.getAttribute('producto');
    let proveedor = document.getElementById('proveedor');
    if (producto) {
        agregar({ 'id_producto': producto, 'id_proveedor': proveedor.value });
    }
});

// Evento para limpiar datos y enviarlo al servidor
document.getElementById('carrito').addEventListener('keydown', e => {
    let id_producto = e.target.id;
    let cantidad = e.target.value;
    let proveedor = document.getElementById('proveedor').value;

    if (e.keyCode === 13) {
        if (id_producto) {
            agregar({ 'id_producto': id_producto, 'id_proveedor': proveedor, 'cantidad': cantidad });
        }
    }
})

// Evento para confirmar la compra
/* document.getElementById('confirmar_compra').addEventListener('click', e => {
    let tabla = document.getElementById('carrito');
    let id_compra = tabla.getAttribute('carrito');
    confirmar_compra({ 'id_compra': id_compra });
}); */

// Evento para borrar elementos en el carrito
document.getElementById('carrito').addEventListener('click', e => {
    let id = parseInt(e.target.getAttribute('dt'));
    if (id) {
        console.log(id);
        eliminar_compra({ 'id_detalle_compra': id })
    }
});

// Evento para borrar la compra completa
document.getElementById('vaciar').addEventListener('click', e => {
    let tabla = document.getElementById('carrito');
    let id_compra = parseInt(tabla.getAttribute('carrito'));

    if (id_compra) {
        eliminar_compra({ 'id_compra': id_compra });
    }
});

// Evento para para ver detalle de la compra
document.getElementById('tabla_compra').addEventListener('click', e => {
    let id = parseInt(e.target.id)
    if (id) {
        listar_detalle_compras(true, id)
        new bootstrap.Modal(document.getElementById('modal_detalle_compra')).show();
    }
});