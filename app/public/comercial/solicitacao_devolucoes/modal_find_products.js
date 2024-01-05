
function showForm() {
    var form = document.getElementById('modal');
    form.style.display = 'flex';
}
function closeForm() {
    var form = document.getElementById('modal');
    form.style.display = 'none';
}

function getCheckProduct() {
    // Obtém o elemento de input do tipo radio
    var radioProdutos = document.getElementsByName('produto');
    // Itera sobre os radio buttons para verificar qual está selecionado
    for (var i = 0; i < radioProdutos.length; i++) {
        if (radioProdutos[i].checked) {
            //valor selecionado
            return radioProdutos[i].value;
        }
    }
}

function defineProduct() {
    var produto = getCheckProduct()
    inputIdProduct = document.getElementById('idproduto')
    inputIdProduct.value = parseInt(produto)
    closeForm()
}

function findToLabels() {

    var fild = document.getElementById('fild-find').value
    var valueFind = document.getElementById('value-find').value

    if( valueFind != '') {   
        
        if (fild == '1') {
            produtos = findProductByID(valueFind)
        }

        if (fild == '2') {
            produtos = findProductByName(valueFind)
        }

        if (fild == '3') {
            produtos = findProductByCodigoBarras(valueFind)
        }

        var radioProdutos = document.getElementById('body-table')
        var labels = []

        for (var i = 0; i < produtos.length; i++) {
            labels.push('<tr><td><input type="radio" name="produto" value="' + produtos[i].id + '"></td><td>' + produtos[i].id + '</td><td>' + produtos[i].codigobarras + '</td><td>' + produtos[i].descricao + '</td>')
        }
        radioProdutos.innerHTML = labels.join('')
    }
}

function findProductByName(desc) {

    lista_retorno = lista_produtos
    palavras = desc.toUpperCase().split('%').filter(palavra => palavra != '')

    for (var i = 0; i < palavras.length; i++) {
        lista_retorno = lista_retorno.filter(produto => produto.descricao.includes(palavras[i]))
    }

    return lista_retorno //lista_produtos.filter(function(produto){ return produto.descricao.includes(desc) })
}

function findProductByID(id) {
    id = parseInt(id)
    return lista_produtos.filter(function (produto) { return produto.id == id })
}

function findProductByCodigoBarras(text){
    if (text.length == 13){
        return lista_produtos.filter(produto => produto.codigobarras.includes(text))
    }

    if (text.length < 13){
        return lista_produtos.filter(produto => produto.codigobarras.slice(-text.length).includes(text))
    }

}