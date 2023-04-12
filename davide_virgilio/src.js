function pageLoading() {

    genesis = `<h1>Costruzione tabella</h1>
	<label for="num-righe">Numero di righe:</label>
	<input type="number" id="num-righe" min="1"><br><br>
	<label for="num-colonne">Numero di colonne:</label>
	<input type="number" id="num-colonne" min="1"><br><br>
	<button onclick="costruisciTabella()">Crea tabella</button>
	<div id="tabella-container"></div>`;
    document.getElementById("pageLoadingID").innerHTML= genesis;

}
