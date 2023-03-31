// for the button 
// document.getElementById('button').addEventListener('click', a);



// document.getElementById('button').addEventListener('DOMContentLoaded', a);

window.onload = function a(){
    fetch('hehe.txt')
    .then(
        function(responce1){
            return responce1.text();
        }
    )
    .then(
        function(data1){
            console.log(data1);
            document.getElementById('result').innerHTML = data1 ;
        }
    )
}

window.onload = function b(){
    fetch('hehe2.txt')
    .then(
        function(responce2){
            return responce2.text();
        }
    )
    .then(
        function(data2){
            console.log(data2);
            document.getElementById('result2').innerHTML = data2 ;
        }
    )
}