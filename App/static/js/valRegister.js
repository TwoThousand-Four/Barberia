// validar que los campos esten llenos -- no te deja avanzar si el campo esta vacio
(function() {
    'use strict';
    window.addEventListener('load', function() {
      // Obtener los formularios a los que queremos agregar estilos de validación
        var forms = document.getElementsByClassName('needs-validation');
      // Bucle 
        var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
            if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
            }
        form.classList.add('was-validated');
        }, false);
    });
    }, false);
})();