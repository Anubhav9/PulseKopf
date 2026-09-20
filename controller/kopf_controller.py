import kopf
from collector import metrics_collector
from datetime import datetime, timezone
from observability import prometheus_metrics

@kopf.on.create("healthmetrics.anubhavdev.com","v1alpha1","healthmetrics")
def resource_creation(namespace,**kwargs):
    kopf.info(f"Resource created in namespace: {namespace}")


@kopf.on.update("healthmetrics.anubhavdev.com","v1alpha1","healthmetrics")
def resource_updation(spec, namespace, **kwargs):
    kopf.info(f"Resource updated in namespace: {namespace} with spec: {spec}")
    heartRateSpec=spec["heartRate_enabled"]
    stepCountSpec=spec["stepCount_enabled"]
    activeEnergySpec=spec["activeEnergy_enabled"]
    restingEnergySpec=spec["restingEnergy_enabled"]

    if heartRateSpec:
        kopf.info(f"Heart Rate metric collection is enabled in namespace: {namespace}")
    if stepCountSpec:
        kopf.info(f"Step Count metric collection is enabled in namespace: {namespace}")
    if activeEnergySpec:
        kopf.info(f"Active Energy metric collection is enabled in namespace: {namespace}")
    if restingEnergySpec:
        kopf.info(f"Resting Energy metric collection is enabled in namespace: {namespace}")

@kopf.timer("healthmetrics.anubhavdev.com","v1alpha1","healthmetrics",interval=60.0)
def collect_metrics(spec,status,patch,namespace,**kwargs):
    kopf.info(f"Collecting metrics for resource in namespace: {namespace}")
    heartRateSpec=spec["heartRate_enabled"]
    stepCountSpec=spec["stepCount_enabled"]
    activeEnergySpec=spec["activeEnergy_enabled"]
    restingEnergySpec=spec["restingEnergy_enabled"]
    current_timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    if heartRateSpec:
        heartRateData=metrics_collector.collect_metrics_after_interval("heartRate",spec["interval"])
        patch.status["current_heartRate"]=heartRateData.get("value","Not Enabled")
        patch.status["lastupdated_timestamp"]=str(current_timestamp)
        prometheus_metrics.heartRate.set(heartRateData.get("value",0))
    elif not heartRateSpec:
        patch.status["current_heartRate"]="Not Enabled"
        patch.status["lastupdated_timestamp"]="Not Enabled"

    if stepCountSpec:
        stepCountData=metrics_collector.collect_metrics_after_interval("stepCount",spec["interval"])
        patch.status["current_stepCount"]=stepCountData.get("value","Not Enabled")
        patch.status["stepCount_lastupdated_timestamp"]=str(current_timestamp)
        prometheus_metrics.stepCount.set(stepCountData.get("value",0))
    elif not stepCountSpec:
        patch.status["current_stepCount"]="Not Enabled"
        patch.status["stepCount_lastupdated_timestamp"]="Not Enabled"

    if activeEnergySpec:
        activeEnergyData=metrics_collector.collect_metrics_after_interval("activeEnergy",spec["interval"])
        patch.status["current_activeEnergy"]=activeEnergyData.get("value","Not Enabled")
        patch.status["activeEnergy_lastupdated_timestamp"]=str(current_timestamp)
        prometheus_metrics.activeEnergy.set(activeEnergyData.get("value",0))
    elif not activeEnergySpec:
        patch.status["current_activeEnergy"]="Not Enabled"
        patch.status["activeEnergy_lastupdated_timestamp"]="Not Enabled"

    if restingEnergySpec:
        restingEnergyData=metrics_collector.collect_metrics_after_interval("restingEnergy",spec["interval"])
        patch.status["current_restingEnergy"]=restingEnergyData.get("value","Not Enabled")
        patch.status["restingEnergy_lastupdated_timestamp"]=str(current_timestamp)
        prometheus_metrics.restingEnergy.set(restingEnergyData.get("value",0))
    elif not restingEnergySpec:
        patch.status["current_restingEnergy"]="Not Enabled"
        patch.status["restingEnergy_lastupdated_timestamp"]="Not Enabled"

