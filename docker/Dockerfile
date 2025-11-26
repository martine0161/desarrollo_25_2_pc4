FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir bandit pip-audit cyclonedx-bom

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY analysis/ ./analysis/
COPY scripts/ ./scripts/

RUN useradd -m -u 1000 scanner && chown -R scanner:scanner /app

USER scanner

CMD ["python", "app/main.py"]