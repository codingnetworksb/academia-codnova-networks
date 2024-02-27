# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo main.py al contenedor
COPY main.py .

# Copia el archivo .env.academia al contenedor
COPY .env.academia .

# Instala Uvicorn para ejecutar la aplicación FastAPI
RUN pip install uvicorn fastapi python-dotenv

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
