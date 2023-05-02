// Javascript
const foota = document.getElementById("footer");
foota.remove();


function reloader(db="BTCKSH"){
    var dataPoints2 = [];
    var dataPoints1 = [];
    try{
        new_chart.removeChild(new_chart.children[0]);
    }catch(err){}
    
    let current_url = "https://cyan-mirrors-smile-34-86-111-132.loca.lt/chartdata/candlestic/"+db+"D/null/null";
    let current_url1 = "https://cyan-mirrors-smile-34-86-111-132.loca.lt/chartdata/line/"+db+"D/high/low";
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
            type: "line",
            showInLegend: true,
            name: "predicted price",
            axisYType: "primary",
            yValueFormatString: "$#,##0.00bn",
            xValueFormatString: "MMMM",
            dataPoints: dataPoints1,
        },
        {
            type: "line",
            showInLegend: true,
            name: "Actual Price",
            axisYType: "primary",
            yValueFormatString: "$#,##0.00bn",
            xValueFormatString: "MMMM",
            dataPoints: dataPoints2,
        }],
    });

    //ajax to get data from the database
    var loader = document.getElementById("loader"); 
    $(loader.style.display = "flex");
    $.ajax({
        url : current_url1,
        contentType: 'application/json',
        dataType: 'json',
        type: 'GET',  
        success:function (data) {
            for(var i = 0; i < data.length; i++) {
                const today = new Date(data[i].date);
                const yyyy = today.getFullYear();
                let mm = today.getMonth() + 1; // Months start at 0!
                let dd = today.getDate();
    
                if (dd < 10) dd = '0' + dd;
                if (mm < 10) mm = '0' + mm;
    
                const formattedToday = dd + '/' + mm + '/' + yyyy;
                dataPoints2.push({ x:new Date(data[i].date), y:data[i].price[1]*134.00});  
                dataPoints1.push({ x:new Date(data[i].date), y:data[i].price[0]*134.00});        
            }
            $(loader.style.display = "none");
            chart.render();
        },
        error: function(jqXHR, textStatus, errorThrown) {alert("ERR: 1286: Failed to load the data. Check your internet connection or contact the administrator of the site");}
    });
    // $.ajax({
    //     url : current_url1,
    //     contentType: 'application/json',
    //     dataType: 'json',
    //     type: 'GET',  
    //     success:function(data) {
    //             for(var i = 0; i < data.length; i++) {
    //                 const today = new Date(data[i].date);
    //                 const yyyy = today.getFullYear();
    //                 let mm = today.getMonth() + 1; // Months start at 0!
    //                 let dd = today.getDate();
        
    //                 if (dd < 10) dd = '0' + dd;
    //                 if (mm < 10) mm = '0' + mm;
        
    //                 const formattedToday = dd + '/' + mm + '/' + yyyy;
    //                 dataPoints1.push({ x:new Date(data[i].date), y:data[i].price[0]});       
    //             }
    //             $(loader.style.display = "none");
    //             chart.render();
    //         },
    //     error: function(jqXHR, textStatus, errorThrown) {alert("failed");}
    // });
}