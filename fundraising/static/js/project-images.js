document.getElementById("add_image").onclick=function (ev) {

        var image=document.getElementById("images");

        var preview=document.createElement("img");
        preview.style.width="auto";
        preview.style.height="100px";

        var newInput=document.createElement("input");
        newInput.type="file";
        newInput.name="file[]";

        var br=document.createElement("br");
        var br1=document.createElement("br");

        newInput.onchange=function (ev1) {
            if(this.files && this.files[0]){
                var fileReader=new FileReader();
                fileReader.onload=function (ev2) {
                    preview.src=ev2.target.result;
                };
                fileReader.readAsDataURL(this.files[0])
                }
        };

        image.appendChild(preview);
        image.appendChild(newInput);
        image.appendChild(br);
        image.appendChild(br1);

    }