//var g1=document.getElementById(g1);
//g1.textContent=table; 
//var k1=document.getElementById(k1); 
//k1.textContent=table; 
//var s1=document.getElementById(s1); 
//s1.textContent=table; 
//var m1=document.getElementById(m1); 
//m1.textContent=table; 
//var i1=document.getElementById(i1); 
//i1.textContent=table; 

function rewriteFormModal(week,time){
    let weeks = ["月","火","水","木","金"]
    document.getElementById("form-week").innerText = "曜日　："+weeks[week]+"曜日";
    document.getElementById("form-time").innerText = "時間　："+String(time)+"時限";
}
