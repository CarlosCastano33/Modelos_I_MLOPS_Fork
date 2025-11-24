#Versión de la imagen que se usará de Python
FROM python:3.12-slim

#Se crea el directorio de trabajo
WORKDIR /app

#Como docker se ejecuta en entorno linux, se debe instalar libgomp1, una dependencia necesaria para lightgbm
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 && \
    rm -rf /var/lib/apt/lists/*

#Se copian los scripts para entrenar y predecir, además del archivo que contiene las librerías necesarias
COPY requirements.txt ./

#Se instalan las librerías necesarias tomando su nombre desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Se copian los scripts para entrenar, predecir y el api rest
COPY train.py .
COPY predict.py .
COPY apirest.py .

# Copiar el dataset de entrenamiento
COPY train_dataset.csv .

#Se expone el puerto 5000 para el api rest
EXPOSE 5000

#Es el comando por defecto, es decir, si solo ponemos python y no el nombre del archivo a ejecutar, siempre se ejecutará el api rest por defecto
CMD ["python", "apirest.py"]