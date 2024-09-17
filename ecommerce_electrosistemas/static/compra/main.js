/* import { agregar } from "./agregar.js"; */
/* import { listar } from "./listar.js"; */
/* import { editar } from "./editar.js"; */

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