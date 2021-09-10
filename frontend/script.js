let base_url = 'http://127.0.0.1:8000/api/'
let gotSecret = document.getElementById('gotSecret')
let _hash
let secretText
let hours
let expireAfterViews
let go = document.getElementById('go')
let submit = document.getElementById('submit')

//go.addEventListener("click",addSecret())
//submit.addEventListener("click",addSecret())

function getData(){
    _hash = document.getElementById('hash_input').value
    secretText = document.getElementById('secret_input').value
    hours = document.getElementById('hours').value
    expireAfterViews = document.getElementById('views').value
}

function getSecret(){
    getData()
    let data = {
        _hash : _hash
    }
    console.log(data)
    fetch(base_url+'secret/' + _hash)
    .then(response=>response.json())
    .then(data => {
        console.log(data)
        if(data.secretText != undefined){
                gotSecret.innerHTML = `${data.secretText} <br> Expires at: ${data.expiresAt}`+
                `, or after ${data.remainingViews} more views.`;
        } else {
            gotSecret.innerHTML = data.Message;
        }

    })
}

function addSecret(){
    getData()
    let data = {
        secretText : secretText,
        expireAfterViews : expireAfterViews,
        expireAfter : hours
    }
    fetch(base_url+'secret/',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response=>response.json())
    .then(data=>{
        alert("Secret created! Your hash is: " + data)
        console.log(data)
    })
}
