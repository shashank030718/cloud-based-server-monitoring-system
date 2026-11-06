
const API_URL = "http://localhost:8002/health";

async function fetchServerHealth() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to fetch server data");
        }

        const data = await response.json();
        // Update Hostname
        document.getElementById("hostname").textContent =
            data.hostname;
        // Update Server Uptime
        const uptimeSeconds = data.uptime_seconds;

        const days = Math.floor(uptimeSeconds / 86400);
        const hours = Math.floor((uptimeSeconds % 86400) / 3600);
        const minutes = Math.floor((uptimeSeconds % 3600) / 60);

        document.getElementById("uptime").textContent =
    `        ${days}d ${hours}h ${minutes}m`;

        // Update Monitoring Alerts
        const alertsElement = document.getElementById("alerts");

        if (data.alerts.length === 0) {
            alertsElement.textContent = "No alerts - All systems healthy";
            alertsElement.style.color = "#22c55e";
        } else {
            alertsElement.textContent = data.alerts.join(" | ");
            alertsElement.style.color = "#ef4444";
        }
        // CPU Usage
        document.getElementById("cpu").textContent =
            data.cpu_usage_percent + "%";

        document.getElementById("cpu-bar").style.width =
            data.cpu_usage_percent + "%";

        // Memory Usage
        document.getElementById("memory").textContent =
            data.memory.used_percent + "%";

        document.getElementById("memory-bar").style.width =
            data.memory.used_percent + "%";

        // Disk Usage
        document.getElementById("disk").textContent =
            data.disk.used_percent + "%";

        document.getElementById("disk-bar").style.width =
            data.disk.used_percent + "%";

        // Server Status
        document.getElementById("status").textContent =
            data.status;

        // Last Updated
        document.getElementById("last-updated").textContent =
            "Last Updated: " + new Date(data.timestamp).toLocaleString();

    } catch (error) {
        console.error("Monitoring API Error:", error);

        document.getElementById("status").textContent =
            "API OFFLINE";

        document.getElementById("status").style.color = "#ef4444";
    }
}

fetchServerHealth();

setInterval(fetchServerHealth, 5000);

