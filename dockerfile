FROM python:3.11-slim

# ==== Evitar arquivos cache ====
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ==== Diretório de trabalho ====
WORKDIR /app

# ==== Dependências do sistema ====
RUN apt-get update && apt-get install -y build-essential

# ==== Dependências Python ====
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ==== Código ====
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
