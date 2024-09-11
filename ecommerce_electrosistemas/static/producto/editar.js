import { select_categorias } from "./select_categorias.js";
import { select_marcas } from "./select_marcas.js";

export function editar(id) {
    let form = document.getElementById('form_producto');
    form.reset();

    document.getElementById('img_1_preview').src = '';
    document.getElementById('img_1_preview').style.display = 'none';

    document.getElementById('img_2_preview').src = '';
    document.getElementById('img_2_preview').style.display = 'none';

    document.getElementById('check_img').style.display = 'none';

    select_categorias();
    select_marcas();

    fetch(`/producto/ver-para-editar-producto?id=${id}`).then(res => res.json()).then(data => {
        console.log(data);
        document.getElementById('id').value = data.data.id;
        document.getElementById('descripcion').value = data.data.descripcion;
        document.getElementById('costo').value = data.data.costo;
        document.getElementById('precio_publico').value = data.data.precio_publico;
        document.getElementById('precio_mayorista').value = data.data.precio_mayorista;

        if (data.data.img_1 && data.data.img_1.trim() !== '') {
            document.getElementById('img_1_preview').style.display = 'block';
            document.getElementById('img_1_preview').src = `../../media/${data.data.img_1}`;
            document.getElementById('check_img').style.display = 'block';
        }

        if (data.data.img_2 && data.data.img_2.trim() !== '') {
            document.getElementById('img_2_preview').style.display = 'block';
            document.getElementById('img_2_preview').src = `../../media/${data.data.img_2}`;
            document.getElementById('check_img').style.display = 'block';
        }

        document.getElementById('estante').value = data.data.estante;
        document.getElementById('id_categoria').value = data.data.id_categoria;
        document.getElementById('id_marca').value = data.data.id_marca;

        new bootstrap.Modal(document.getElementById('modal_producto')).show();
    });
}