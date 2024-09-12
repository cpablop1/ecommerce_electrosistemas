export function validacion(formulario){
    let inputs = formulario.querySelectorAll('input[type=date], input[type=number], select');
    
    Array.from(inputs, (value, index) => {
        console.log(value);
    });
}