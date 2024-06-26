function confimarEliminar(id) {
    Swal.fire({
        title: "Estás Seguro?",
        text: "Esto no se puede revertir!",
        icon: "error",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, elimina"
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire({

            title: "Eliminado!",
            text: "Eliminado correctamente.",
            icon: "success"
          }).then(function() {
            window.location.href = "delete/" + id + "/";
          });
        }
      });
}
