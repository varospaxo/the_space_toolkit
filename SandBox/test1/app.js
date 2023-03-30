// for the button 
// document.getElementById('button').addEventListener('click', a);



// document.getElementById('button').addEventListener('DOMContentLoaded', a);

window.onload = function a(){
    fetch('hehe.txt')
    .then(
        function(responce){
            return responce.text();
        }
    )
    .then(
        function(data){
            console.log(data);
            document.getElementById('result').innerHTML = data ;
        }
    )
}

window.onload = function b(){
    fetch('hehe2.txt')
    .then(
        function(responce){
            return responce.text();
        }
    )
    .then(
        function(data){
            console.log(data);
            document.getElementById('result2').innerHTML = data ;
        }
    )
}