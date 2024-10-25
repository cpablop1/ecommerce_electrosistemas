import { listar } from "./listar.js";

export function eliminar(id) {

    fetch(`/producto/eliminar-descuento?id=${id}`).then(res => res.json()).then(data => {
        if (data.res) {
            alert(data.msg);
            listar();
        } else {
            alert(data.msg);
        }
    });
}