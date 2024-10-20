export function select_categoria() {
    // Con API fech solicitamos los datos al servidor
    fetch('/producto/listar-categorias/').then(res => {
        return res.json();
    }).then(data => {
        let ul = document.getElementById('select_categorias');
        ul.innerHTML = '';

        data.data.forEach((categoria, index, array) => {
            let hr = '<li><hr class="dropdown-divider"></li>';
            let li = `<li><a class="dropdown-item" href="#" id_categoria="${categoria.id}">${categoria.nombre}</a></li>`;

            ul.insertAdjacentHTML('beforeend', li);

            if (index < array.length - 1) {
                ul.insertAdjacentHTML('beforeend', hr)
            }
        });

    });
}