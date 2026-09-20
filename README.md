# PulseKopf

A Kubernetes controller that brings personal health metrics into the cluster.

PulseKopf watches a `HealthMetric` custom resource (`healthmetrics.anubhavdev.com/v1alpha1`) and, on a timer, pulls the metrics you enabled from a health API, writes the latest values into the resource's `status`, and exposes them as Prometheus gauges.

## How it works

- **CRD** (`resources/health_metrics_crd.yaml`) — defines `HealthMetric`; its schema is generated from the Pydantic models in `models/` via `generator/spec_generator.py`.
- **Controller** (`controller/kopf_controller.py`) — [kopf](https://kopf.readthedocs.io/) handlers for create/update plus a timer that collects metrics every 60s.
- **Collector / integration** (`collector/`, `integrations/`) — fetches `heartRate`, `stepCount`, `activeEnergy` and `restingEnergy` for the interval configured on the resource.
- **Observability** (`observability/prometheus_metrics.py`) — a FastAPI app exposing the gauges at `/metrics`.

### Example resource

```yaml
apiVersion: healthmetrics.anubhavdev.com/v1alpha1
kind: HealthMetric
metadata:
  name: my-metrics
spec:
  heartRate_enabled: true
  stepCount_enabled: true
  activeEnergy_enabled: false
  restingEnergy_enabled: false
  interval: 60
```

## Running

The health API token is read from the `HEALTH_API_KEY` environment variable.

Locally:

```bash
pip install -r requirements.txt
kubectl apply -f resources/health_metrics_crd.yaml
kopf run --standalone --all-namespaces controller/kopf_controller.py
```

With Docker:

```bash
docker build -t pulsekopf .
docker run --rm -e HEALTH_API_KEY=... -v ~/.kube:/home/pulsekopf/.kube:ro pulsekopf
```

In-cluster, the controller uses its service account and needs RBAC to watch `healthmetrics` and patch their status.
