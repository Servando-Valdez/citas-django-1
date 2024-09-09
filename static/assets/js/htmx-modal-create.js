;(function () {
    const modalCrear = new bootstrap.Modal(document.getElementById('CreateModal'));

    htmx.on("htmx:afterSwap", (e) => {
        console.log("Contenido cargado, mostrando modal.");
        if (e.detail.target.id == "dialogCreate") {
            modalCrear.show()
        }
    })

    htmx.on("htmx:beforeSwap", (e) => {
        // console.log(e.detail.target.id == "dialogEliminar" && !e.detail.xhr.response)
        console.log("Preparando para cerrar modal si la respuesta es 200.");
        if (e.detail.target.id == "dialogCreate" && e.detail.xhr.response == 200) {
            modalCrear.hide()
            e.detail.shouldSwap = false
            console.log("Respuesta 200, recargando página.");
            // if (e.detail.xhr.status == 200){
                window.location.reload();
            // }
        }
    })

    htmx.on("hidden.bs.modal", () => {
        console.log("Modal cerrado, limpiando contenido.");
        document.getElementById("dialogCreate").innerHTML = ""
    })
})();

// document.querySelectorAll('[data-bs-dismiss="modal"]').forEach((btn) => {
//     btn.addEventListener('click', function () {
//         const modalCrear = new bootstrap.Modal(document.getElementById('CreateModal'));
//         modalCrear.hide();
//     });
// });

// ; (function () {
//     const modal = new bootstrap.Modal(document.getElementById("CreateModal"))

//     htmx.on("htmx:afterSwap", (e) => {
//         // Response targeting #dialog => show the modal
//         if (e.detail.target.id == "dialogCreate") {
//             modal.show()
//         }
//     })

//     htmx.on("htmx:beforeSwap", (e) => {
//         // Empty response targeting #dialog => hide the modal
//         if (e.detail.target.id == "dialogCreate" && !e.detail.xhr.response) {
//             modal.hide()
//             e.detail.shouldSwap = false
//         }
//     })

//     // Remove dialog content after hiding
//     htmx.on("hidden.bs.modal", () => {
//         document.getElementById("dialogCreate").innerHTML = ""
//     })
// })()