// Note for me, add more comments to take advantage of Sphinx

let priorityChart, categoryChart;

function updateDashboard() {
  // Priority chart section
  priorityChart.data = dashboardData.priority_chart_data;
  priorityChart.update();

  // Category chart section
  categoryChart.data = dashboardData.category_chart_data;
  categoryChart.update();

  // Status chart section
  statusChart.data = dashboardData.status_chart_data;
  statusChart.update();

  // Risk Matrix section
  populateRiskMatrix(dashboardData.risk_matrix_data);
}

function initPriorityChart() {
  const priorityCtx = document.getElementById("priorityChart").getContext("2d");
  priorityChart = new Chart(priorityCtx, {
    type: "bar",
    data: {},
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: "Risk Score",
          },
        },
        x: {
          title: {
            display: true,
            text: "Risk Name",
          },
        },
      },
      plugins: {
        colors: {
          forceOverride: true,
        },
      },
    },
  });
}

function initCategoryChart() {
  const categoryCtx = document.getElementById("categoryChart").getContext("2d");
  categoryChart = new Chart(categoryCtx, {
    type: "pie",
    data: {},
    options: {
      responsive: true,
      plugins: {
        colors: {
          forceOverride: true,
        },
      },
    },
  });
}

function initStatusChart() {
  const statusCtx = document.getElementById("statusChart").getContext("2d");
  statusChart = new Chart(statusCtx, {
    type: "pie",
    data: {},
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
        },
        title: {
          display: true,
          text: "Risk Status Distribution",
        },
      },
    },
  });
}

function populateRiskMatrix(data) {
  const matrix = document.querySelector(".risk-matrix tbody");
  matrix.innerHTML = "";

  for (let i = 5; i >= 1; i--) {
    const row = document.createElement("tr");
    row.innerHTML = `<th>${i}</th>`;
    for (let j = 1; j <= 5; j++) {
      const cell = document.createElement("td");
      const risks = data[`${i}-${j}`] || [];
      cell.innerHTML = risks
        .map((risk) => `<div class="risk-item">${risk}</div>`)
        .join("");
      row.appendChild(cell);
    }
    matrix.appendChild(row);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initPriorityChart();
  initCategoryChart();
  initStatusChart();
  updateDashboard();
});
