function delete_service(id){
    Swal.fire({
        "title": "¿Estás seguro?",
        "text": "Esta acción no se puede deshacer",
        "icon": "question",
        "showCancelButton":true,
        "cancelButtonText":"No, cancelar",
        "confirmButtonText":"Sí, eliminar",
        "reverseButtons":true,
        "confirmButtonColor": '#EA0909'
    }).then(function(result){
        if(result.isConfirmed){
            window.location.href="/eliminar/"+id+"/"
        }
    })
}