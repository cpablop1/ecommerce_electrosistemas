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
    let form = document.getElementById('form_compra') // Instrucción para obtener el objecto (es decir, el formualario)
    form.reset(); // Limpiamos el formulario obtenido
    listar_detalle_compras();
    setTimeout(select_proveedores(), 500);
});

// Evento para mostrar la modal de agregar productos al carrito
document.getElementById('agregar_producto').addEventListener('click', e => {
    new bootstrap.Modal(document.getElementById('modal_agregar_producto')).show();
    listar_productos();
});

// Evento para saber a que fila el usurio dio click para agregar el producto en el carrito
document.getElementById('tabla_agregar_producto').addEventListener('click', e => {
    let producto = e.target.parentNode.getAttribute('producto');
    let proveedor = document.getElementById('proveedor');
    if(producto){
        agregar({'id_producto': producto, 'id_proveedor': proveedor.value, 'cantidad': 1});
    }
});

// Evento para limpiar datos y enviarlo al servidor
document.getElementById('form_compra').addEventListener('submit', e => {
    e.preventDefault(); // Anulamos el evento submit del formulario por defecto
    let nombre = document.getElementById('nombre') // Otenemos el campo nombre
    if (nombre.value.trim().length === 0) { // Validamos si el formulario no está vacío
        alert('El campo nombre es obligatorio.');
        setTimeout(() => nombre.focus(), 500);
        nombre.classList.add('is-invalid');
    } else { // Si el formulario es válido llamamos el métedo agregar()
        agregar(e.target); // Y le pasamos por parámetro el formulario
        nombre.classList.remove('is-invalid');
    }
});