export function validacion(form) {
    let descripcion = form.elements['descripcion'];
    let categoria = form.elements['id_categoria'];
    let marca = form.elements['id_marca'];

    if (descripcion.value.trim().length === 0) {
        descripcion.classList.add('is-invalid');
        descripcion.focus();
        descripcion = false;
    } else {
        descripcion.classList.remove('is-invalid');
        descripcion = true;
    }

    if (categoria.value.trim().length === 0) {
        categoria.classList.add('is-invalid');
        categoria = false;
    } else {
        categoria.classList.remove('is-invalid');
        categoria = true
    }

    if (marca.value.trim().length === 0) {
        marca.classList.add('is-invalid');
        marca = false;
    } else {
        marca.classList.remove('is-invalid');
        marca = true;
    }

    return descripcion & categoria & marca;
}