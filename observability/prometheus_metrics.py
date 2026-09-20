from fastapi import FastAPI
from prometheus_client import Gauge, make_asgi_app

app=FastAPI()
metrics_app=make_asgi_app()
app.mount("/metrics", metrics_app)

heartRate=Gauge(
"heartRate", "Current Heart Rate Value"
)
stepCount=Gauge(
"stepCount", "Current Step Count Value"
)

activeEnergy=Gauge(
"activeEnergy", "Current Active Energy Value"
)

restingEnergy=Gauge(
"restingEnergy", "Current Resting Energy Value"
)
