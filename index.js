import "./styles.css";
import $ from "jQuery";

// Environment Indicators
let last_id = undefined;
let last_fecha = undefined;
let last_hora = undefined;

// Interactive Elements
const button_submit = document.getElementById("button-submit");
const button_update = document.getElementById("button-update");

// Medical Record Elements
const id_input = document.getElementById("id");
const historial = document.getElementById("historial");
const last_update = document.getElementById("last_mod");
const name_input = document.getElementById("name_input");
const algs_input = document.getElementById("alergias_input");
const enfs_input = document.getElementById("enfs_input");
const meds_input = document.getElementById("meds_input");
const cirs_input = document.getElementById("cirugias_input");
const othr_input = document.getElementById("otros_input");
const treats_input = document.getElementById("tratamientos_input");
const probs_input = document.getElementById("problemas_input");
const obsv_input = document.getElementById("observaciones_input");

// Auxiliar functions
function list_to_string(list) {
  let final = "";

  for (let i = 0; i < list.length; i++) {
    final += list[i];
    if (i !== list.length - 1) {
      final += "\n";
    }
  }

  return final;
}

function string_to_list(string) {
  let final = [];
  let splitted = string.split("\n");

  for (let i = 0; i < splitted.length; i++) {
    final.push(splitted[i]);
  }

  return final;
}

function anyEmpty() {
  let empty = false;

  if (!/[a-zA-Z]/.test(name_input.value)) {
    empty = true;
  } else if (!/[a-zA-Z]/.test(algs_input.value)) {
    empty = true;
  } else if (!/[a-zA-Z]/.test(enfs_input.value)) {
    empty = true;
  } else if (!/[a-zA-Z]/.test(meds_input.value)) {
    empty = true;
  } else if (!/[a-zA-Z]/.test(cirs_input.value)) {
    empty = true;
  } else if (!/[a-zA-Z]/.test(othr_input.value)) {
    empty = true;
  } else if (!/[a-zA-Z]/.test(treats_input.value)) {
    empty = true;
  } else if (!/[a-zA-Z]/.test(probs_input.value)) {
    empty = true;
  } else if (!/[a-zA-Z]/.test(obsv_input.value)) {
    empty = true;
  }

  return empty;
}

function fill_values(parsed) {
  last_update.textContent = `Última modificación: ${parsed["fecha"]} ${parsed["hora"]}`;
  name_input.value = parsed["nombre"];
  algs_input.value = list_to_string(parsed["alergias"]);
  enfs_input.value = list_to_string(parsed["enfermedades"]);
  meds_input.value = list_to_string(parsed["medicamentos"]);
  cirs_input.value = list_to_string(parsed["cirugias"]);
  othr_input.value = list_to_string(parsed["otros"]);
  treats_input.value = list_to_string(parsed["tratamientos"]);
  probs_input.value = list_to_string(parsed["problemas"]);
  obsv_input.value = list_to_string(parsed["observaciones"]);
  last_fecha = parsed["fecha"];
  last_hora = parsed["hora"];
}

function getHistorial(id) {
  $.ajax({
    type: "GET",
    contentType: "jsonp",
    url: "http://192.168.131.39:5000/historial/" + id,
    crossDomain: true,

    statusCode: {
      200: function (response) {
        const parsed = JSON.parse(response);
        fill_values(parsed);
      },
      400: function (response) {
        alert("Mala petición");
      },
      404: function (response) {
        alert(`No existe el paciente con identificador: ${id}`);
      }
    }
  });
}

function buildDict() {
  let queryDict = {
    nombre: name_input.value,
    id: last_id,
    fecha: last_fecha,
    hora: last_hora,
    alergias: string_to_list(algs_input.value),
    enfermedades: string_to_list(enfs_input.value),
    medicamentos: string_to_list(meds_input.value),
    cirugias: string_to_list(cirs_input.value),
    otros: string_to_list(othr_input.value),
    tratamientos: string_to_list(treats_input.value),
    problemas: string_to_list(probs_input.value),
    observaciones: string_to_list(obsv_input.value)
  };

  return queryDict;
}

function updateHistorial() {
  console.log(buildDict());
  $.ajax({
    url: "http://192.168.131.39:5000/historial/" + last_id,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(buildDict()),
    crossDomain: true,
    statusCode: {
      200: function (response) {
        alert("Actualización realizada correctamente");
      },
      400: function (response) {
        alert("Mala petición");
      },
      404: function (response) {
        alert(`No existe ningún paciente con identificador ${last_id}`);
      }
    }
  });
}

button_submit.addEventListener("click", (event) => {
  if (id_input.value === "") {
    // Empty id
    alert("El Número de Identificador es obligatorio");
    historial.style.display = "";
    event.stopPropagation();
  } else {
    // Valid id
    getHistorial(id_input.value);
    last_id = id_input.value;

    if (historial.style.display === "") {
      historial.style.display = "block";
    }
  }
});

button_update.addEventListener("click", (event) => {
  if (!anyEmpty()) {
    updateHistorial();
  } else {
    alert("No puede haber campos vacios");
  }
});
