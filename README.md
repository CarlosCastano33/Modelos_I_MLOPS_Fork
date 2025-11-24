# Modelos_I_MLOPS
Proyecto sustituto realizado para el curso Modelos 1, o MLOPS. Universidad de Antioquia.

El [modelo seleccionado](https://www.kaggle.com/code/sanujisamarakoon/predict-the-customer-satisfaction-cse22) se desarrolló para la competencia de Kaggle [Predict the Customer Satisfaction - CSE 22](https://www.kaggle.com/competitions/Predict-the-Customer-Satisfaction-CSE-22), por el autor [sanujisamarakoon](https://www.kaggle.com/sanujisamarakoon).

### Integrantes
- Davidson Arley Pérez Jiménez - C.C. 1001738845
- Carlos Eduardo Castaño Garzón - C.C. 1039705379

# Instrucciones
- Clone el repositorio en su máquina.

### Para fase-1:
En esta fase se tendrá el notebook que realizará la carga, limpieza y preparación de los datos, además de utilizar el modelo tanto con los datos de train, como los de test para finalmente realizar las predicciones y generar el archivo con el formato predefinido en la competición.

- Cargue el archivo `app.ipynb` en Google Colaboratory.
- Cargue los archivos `sample_submission.csv`, `test_dataset.csv` y `train_dataset.csv` en la sesión **Files** del colab (justamente en la carpeta en la que se encuentra al abrir la sesión files, no los suba en otra ruta o la celda que carga los archivos no los encontrará).
- Ejecute celda por celda en orden, no se salte ninguna.
- Al finalizar la ejecución de todas las celdas, abra nuevamente la sesión **Files** del colab, podrá ver el archivo `submission.csv` con las predicciones finales, la última celda del notebook muestra este archivo.

### Para fase-2:
- Asegúrese de tener instalado Docker en su máquina y tener el servicio en ejecución.
- Estando dentro del directorio **fase-2** abra una terminal (o línea de comandos).
- Escriba y ejecute el comando `docker build -t fase_2 .` para crear la imagen que contendrá las librerías y los scripts `train.py` y `predict.py`.
- Sea paciente, el comando anterior construirá la imagen descargando e instalando las librerías necesarias.
- Luego de que se termine de crear la imagen puede verla con el comando `docker image ls`.
- Asegúrese de tener en el directorio **fase-2** un archivo csv llamado `train_dataset.csv` (siempre que vaya a usar nuevos datos de entrenamiento asígnele el mismo nombre al archivo).
- Escriba y ejecute el comando `docker run --rm --name fase_2_train -v "${PWD}:/app" fase_2 python train.py`, este comando creará el contenedor que ejecutará el entrenamiento del modelo predictivo. Fíjese que se escribe *--rm* en el comando, esto es ideal para cuando se quiera hacer un nuevo entrenamiento, ya que nos ahorrará el proceso de borrar el contenedor (con *--rm* se borra el contenedor al finalizar la ejecución) para volver ejecutar el train que generará el modelo entrenado.
- En caso de haber utilizado el símbolo del sistema (CMD), ejecutar el comando `docker run --rm --name fase_2_train -v "%cd%:/app" fase_2 python train.py`.
- Luego de que se realice el entrenamiento del modelo podrá ver un archivo llamado `model.pkl` que contendrá el modelo entrenado.
- Asegúrese de tener en el directiorio **fase-2** un archivo csv llamado `data.csv` (siempre que vaya a usar nuevos datos para realizar las predicciones asígnele el mismo nombre al archivo).
- Escriba y ejecute el comando `docker run --rm --name fase_2_predict -v "${PWD}:/app" fase_2 python predict.py`, este comando creará el contenedor que ejecutará las predicciones con base en los datos del archivo `data.csv`. Al igual que con la ejecución del train, este comando también usa *--rm* para eliminar el contenedor después de su ejecución, con el fin de evitar la eliminación manualmente cuando se vaya a predecir con datos nuevos.
- Ejecutar `docker run --rm --name fase_2_predict -v "%cd%:/app" fase_2 python predict.py` si estás en CMD.
- Luego de la ejecución del script de predicción, en la carpeta **fase-2** verá un nuevo archivo llamado `predictions.csv` que contendrá las predicciones realizadas por el modelo.

### Para fase-3:
- Asegúrese de tener instalado Docker en su máquina y tener el servicio en ejecución.
- Asegúrese de tener la librería "requests" dentro de su entorno, ejecutando el comando `pip install requests` con entorno virtual activado.
- Estando dentro del directorio **fase-3** abra una terminal (o línea de comandos).
- Escriba y ejecute el comando `docker build -t fase_3 .` para crear la imagen que contendrá las librerías y los scripts `train.py`, `predict.py` y `apirest.py`.
- Escriba y ejecute el comando `docker run -p 5000:5000 fase_3` para ejecutar el contenedor con el api rest y los scripts de entrenamiento y predicción.
- Abra otra terminal en el directorio **fase-3** con el entorno virtual activado.
- Escriba y ejecute el comando `python client.py`, el cual ejecutará el cliente que llamará a la api y a cada uno de los endpoints.
