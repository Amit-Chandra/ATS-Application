document.addEventListener("DOMContentLoaded", function() {
    var pieChartData = document.getElementById("chartData").textContent;
    
    try {
        var chartObj = JSON.parse(pieChartData);
        Plotly.newPlot('skillChart', chartObj.data, chartObj.layout);
    } catch (error) {
        console.error("Error parsing Plotly chart data:", error);
    }
});
