/* import { agregar } from "./agregar.js";
import { listar } from "./listar.js";
import { editar } from "./editar.js"; */
import { select_marcas } from "./select_marcas.js";
import { select_categorias } from "./select_categorias.js";
import { validacion } from "./validacion.js";

// Al cargar el DOM ejecutar la funcion de listar
window.onload = () => {
    //listar();
}

window.editar = id => {
    editar(id);
}

// Evento para mostrar la ventana modal para crear categorías
document.getElementById('agregar').addEventListener('click', () => {
    new bootstrap.Modal(document.getElementById('modal_producto')).show(); // Instrucción para mostrar la modal
    let form = document.getElementById('form_producto') // Instrucción para obtener el objecto (es decir, el formualario)
    form.reset(); // Limpiamos el formulario obtenido

    setTimeout(() => { // Despues de haber cargado el formulario enfocamos el campo "nombre"
        document.getElementById('descripcion').focus();
        select_marcas();
        select_categorias();
    }, 500);

});

// Evento para limpiar datos y enviarlo al servidor
document.getElementById('form_producto').addEventListener('submit', e => {
    e.preventDefault(); // Anulamos el evento submit del formulario por defecto
    let form_valido = validacion(e.target); // llamamos la función para validar el formulario.
    
    if (form_valido) { // Validamos si el formulario no está vacío
        agregar(e.target); // Y le pasamos por parámetro el formulario
    } else { // Si el formulario es válido llamamos el métedo agregar()
        alert('Complete el formulario para continuar.');
    }
});