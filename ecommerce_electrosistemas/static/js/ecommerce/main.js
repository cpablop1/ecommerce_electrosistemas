import { listar_productos } from "./listar_productos.js";
import { ver_producto } from "./ver_producto.js";
import { agregar_venta } from "./agregar_venta.js";

window.onload = () => {
    listar_productos({});
}

// Evento para ver un producto específico
document.getElementById('productos').addEventListener('click', e => {
    let producto = parseInt(e.target.getAttribute('producto'));
    if (producto) {
        ver_producto({ 'id': producto });
    }
});

// Evento para agregar producto al carrito
document.getElementById('agregar_carrito').addEventListener('click', e => {
    if (userIsAuthenticated) {
        let producto = parseInt(e.target.getAttribute('producto'));
        console.log(producto);
        agregar_venta({ 'id_producto': producto });
    } else {
        let alert = document.getElementById('no_sesion');
        alert.style.display = 'block';
        setTimeout(() => alert.style.display = 'none', 5000);
    }
});