#Versión de la imagen que se usará de Python
FROM python:3.12-slim

#Se crea el directorio de trabajo
WORKDIR /app

#Como docker se ejecuta en entorno linux, se debe instalar libgomp1, una dependencia necesaria para lightgbm
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 && \
    rm -rf /var/lib/apt/lists/*

#Se copian los scripts para entrenar y predecir, además del archivo que contiene las librerías necesarias
COPY train.py predict.py ./
COPY requirements.txt ./

#Se instalan las librerías necesarias tomando su nombre desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Es el comando por defecto, es decir, si solo ponemos python y no el nombre del archivo a ejecutar, siempre se ejecutará el train por defecto
CMD ["python", "train.py"]