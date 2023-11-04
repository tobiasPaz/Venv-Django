const btnBorrar = document.getElementById("btn-borrar");
const csrf_token = document.getElementById("csrf_token");
const idProyecto = document.getElementById("id-proyecto");
const btnVolver = document.getElementById("btn-volver");

function eliminar() {
  console.log("si funciono pero no se porque");
  fetch(`http://localhost:8000/TPs/borrar_proyecto/${idProyecto.textContent}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrf_token.textContent,
      credentials: "same-origin",
    },
  });
}

function volver() {
  window.location.replace("http://localhost:8000/TPs");
}

btnVolver.addEventListener("click", volver);

btnBorrar.addEventListener("click", eliminar);
