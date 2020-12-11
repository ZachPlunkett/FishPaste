

const handleImageUpload = event => {
    const files = event.target.files
    const formData = new FormData()
    formData.append('file', files[0])

    fetch('http://localhost:8001/upload', {
        method: 'POST',
        body: formData
    })
        .then(function(response) {
            return response.text().then(function(text) {
                console.log(text);
            });
        })
        .catch(error => {
            console.error(error)
        })

}

window.onload=function(){
    document.querySelector('#inputFile').addEventListener('change', event => {
        handleImageUpload(event)
    })
}


function getLabeledImage() {

    var url = "http://localhost:8001";   // The URL and the port number must match server-side
    var endpoint = "/labeled/";            // Endpoint must match server endpoint
    var filename = document.getElementById("fileParagraph").innerHTML;

    var http = new XMLHttpRequest();


    // prepare GET request
    http.open("GET", url+endpoint+filename, true);

    http.onreadystatechange = function() {
        var DONE = 4;       // 4 means the request is done.
        var OK = 200;       // 200 means a successful return.
        if (http.readyState == DONE && http.status == OK && http.responseText) {

            //var replyObj = JSON.parse(replyString);
            var reply = http.response;

            document.getElementById("result").innerHTML = reply;
        }
    };

    // Send request
    http.send();
}