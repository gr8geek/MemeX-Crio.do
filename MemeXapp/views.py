from django.conf.urls import url
from django.shortcuts import render,HttpResponse,redirect
def index1(request):
    return HttpResponse('''
<!DOCTYPE html>
<html>
    <style>
    img{
        width:80%;
        height:80%;
    }
        .memeEle{
            margin-top:4%;
            margin-left:5%;
            width:30%;
            height:30%;
        }
       
    </style>
    <script>
        document.addEventListener("DOMContentLoaded",(event)=>{
                        function loadhun(){
                var xmlhttp = new XMLHttpRequest();
                var url = "memes";
                console.log("Inside")
                xmlhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        var myArr = JSON.parse(this.responseText);
                        console.log(myArr)
                        var divren = document.getElementById("memediv")
                        myArr.forEach((elem)=>{
                            var nele = document.createElement("div")
                            nele.classList.add("memeEle")
                            var img = document.createElement("img")
                            img.src=elem["url"]
                            var name = document.createElement("h4")
                            name.innerText = elem["name"]
                            var cap = document.createElement("p")
                            cap.innerText = elem["caption"]
                            nele.appendChild(name)
                            nele.appendChild(cap)
                            nele.appendChild(img)
                            divren.appendChild(nele)
                        })
                    }
                };
                xmlhttp.open("GET", url, true);
                xmlhttp.send();

            }
            var btn = document.getElementById("btn")
            btn.onclick = (event)=>{
                event.preventDefault()
                var owner = document.getElementById("owner").value
                var caption = document.getElementById("caption").value
                var url = document.getElementById("url").value

                var xhr = new XMLHttpRequest();
                var url_name = "memes";
                xhr.open("POST", url_name, true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === 4 && xhr.status === 200) {
                        var json = JSON.parse(xhr.responseText);
                        console.log(json)
                    }
                };
                var data = JSON.stringify({"name":owner, "caption": caption,"url":url});
                xhr.send(data);

            }

            loadhun()
        })
        
    </script>
    <body>
    <h1>Meme Stream</h1>
        <div class="formdiv">
            <form action="/memes" method="POST">
                <label for="owner">Meme Owner: </label>
                <input id="owner" type="text" name="owner" value=""placeholder="Enter your full name">
                <br>
                <label for="caption">Caption: </label>
                <input id="caption" type="text" name="caption" value=""placeholder="Be creative with caption">
                <br>
                <label for="url">Meme URL: </label>
                <input id="url" type="text" name="url" value=""placeholder="Enter url of your meme here">
                <br>
                <button id="btn" >Submit</button>
            </form>
        </div>
        <p>___________________________________________________________________________________________________________________________________________________________________<p>
        <div id = "memediv" style="
                margin:4px, 4px; 
                padding:4px; 
                width: 100%; 
                height: 100vh; 
                overflow-x: hidden; 
                overflow-y: auto; 
        " >

        </div>
    </body>
</html>

    ''')
