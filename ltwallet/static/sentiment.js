window.onload = function () {
    var positive = {{ sentiment[0] }};
    console.log(positive);

    var chart = new CanvasJS.Chart("chartContainer", {
        exportEnabled: true,
        animationEnabled: true,
        title:{
            text: "State Operating Funds"
        },
        legend:{
            cursor: "pointer",
            itemclick: explodePie
        },
        data: [{
            type: "pie",
            showInLegend: true,
            toolTipContent: "{name}: <strong>{y}%</strong>",
            indexLabel: "{name} - {y}%",
            dataPoints: [
                { y: {{ sentiment[0] }}, name: "School Aid", exploded: true },
                { y: {{ sentiment[1] }}, name: "Medical Aid" },
                { y: {{ sentiment[2] }}, name: "Debt/Capital" },
            ]
        }]
    });
    chart.render();
    }
    
    function explodePie (e) {
        if(typeof (e.dataSeries.dataPoints[e.dataPointIndex].exploded) === "undefined" || !e.dataSeries.dataPoints[e.dataPointIndex].exploded) {
            e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
        } else {
            e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
        }
        e.chart.render();
    
    }