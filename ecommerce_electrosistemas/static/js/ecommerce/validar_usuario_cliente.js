export function validar_usuario_cliente(form) {

    let input = [];
    let inputs = ['nombres', 'apellidos', 'telefono', 'direccion', 'usuario', 'correo', 'clave'];

    inputs.forEach(campo => {
        if (form.elements[campo].value.trim().length === 0) {
            form.elements[campo].classList.add('is-invalid');
            if (form.elements[campo].nextElementSibling) {
                form.elements[campo].nextElementSibling.style.display = 'block';
            }
            input.push(false);
        } else {
            form.elements[campo].classList.remove('is-invalid');
            if (form.elements[campo].nextElementSibling) {
                form.elements[campo].nextElementSibling.style.display = 'none';
            }
            input.push(true);
        }
    });

    if (form.elements['clave1'].value.trim() !== form.elements['clave'].value.trim()) {
        form.elements['clave1'].classList.add('is-invalid');
        form.elements['clave1'].nextElementSibling.style.display = 'block';
        input.push(false);
    } else {
        form.elements['clave1'].classList.remove('is-invalid');
        form.elements['clave1'].nextElementSibling.style.display = 'none';
        input.push(true);
    }

    return input.every(campo => campo === true);
}