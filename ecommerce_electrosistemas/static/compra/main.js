/* import { listar } from "./listar.js"; */
/* import { editar } from "./editar.js"; */
import { agregar } from "./agregar.js";
import { listar_productos } from "./listar_productos.js";
import { select_proveedores } from "./select_proveedores.js";
import { listar_detalle_compras } from "./listar_detalle_compras.js";

// Al cargar el DOM ejecutar la funcion de listar
window.onload = () => {
    //listar();
}

window.editar = id => {
    //editar(id);
}

// Evento para mostrar la ventana modal para crear categorías
document.getElementById('agregar').addEventListener('click', () => {
    new bootstrap.Modal(document.getElementById('modal_compra')).show(); // Instrucción para mostrar la modal
    
    setTimeout(select_proveedores(), 500);

    setTimeout(listar_detalle_compras(), 1000);
    
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