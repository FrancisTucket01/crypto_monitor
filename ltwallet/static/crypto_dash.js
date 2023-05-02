// Javascript
const logo = document.getElementById('logo');
logo.style.display = "none";
var prev_db = null;
var new_chart = document.getElementById("chartContainer");
const popup = document.getElementById("popup").style.display;
const scroler = document.getElementById("scrol");
const scro = document.getElementById("scro");
const theme = document.getElementById("theme");
const wrapper = document.getElementById("wrapper");
const newsli = document.getElementById("newsli");
const lists = document.getElementsByClassName("lists");
const them = sessionStorage.getItem("theme");
const hed = document.getElementById("hed");
// const mychart = document.getElementById("chart");
const themeText = document.getElementById("theme-text");
var dataPoints = [];
var dataPoints1 = [];

window.onload(reloader());
function loadProfile(state){
    if (state == 'over'){
        profCont.classList.toggle('prof-vis');
        console.log("Overed");
    }
    else if(state == 'out'){
        profCont.classList.toggle('prof-vis');
        console.log("!Overed");
    }
}

function log_clicked(dbs){
    if (prev_db == null){
        document.getElementById(dbs).classList.toggle("active-sub-header-link");
        prev_db = dbs;
    }
    else{
        document.getElementById(dbs).classList.toggle("active-sub-header-link");
        document.getElementById(prev_db).classList.toggle("active-sub-header-link");
        prev_db = dbs;
    }        
}

function closeflasher(){
    const outing = document.getElementById("flasher");
    outing.style.display = "none";
    }



function notify() {
    if (popup == "none"){
        document.getElementById("popup").style.display = "grid";
    }
}
scroler.addEventListener("click", () =>{
    window.scrollTo({ top: 0, behavior: 'smooth' })
    
})

window.addEventListener("scroll",() =>{
    const top = window.scrollY;
    if(top >= 400){
        scro.classList.add("visible");
    }
    if (top < 400 ){
        scro.classList.remove("visible");
    }
})

function themeToggle(){
    wrapper.classList.toggle("dark");
    hed.classList.toggle("dark");
    //newsli.classList.toggle("dark");
    mychart.classList.toggle("dark");
    for (i=0; i<lists.length; i++){
        lists[i].classList.toggle("dark");
    }
    if (document.getElementById("theme-text").innerHTML == 'Light Theme'){
        document.getElementById("theme-text").innerHTML = 'Dark Theme';
    }
    else{
        document.getElementById("theme-text").innerHTML = "Light Theme"
    }
    if ( them == "dark"){
        sessionStorage.setItem("theme", "light");
    }else if(them == "light"){
        sessionStorage.setItem("theme", "dark");
    }
    else{
        sessionStorage.setItem("theme", "light");
    }
}
function changeTheme(){
    wrapper.classList.toggle(them);
    hed.classList.toggle(them)
    mychart.classList.toggle(them)
    if (them == 'dark'){
        document.getElementById("theme-text").innerText = "Light Theme"
    }
    else{
        document.getElementById("theme-text").innerText = "Dark Theme"
    }
    for (i=0; i<lists.length; i++){
        lists[i].classList.toggle(them);
    }
}


