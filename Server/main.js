
var filename;

function postImage() {

    var url = "http://localhost:8001";   // The URL and the port number must match server-side
    var endpoint = "/upload";            // Endpoint must match server endpoint
    var http = new XMLHttpRequest();
    var payloadObj = document.getElementById('inputFile').files[0];
    var formData = new FormData();

    formData.append("image", payloadObj);

    // prepare POST request
    http.open("POST", url+endpoint, true);
    http.setRequestHeader("Content-Type", "multipart/form-data");

    http.onreadystatechange = function() {
        var DONE = 4;       // 4 means the request is done.
        var OK = 200;       // 200 means a successful return.
        if (http.readyState == DONE && http.status == OK && http.responseText) {

            //var replyObj = JSON.parse(replyString);
            filename = http.response;
        }
    };

    http.send(formData);


    /*
    var url = "http://localhost:8001";   // The URL and the port number must match server-side
    var endpoint = "/upload";            // Endpoint must match server endpoint
    var http = new XMLHttpRequest();
    var payloadObj = document.getElementById('inputFile').files[0];

    // prepare POST request
    http.open("POST", url+endpoint, true);
    http.setRequestHeader("Content-Type", "multipart/form-data");

    http.onreadystatechange = function() {
        var DONE = 4;       // 4 means the request is done.
        var OK = 200;       // 200 means a successful return.
        if (http.readyState == DONE && http.status == OK && http.responseText) {

            //var replyObj = JSON.parse(replyString);
            filename = http.response;
        }
    };
    // Send request
    http.send(payloadObj);

    */
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