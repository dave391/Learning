function abilitaBottoneCreaTabella(){
    if (document.myForm.txtNumeroRighe.value > 0 && document.myForm.txtNumeroColonne.value> 0 ) {
        document.myForm.btnCreaTabella.disabled = false;
    } else
        document.myForms.btnCreaTabella.disabled = true;
}

function creaTabella(NumeroRighe,NumeroColonne, divTabella) {
    let divTabellaObj = document.getElementById(divTabella);
    // let NumeroRighe= document.getElementById("txtNumeroRighe");
    // let NumeroColonne = document.getElementById ("txtNumeroColonne")
    let htmlTableString = '<table id="table" class="Visible">' 
    htmlTableString += tableHeader(NumeroColonne);
    for (let i =0; i < NumeroRighe;i++) {
        htmlTableString+= tableRow(NumeroColonne);
    }
    htmlTableString += '</table>';
    divTabellaObj.innerHTML = htmlTableString;
    document.getElementById("btnHideTable").disabled = false;
}

function tableHeader(NumeroColonne){
    let htmlString ='<tr>';
        for (let i=0; i< NumeroColonne;i++) {
            htmlString += '<th> Header' + i.toString() + '</th>';
        }
    htmlString +='</tr>';
    return htmlString;
}

function tableRow (NumeroColonne){
    let htmlString ='<tr>';
        for (let i=0; i< NumeroColonne;i++) {
            htmlString += '<td> Col' + i.toString() + '</td>';
        }
    htmlString +='</tr>';
    return htmlString;  

}

function cancellaTabella(divTabella){
    let divTabellaObj = document.getElementById(divTabella);
    divTabellaObj.innerHTML="";
    document.getElementById("btnHideTable").disabled = true;
    
}

function nascondiTabella() {
    let table = document.getElementById("table");
    if (table.className == "Invisible") {
        document.getElementById("btnHideTable").textContent ="Nascondi tabella";
        table.className = "Visible";
    } else {
        document.getElementById("btnHideTable").textContent ="Visualizza tabella";
        table.className = "Invisible";
    }
}