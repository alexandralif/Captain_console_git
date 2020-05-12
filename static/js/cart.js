console.log("Hello world")
var updatebtns = document.getElementsByClassName('add_to_cart')

for (var i=0; i<updatebtns.length; i++) {
    updatebtns[i].addEventListener('click', function () {
        var product = this.dataset.product
        var action = this.dataset.action
        console.log('product_id:', product, 'action:', action  )

    })
}

//function add_to_cart(id){
//    $.ajax({
//        url: '/cart/add_to_cart',
//        type: 'POST',
//        method: 'POST',
//        data: {product_id: id},
//        success: function (resp) {
//            $("#cart_item").html(resp.numberOfItems)
//            console.log("yay")
//            confirm("Vöru hefur verið bætt við í körfuna")
//        },
//        error: function (xhr, status, error) {
//            // TODO: Show toastr
//            alert("Þú ert ekki innskráð/ur. Vinsamlegast skráðu þig inn til þess að setja vörur í körfuna")
//            console.error(error)
//        }
//    });
//}