function genesis(){
    const title = document.createElement("h1");
    title.innerHTML = "TEST TITOLO";
    document.getElementById("divOne").appendChild(title);
}

function showPatente () {
    const radioSi = document.createElement("input");
    radioSi.type = "radio";
    radioSi.name = "radio";
    radioSi.id ="radioSiId";
    const labelSi = document.createElement("label");
    //labelSi.for radioSiId = "Si"; 
    labelSi.for = "radioSiId";
    labelSi.innerHTML = "Si";
    const radioNo = document.createElement("input");
    radioNo.type = "radio";
    radioNo.name = "radio";
    radioNo.id ="radioNoId";
    const labelNo = document.createElement("label");
    
    labelNo.for = "radioNod";
    labelNo.innerHTML = "No";
// Append to body:
    document.body.appendChild(radioSi);
    document.body.appendChild(labelSi);
    document.body.appendChild(radioNo);
    document.body.appendChild(labelNo);
     }

