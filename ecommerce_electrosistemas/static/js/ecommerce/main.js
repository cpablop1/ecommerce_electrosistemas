import { listar_productos } from "./listar_productos.js";
import { ver_producto } from "./ver_producto.js";

window.onload = () => {
    listar_productos();
}

document.getElementById('productos').addEventListener('click', e => {
    let producto = parseInt(e.target.getAttribute('producto'));
    if (producto) {
        ver_producto({ 'id': producto });
    }
});

document.getElementById('agregar_carrito').addEventListener('click', e => {
    if (userIsAuthenticated) {
        let id = parseInt(e.target.getAttribute('producto'))
    } else {
        let alert = document.getElementById('no_sesion');
        alert.style.display = 'block';
        setTimeout(() => alert.style.display = 'none', 5000);
    }
});