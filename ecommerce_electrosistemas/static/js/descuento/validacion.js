export function validacion(formulario) {
    let inputs = formulario.querySelectorAll('input[type=date], input[type=number], select');
    let valid = [];

    Array.from(inputs, (value, index) => {
        if (value.value.trim().length === 0) {
            value.classList.add('is-invalid');
            valid.push(false);
        } else {
            value.classList.remove('is-invalid');
            valid.push(true);
        }
    });

    return valid.every(item => item === true);
}