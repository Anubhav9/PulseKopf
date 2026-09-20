# PulseKopf

A Kubernetes controller that collects personal health metrics from a smart ring and exposes them on the cluster.

## Folder structure

```
PulseKopf/
├── collector/        # Fetches metrics for the configured interval
├── controller/       # kopf handlers for the HealthMetric custom resource
├── generator/        # Generates the CRD schema from the Pydantic models
├── integrations/     # Health API client
├── models/           # Pydantic models for the spec and status
├── observability/    # FastAPI app exposing Prometheus gauges
├── resources/        # HealthMetric CRD manifest
├── Dockerfile
└── requirements.txt
```
