export function listar_productos(data) {
    let params = new URLSearchParams(data);
    let productos = '';
    let buscar = ('buscar' in data) ? data.buscar : '';
    let ruta_principal = '/ecommerce/'
    let evaluar_ruta = window.location.pathname;

    // Comprobar si esta en la ruta correcta para listar los productos
    if (ruta_principal !== evaluar_ruta) {
        window.location.href = `${ruta_principal}?${params.toString()}`; // Si no está en la ruta, redireccione a la ruta correcta
        return;
    }

    // Si ya estamos en /ecommerce/, obtenemos los parámetros de la URL
    if (!data || Object.keys(data).length === 0) {
        params = new URLSearchParams(window.location.search);
        let clave_buscar = Object.fromEntries(params.entries());

        buscar = ('buscar' in clave_buscar) ? clave_buscar.buscar : '';

        history.replaceState(null, '', ruta_principal);
    }

    fetch(`/producto/listar-productos?${params.toString()}`).then(data => data.json()).then(data => {

        for (let item of data.data) {
            let img = '';
            if (item.img_1.trim().length === 0) {
                img = `../../static/img/not_found.png`;
            } else {
                img = `../../media/${item.img_1}`;
            }

            productos += `<div class="col">
                                <div class="card m-2" style="width: 18rem;">
                                    <img role="button" src="${img}" class="card-img-top" alt="${item.descripcion}" producto="${item.id}">
                                    <div class="card-body">
                                        <h5 role="button" class="card-title" producto="${item.id}">${item.descripcion}</h5>
                                    </div>
                                    <div class="card-footer">
                                        <div class="row">
                                            <div class="col">
                                                <h5 class="card-title">Q. ${item.precio_publico}</h5>
                                            </div>
                                            <div class="col">
                                                <h5 class="card-title">Existencia: ${item.stock}</h5>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>`;
        }
        document.getElementById('productos').innerHTML = productos;
    }).finally(() => {
        document.getElementById('buscar').value = buscar;
        document.getElementById('buscar').focus();
    });

}