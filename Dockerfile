FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

COPY src/ /app/src/



FROM gcr.io/distroless/python3-debian12

USER nonroot:nonroot

WORKDIR /app

COPY --from=builder --chown=nonroot:nonroot /root/.local/ /home/nonroot/.local/

COPY --from=builder --chown=nonroot:nonroot /app/src/ /app/src/

ENV PATH=/home/nonroot/.local/bin:$PATH

CMD ["/app/src/main.py"]
