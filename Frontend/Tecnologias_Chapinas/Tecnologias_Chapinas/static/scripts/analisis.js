
const file_input = document.getElementById("file-input")
const btnCargar = document.getElementById("btnCargar")
const txtArea1 = document.getElementById("Textarea1")
const txtArea2 = document.getElementById("Textarea2")

function cargarArchivo(){
  file_input.click();
}

file_input.addEventListener("change", function() {
        var fr=new FileReader();
            fr.onload=function(){
                txtArea1.textContent=fr.result;
            }

            fr.readAsText(this.files[0]);
});


