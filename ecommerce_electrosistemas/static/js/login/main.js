import { iniciarSesion } from "./iniciarSesion.js";


document.getElementById('form_login').addEventListener('submit', e => {
    e.preventDefault();
    iniciarSesion(e.target);
});