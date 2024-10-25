import { agregar } from "./agregar.js";
import { listar } from "./listar.js";
import { editar } from "./editar.js";
import { select_productos } from "./select_productos.js";
import { validacion } from "./validacion.js";
import { eliminar } from "./eliminar.js";

// Al cargar el DOM ejecutar la funcion de listar
window.onload = () => {
    listar();
}

window.editar = id => {
    editar(id);
}

// Evento para mostrar la ventana modal para crear categorías
document.getElementById('agregar').addEventListener('click', () => {
    new bootstrap.Modal(document.getElementById('modal_descuento')).show(); // Instrucción para mostrar la modal
    let form = document.getElementById('form_descuento') // Instrucción para obtener el objecto (es decir, el formualario)
    form.reset(); // Limpiamos el formulario obtenido
    select_productos();
});

// Evento para limpiar datos y enviarlo al servidor
document.getElementById('form_descuento').addEventListener('submit', e => {
    e.preventDefault(); // Anulamos el evento submit del formulario por defecto

    let validar = validacion(e.target);
    
    if(validar) {
        agregar(e.target);
    }
});

// Evento para eliminar descuento
document.getElementById('tabla_descuento').addEventListener('click', e => {
    let id = parseInt(e.target.getAttribute('desc'))

    if (id) {
        eliminar(id);
    }
});