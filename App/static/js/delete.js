function delete_service(id){
    Swal.fire({
        title: "¿Estás seguro de eliminar este servicio?",
        text: "Este cambio no se puede revertir!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminarlo!"
      }).then(function(result){
        if(result.isConfirmed){
            window.location.href="/eliminar/"+id+"/"
        }
    });
}