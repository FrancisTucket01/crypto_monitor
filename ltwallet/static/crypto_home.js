// JS

window.addEventListener("scroll",() =>{
    const top = window.scrollY;
    const newnav = document.getElementById('newnav');
    if (top >= 40){
        newnav.classList.add("sticky-nav");
        logo.style.display = "block";
    }
    if (top < 38){
        newnav.classList.remove("sticky-nav");
        logo.style.display = "none";
    }
})

function reloader(db="BTCKSH"){
    var dataPoints = [];
    var dataPoints1 = [];
    try{
        new_chart.removeChild(new_chart.children[0]);
    }catch(err){}
    
    status = new_chart.hasChildNodes()
    
    new_chart.innerHTML = "Hello there from beyond";

    let current_url = "https://cyan-mirrors-smile-34-86-111-132.loca.lt/chartdata/candlestic/"+db+"D/null/null";
    let current_url1 = "https://cyan-mirrors-smile-34-86-111-132.loca.lt/chartdata/line/"+db+"D/null/null";
    // check if user in dashboard and set the chart title to null
    // Canvas js chart
    var chart = new CanvasJS.Chart("chartContainer",{
        animationEnabled: true,
        theme: "light2", // "light1", "light2", "dark1", "dark2"
        exportEnabled: true,
        title:{
            text:"Crypto "+db,
            fontColor: "white",
        },
        subtitles: [{
            text: "Daily Averages",
            fontColor: "white",
        }],
        axisX:{
            titleFontColor: "white",
            labelFontColor: "white",
            crosshair: {
                enabled: true
            },
            labelAngle: -45
            },
        axisY:{
            titleFontColor: "white",
            labelFontColor: "white",
            crosshair: {
                enabled: true
            },
            },
        backgroundColor: "#124143",
        zoomEnabled:true,
        legend: {
            fontColor: "white",
        },
        data: [{
            type: "candlestick",
            risingColor: "red", 
            showInLegend: true,
            name: "Crypto Price",
            fallingColor: "green",
            dataPoints: dataPoints,
        },
        {
            type: "line",
            showInLegend: true,
            name: "Volume",
            axisYType: "secondary",
            yValueFormatString: "$#,##0.00bn",
            xValueFormatString: "MMMM",
            dataPoints: dataPoints1,
        }],
    });

    var loader = document.getElementById("loader-home"); 
    $(loader.style.display = "flex");
    //ajax to get data from the database
    $.getJSON(current_url, function(data) {
        for(var i = 0; i < data.length; i++) {
            const today = new Date(data[i].date);
            const yyyy = today.getFullYear();
            let mm = today.getMonth() + 1; // Months start at 0!
            let dd = today.getDate();

            if (dd < 10) dd = '0' + dd;
            if (mm < 10) mm = '0' + mm;

            const formattedToday = dd + '/' + mm + '/' + yyyy;
            dataPoints.push({ x:new Date(data[i].date), y:[data[i].price[0]*134.00, data[i].price[1]*134.00, data[i].price[2]*134.00, data[i].price[3]*134.00]});
            //dataPoints.push({ label: data[i].label, y: data[i].price });            
        }
        chart.render();
    });
    $.getJSON(current_url1, function(data) {
        for(var i = 0; i < data.length; i++) {
            const today = new Date(data[i].date);
            const yyyy = today.getFullYear();
            let mm = today.getMonth() + 1; // Months start at 0!
            let dd = today.getDate();

            if (dd < 10) dd = '0' + dd;
            if (mm < 10) mm = '0' + mm;

            const formattedToday = dd + '/' + mm + '/' + yyyy;
            dataPoints1.push({ x:new Date(data[i].date), y:data[i].price[0]*134.00});
            //dataPoints.push({ label: data[i].label, y: data[i].price });            
        }
        $(loader.style.display = "none");
        chart.render();
    });
}
