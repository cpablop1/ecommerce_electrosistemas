import { select_categoria } from './select_categoria.js';
import { listar_productos } from './listar_productos.js';

window.addEventListener('load', e => {
    select_categoria();
});

// Evento para buscar productos por categorías
document.getElementById('select_categorias').addEventListener('click', e => {
    let id_categoria = parseInt(e.target.getAttribute('id_categoria'));

    if (id_categoria) {
        listar_productos({'id_categoria': id_categoria});
    }
});

// Evento para buscar productos por nombres
document.getElementById('buscar').addEventListener('keydown', e => {
    let buscar = e.target.value
    
    if (e.keyCode === 13) {
        listar_productos({'buscar': buscar})
    }
})