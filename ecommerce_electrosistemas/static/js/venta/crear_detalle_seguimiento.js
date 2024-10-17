import { listar } from "./listar.js";

export function crear_detalle_seguimiento(id_seguimiento, id_venta) {
    // Con API fech solicitamos los datos al servidor
    fetch(`/venta/crear-detalle-seguimiento/?id_venta=${id_venta}&id_seguimiento=${id_seguimiento}`).then(res => {
        return res.json();
    }).then(async data => {
        if (data.res) {
            alert(data.msg);
            listar();
        } else {
            alert(data.msg);
        }

    });
}