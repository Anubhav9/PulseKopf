FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd --create-home --uid 1000 pulsekopf && chown -R pulsekopf:pulsekopf /app
USER pulsekopf

ENTRYPOINT ["kopf", "run", "--standalone", "--all-namespaces", "controller/kopf_controller.py"]
