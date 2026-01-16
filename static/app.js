async function guardar() {
  const data = {
    nombre: nombre.value,
    apellido: apellido.value,
    numero_id: numero_id.value,
    color_favorito: color.value
  };

  await fetch("/api/practica", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
}
