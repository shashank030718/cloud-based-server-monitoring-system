from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import psutil
import socket
from datetime import datetime

app = FastAPI(title="Cloud Server Monitoring API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://localhost:5501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Cloud Server Monitoring API is running"
    }


@app.get("/health")
def server_health():

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    cpu_load = psutil.getloadavg()
    cpu_usage = psutil.cpu_percent(interval=1)
    uptime_seconds = int(datetime.now().timestamp() - psutil.boot_time())
    alerts = []

    if cpu_usage > 80:
        alerts.append("WARNING: High CPU Usage")

    if memory.percent > 80:
        alerts.append("WARNING: High Memory Usage")

    if disk.percent > 80:
        alerts.append("WARNING: High Disk Usage")
    return {
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().astimezone().isoformat(),

        "cpu_usage_percent": cpu_usage,
        "alerts":alerts,
        "cpu_load_average": {
            "1_min": round(cpu_load[0], 2),
            "5_min": round(cpu_load[1], 2),
            "15_min": round(cpu_load[2], 2)
        },
        "uptime_seconds": uptime_seconds,
        "cpu_load_average": {
            "1_min": round(cpu_load[0], 2),
            "5_min": round(cpu_load[1], 2),
            "15_min": round(cpu_load[2], 2)
        },		

        "memory": {
            "total_gb": round(memory.total / (1024 ** 3), 2),
            "used_percent": memory.percent,
            "available_gb": round(memory.available / (1024 ** 3), 2)
        },

        "disk": {
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "used_percent": disk.percent,
            "free_gb": round(disk.free / (1024 ** 3), 2)
        },

        "status": (
            "HEALTHY"
            if memory.percent < 80 and disk.percent < 80
            else "WARNING"
        ),
        "status": "WARNING" if alerts else "HEALTHY"
    }

