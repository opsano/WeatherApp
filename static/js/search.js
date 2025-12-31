const input = document.getElementById("searchInput");
const suggestionsDiv = document.getElementById("suggestions");

input.addEventListener("input", async () => {
    const query = input.value.trim();

    if (query.length < 2){
        suggestionsDiv.innerHTML = "";
        return;
    }

    const res = await fetch(`api/autocomplete/?q=${encodeURIComponent(query)}`)
    const data = await res.json();

    console.log(data);

    suggestionsDiv.innerHTML = "";

    data.names.forEach((name) => {
    const item = document.createElement("div");
    item.className = "suggestion-item";
    item.textContent = name;
    item.addEventListener("click", () => {
      input.value = name;
      window.location.href = `/weather/?q=${encodeURIComponent(name)}`;
    });
    suggestionsDiv.appendChild(item);
  });
});