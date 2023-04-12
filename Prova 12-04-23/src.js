// Genera struttura html della pagina al momento t0
function caricaPagina() {
    genesi = `<h1>Costruzione tabella</h1>
	<label for="num-righe">Numero di righe:</label>
	<input type="number" id="num-righe" min="1"><br><br>
	<label for="num-colonne">Numero di colonne:</label>
	<input type="number" id="num-colonne" min="1"><br><br>
	<button onclick="costruisciTabella()" class="button-disabled" id="crea-btn" disabled>Crea tabella</button>
	<div id="tabella-container"></div>`;
    document.getElementById("carica-pagina").innerHTML= genesi;

	// Aggiunge dei listener sugli input per monitorare l'input dell'utente
	document.getElementById("num-righe").addEventListener("input", controlloValori);
	document.getElementById("num-colonne").addEventListener("input", controlloValori);
}

// Verifica che i valori inseriti siano validi cambia id del bottone per css.
function controlloValori() {
	var numR = parseInt(document.getElementById("num-righe").value);
	var numC = parseInt(document.getElementById("num-colonne").value);
	var button = document.getElementById("crea-btn");
	if (isNaN(numR) || isNaN(numC) || numR <= 0 || numC <= 0) {
		button.disabled = true;
	} else {
		button.disabled = false;
		button.id = "button";
	}
}

// Recupera il numero di righe e colonne inseriti dall'utente
function costruisciTabella() {
	var numRighe = parseInt(document.getElementById("num-righe").value);
	var numColonne = parseInt(document.getElementById("num-colonne").value);
	
	// Crea la tabella
	var tabella = document.createElement("table");
	
	// Crea l'intestazione e le colonne della tabella
	var rigaIntestazione = document.createElement("tr");
	for (var i = 0; i <= numColonne; i++) {
		var cella = document.createElement("th");
		var testoCella = document.createTextNode("Colonna " + i);
		cella.appendChild(testoCella);
		rigaIntestazione.appendChild(cella);
	}
	tabella.appendChild(rigaIntestazione);
	
	// Crea le righe della tabella
	for (var i = 0; i <= numRighe; i++) {
		var riga = document.createElement("tr");
		for (var j = 0; j <= numColonne; j++) {
			var cella = document.createElement("td");
			cella.setAttribute("id","col")
			var testoCella = document.createTextNode("Riga " + i + ", Colonna " + j);
			cella.appendChild(testoCella);
			riga.appendChild(cella);
		}
		tabella.appendChild(riga);
	}
	
	// Visualizza la tabella
	var tabellaContainer = document.getElementById("tabella-container");
	tabellaContainer.innerHTML = "";
	tabellaContainer.appendChild(tabella);

	// Aggiungi bottone per nascondere la tabella
	var btnMostraNascondi = document.createElement("button");
	btnMostraNascondi.innerHTML = "Nascondi";
	tabellaContainer.appendChild(btnMostraNascondi);

	// Mostra e nasconde sul click dell'utente
	btnMostraNascondi.onclick = function()
	
	{
		if (tabella.style.display == "none") {
			tabella.style.display = "table";
			btnMostraNascondi.innerHTML = "Nascondi"
		} else {
			tabella.style.display = "none";
			btnMostraNascondi.innerHTML = "Mostra"
		}
	};
	

	// Aggiungi bottone per svuotare la tabella
	var btnSvuotaTabella = document.createElement("button");
	btnSvuotaTabella.innerHTML = "Svuota tabella";
	// Svuota tabella sul click dell'utente
	btnSvuotaTabella.onclick = function()
	{
		var celleTabella = tabella.getElementsByTagName("col");
		for (var i = 0; i < celleTabella.length; i++) {
			celleTabella[i].innerHTML = "";
		}
		btnSvuotaTabella.disabled = true;
		btnSvuotaTabella.id = "buttonDisabled";
	};
	
	tabellaContainer.appendChild(btnSvuotaTabella);
}