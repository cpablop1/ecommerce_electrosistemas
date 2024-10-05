export function validacion(formulario) {
    let nombres = formulario.elements['nombres'];
    let apellidos = formulario.elements['apellidos'];
    let telefono = formulario.elements['telefono'];

    if (nombres.value.trim().length === 0) {
        nombres.classList.add('is-invalid');
        nombres = false;
    } else {
        nombres.classList.remove('is-invalid');
        nombres = true;
    }

    if (apellidos.value.trim().length === 0) {
        apellidos.classList.add('is-invalid');
        apellidos = false;
    } else {
        apellidos.classList.remove('is-invalid');
        apellidos = true;
    }

    if (telefono.value.trim().length === 0) {
        telefono.classList.add('is-invalid');
        telefono = false;
    } else {
        telefono.classList.remove('is-invalid');
        telefono = true;
    }

    return nombres & apellidos & telefono;
}