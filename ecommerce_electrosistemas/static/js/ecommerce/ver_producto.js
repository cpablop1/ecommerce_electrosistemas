export function ver_producto(data) {
    let params = new URLSearchParams(data);

    fetch(`/producto/listar-productos?${params.toString()}`).then(data => data.json()).then(data => {

        let img = '';
        let indicador = `<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="bg-primary active" aria-current="true" aria-label="Slide 1"></button>`;
        document.getElementById('descripcion_producto').innerHTML = data.data[0].descripcion;
        document.getElementById('precio_producto').innerHTML = `Q. ${data.data[0].precio_publico}`;
        document.getElementById('stock_producto').innerHTML = `Existencias: ${data.data[0].stock}`;
        document.getElementById('marca_producto').innerHTML = `Marca: ${data.data[0].marca}`;

        if (data.data[0].img_1.trim().length != 0) {
            img += `<div class="carousel-item active">
                        <img src="./../media/${data.data[0].img_1}" class="d-block mx-auto" alt="..." style="width: 400px; height: auto;">
                    </div>`;
        } else {
            img += `<div class="carousel-item active">
                        <img src="./../static/img/not_found.png" class="d-block mx-auto" alt="..." style="width: 500px; height: auto;">
                    </div>`;
        }

        if (data.data[0].img_2.trim().length != 0) {
            img += `<div class="carousel-item">
                        <img src="./../media/${data.data[0].img_2}" class="d-block mx-auto" alt="..." style="width: 400px; height: auto;">
                    </div>`;
            indicador += `<button class="bg-primary" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>`;
        }

        document.getElementById('indicador_producto').innerHTML = indicador;
        document.getElementById('img_producto').innerHTML = img;
        document.getElementById('agregar_carrito').setAttribute('producto', data.data[0].id);

        new bootstrap.Modal(document.getElementById('modal_ver_producto')).show(); // Instrucción para mostrar la modal

    });
}