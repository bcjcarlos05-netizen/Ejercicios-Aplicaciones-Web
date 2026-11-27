/* ===== ACORDEÓN (How To W3Schools) ===== */
const acc = document.getElementsByClassName("accordion");

for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        /* Añade o quita la clase "active" para resaltar el botón abierto */
        this.classList.toggle("active");

        /* Muestra u oculta el panel que hay justo debajo del botón */
        const panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}
