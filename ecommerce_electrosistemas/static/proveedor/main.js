import { agregar } from "./agregar.js";
/* import { listar } from "./listar.js"; */
/* import { editar } from "./editar.js"; */
import { validacion } from "./validacion.js";

// Al cargar el DOM ejecutar la funcion de listar
window.onload = () => {
    //listar();
}

window.editar = id => {
    //editar(id);
}

// Evento para mostrar la ventana modal para crear categorías
document.getElementById('agregar').addEventListener('click', () => {
    new bootstrap.Modal(document.getElementById('modal_proveedor')).show(); // Instrucción para mostrar la modal
    let form = document.getElementById('form_proveedor') // Instrucción para obtener el objecto (es decir, el formualario)
    form.reset(); // Limpiamos el formulario obtenido

    setTimeout(() => { // Despues de haber cargado el formulario enfocamos el campo "nombre"
        document.getElementById('nombres').focus();
    }, 500);

});

// Evento para limpiar datos y enviarlo al servidor
document.getElementById('form_proveedor').addEventListener('submit', e => {
    e.preventDefault(); // Anulamos el evento submit del formulario por defecto
    let valido = validacion(e.target);
    
    if (valido) { 
        agregar(e.target);
    } else { 
        alert('Complete el formulario para continuar.');
    }
});