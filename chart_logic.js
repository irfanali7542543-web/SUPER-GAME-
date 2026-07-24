// Initialize Chart
const chartContainer = document.getElementById('chart');
const chart = LightweightCharts.createChart(chartContainer, {
    width: chartContainer.clientWidth,
    height: 400,
    layout: { backgroundColor: '#000', textColor: '#DDD' },
});

const lineSeries = chart.addLineSeries();

// Function to fetch live data from your server
function updateChart() {
    fetch('/api/live-data') 
        .then(response => response.json())
        .then(data => {
            lineSeries.update(data);
        });
}

// Update chart every 2 seconds
setInterval(updateChart, 2000);
