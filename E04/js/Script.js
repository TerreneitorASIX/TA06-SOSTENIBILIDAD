document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search");
    const fileList = document.getElementById("file-list");
    const selectedFileName = document.getElementById("selected-file-name"); // Referencia al div donde aparece el nombre del archivo
    const columns = [
        document.getElementById("col1"),
        document.getElementById("col2"),
        document.getElementById("col3"),
        document.getElementById("col4")
    ];

    const files = ["resultats_P1.csv","resultats_P10.csv","resultats_P100.csv","resultats_P1000.csv","resultats_P1001.csv","resultats_P1002.csv","resultats_P10004.csv","resultats_P10005.csv","resultats_P10006.csv","resultats_P10007.csv","resultats_P10008.csv","resultats_P10009.csv","resultats_P10010.csv","resultats_P10011.csv","resultats_P10012.csv","resultats_P10013.csv","resultats_P10014.csv","resultats_P10015.csv","resultats_P10016.csv","resultats_P10017.csv","resultats_P10018.csv","resultats_P10019.csv","resultats_P10020.csv","resultats_P10021.csv","resultats_P10022.csv","resultats_P10023.csv","resultats_P10024.csv","resultats_P10025.csv","resultats_P10026.csv","resultats_P10027.csv","resultats_P10028.csv","resultats_P10029.csv","resultats_P10030.csv","resultats_P10031.csv","resultats_P10032.csv","resultats_P10033.csv","resultats_P10034.csv","resultats_P10035.csv","resultats_P10036.csv","resultats_P10037.csv","resultats_P10038.csv","resultats_P10039.csv","resultats_P10040.csv","resultats_P10041.csv","resultats_P10042.csv","resultats_P10043.csv","resultats_P10044.csv","resultats_P10045.csv","resultats_P10046.csv","resultats_P10047.csv","resultats_P10048.csv","resultats_P10049.csv","resultats_P10050.csv","resultats_P10051.csv","resultats_P10052.csv","resultats_P10053.csv","resultats_P10054.csv","resultats_P10055.csv","resultats_P10056.csv","resultats_P10057.csv","resultats_P10058.csv","resultats_P10059.csv","resultats_P10060.csv","resultats_P10061.csv","resultats_P10062.csv","resultats_P10063.csv","resultats_P10064.csv","resultats_P10065.csv","resultats_P10066.csv","resultats_P10067.csv","resultats_P10068.csv","resultats_P10069.csv","resultats_P10070.csv","resultats_P10071.csv","resultats_P10072.csv","resultats_P10073.csv","resultats_P10074.csv","resultats_P10075.csv","resultats_P10076.csv","resultats_P10077.csv","resultats_P10078.csv"];

    function renderFileList(fileArray) {
        fileList.innerHTML = "";
        fileArray.forEach(file => {
            const item = document.createElement("div");
            item.classList.add("file-item");
            item.textContent = file;
            item.addEventListener("click", () => {
                loadFile(file);
                fileList.style.display = "none"; // Oculta la lista después de seleccionar un archivo
                searchInput.value = ""; // Limpia el campo de búsqueda
            });
            fileList.appendChild(item);
        });
    }

    function loadFile(file) {
        console.log(`Cargando el archivo: csv/${file}`);

        // ✅ Mostrar el nombre del archivo seleccionado
        selectedFileName.textContent = `Archivo seleccionado: ${file}`;

        fetch(`csv/${file}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Error al cargar el archivo: ${response.statusText}`);
                }
                return response.text();
            })
            .then(data => {
                console.log("Contenido del archivo:\n", data);

                let rows = data.split("\n").map(row => row.trim()).filter(row => row !== "");
                
                if (rows.length < 2) {
                    console.error("El archivo CSV parece vacío o tiene solo encabezado.");
                    return;
                }

                // Filtrar encabezados no deseados
                rows = rows.filter(row => /\d/.test(row));
                rows = rows.filter(row => !row.includes("5 anys més plujosos:"));
                rows = rows.filter(row => !row.includes("5 anys menys plujosos:"));
                rows = rows.filter(row => !row.includes("5 anys amb més variació interanual:"));
                rows = rows.filter(row => !row.includes("5 anys amb menys variació interanual:"));

                // Limpiar las columnas antes de agregar contenido nuevo
                columns.forEach(col => col.innerHTML = "");

                // Distribuir filas en las 4 columnas de forma equilibrada
                const chunkSize = Math.ceil(rows.length / columns.length);
                columns.forEach((col, index) => {   
                    const chunk = rows.slice(index * chunkSize, (index + 1) * chunkSize);
                    chunk.forEach(row => {
                        const div = document.createElement("div");
                        div.textContent = row;
                        col.appendChild(div);
                    });
                });
            })
            .catch(error => console.error("Error cargando el archivo:", error));
    }

    searchInput.addEventListener("input", () => {
        const query = searchInput.value.toLowerCase();
        if (query === "") {
            fileList.style.display = "none"; // Oculta la lista cuando no hay búsqueda
        } else {
            fileList.style.display = "block"; // Muestra la lista si el usuario escribe algo
            const filteredFiles = files.filter(file => file.toLowerCase().includes(query));
            renderFileList(filteredFiles);
        }
    });

    fileList.style.display = "none"; // Ocultar la lista al inicio
});
