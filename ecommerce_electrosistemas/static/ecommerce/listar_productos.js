export function listar_productos() {
    let productos = '';

    for (let item = 0; item > 5; item++) {
        productos += `<div class="col">
                    <div class="card m-2" style="width: 18rem;">
                        <img src="../../media/producto/xno497EtBlxzNgoX586WKLpQ2WasHceCnYFkR3v5.jpg"
                            class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">BOCINA BLUETOOTH VTA+ 2 EN 1 NEGRO</h5>
                        </div>
                        <div class="card-footer">
                            <div class="row">
                                <div class="col">
                                    <h5 class="card-title">Q. 335</h5>
                                </div>
                                <div class="col">
                                    <h5 class="card-title">Existencia: 8</h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`;
    }

    document.getElementById('productos').innerHTML = productos;
}