
const ctx1 = document.getElementById('websiteViewsChart').getContext('2d');
const websiteViewsChart = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
        datasets: [{
            label: 'Views',
            data: [40, 20, 50, 30, 60, 70, 40],
            backgroundColor: '#6C757D',
            borderColor: '#6C757D',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx2 = document.getElementById('dailySalesChart').getContext('2d');
const dailySalesChart = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Sales',
            data: [200, 400, 300, 600, 500, 700, 400, 500, 600],
            backgroundColor: 'rgba(0, 123, 255, 0.2)',
            borderColor: '#007BFF',
            borderWidth: 2,
            fill: true
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx3 = document.getElementById('completedTasksChart').getContext('2d');
const completedTasksChart = new Chart(ctx3, {
    type: 'line',
    data: {
        labels: ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Tasks',
            data: [300, 500, 400, 600, 700, 800, 500, 600, 700],
            backgroundColor: 'rgba(108, 117, 125, 0.2)',
            borderColor: '#6C757D',
            borderWidth: 2,
            fill: true
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
