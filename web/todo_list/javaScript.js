function newItem(){
    var li=document.createElement('li');
    var inputValue = document.getElementById('myInput').value;
    var y =document.createTextNode(inputValue);
    li.appendChild(y);
    if (inputValue === ''){
        alert('you must enter a value!!!')
    }
    else{
        document.getElementById('myList').appendChild(li);
    }
    document.getElementById('myInput').value ='';
    console.log(y)
        var span =document.createElement('SPAN')
        var txt = document.createTextNode('close')
        span.className ='close'
        span.appendChild(txt)
        li.appendChild(span)
        for (i = 0; i < close.length; i++) {
        close[i].onclick = function () {
        var div = this.parentElement;
        div.style.display = "none";
};
}
}
var myNodeLi = document.getElementsByTagName('LI');
var i;
for (i= 0; i<myNodeLi.length; i++){
    var span = document.createElement('SPAN');
    var txt =document.createTextNode('close');
    span.className = 'close'
    span.appendChild(txt);
    myNodeLi[1].appendChild(span);
}
var close = document.getElementsByClassName("close");
var list =document.querySelector('ul');
list.addEventListener(
    'click', 
    function (ev){
    if(ev.target.tagName === 'LI'){
        ev.target.classList.toggle('checked');
    }
}, false
)
// var i;
// for (i = 0; i < close.length; i++) {
//   close[i].onclick = function () {
//     var div = this.parentElement;
//     div.style.display = "none";
//   };
// }