import { listar_productos } from "./listar_productos.js";
import { ver_producto } from "./ver_producto.js";

window.onload = () => {
    listar_productos();
}

document.getElementById('productos').addEventListener('click', e => {
    let producto = parseInt(e.target.getAttribute('producto'));
    if (producto) {
        ver_producto({'id': producto});
    }
});