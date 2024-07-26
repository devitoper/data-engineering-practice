## Exercise #1 - Downloading Files with Python.

In this first exercise you will practice your Python skills,
as well as learn about a very common task ... downloading data files
from a `HTTP` source. 
You will have to unzip the files with Python as well.

## Ejercicio n.º 1: descarga de archivos con Python.
En este primer ejercicio practicarás tus habilidades con Python,
así como aprender sobre una tarea muy común... descargar archivos de datos
de una fuente `HTTP`.
También tendrás que descomprimir los archivos con Python.


#### Setup
1. Change directories at the command line 
   to be inside the `Exercise-1` folder `cd Exercises/Exercise-1`
   
2. Run `docker build --tag=exercise-1 .` to build the `Docker` image.

3. There is a file called `main.py` in the `Exercise-1` directory, this
is where you `Python` code to complete the exercise should go.
   
4. Once you have finished the project or want to test run your code,
   run the following command `docker-compose up run` from inside the `Exercises/Exercise-1` directory


#### Configuración
1. Cambiar directorios en la línea de comando
 estar dentro de la carpeta `Ejercicio-1` `cd Ejercicios/Ejercicio-1`

2. Ejecute `docker build --tag=exercise-1 .` para crear la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-1`, este
es donde debe ir el código `Python` para completar el ejercicio.

4. Una vez que haya terminado el proyecto o desee probar, ejecute su código,
 ejecute el siguiente comando `docker-compose up run` desde el interior del directorio `Ejercicios/Ejercicio-1`


#### Problems Statement
You need to download 10 files that are sitting at the following specified
`HTTP` urls. You will use the `Python` package `requests` to do this
work.

You will need to pull the filename from the download uri.

The files are `zip` files that will also need to be unzipped into 
their `csv` format.

They should be downloaded into a folder called `downloads` which
does not exist currently inside the `Exercise-1` folder. You should
use `Python` to create the directory, do not do it manually.

Generally, your script should do the following ...
1. create the directory `downloads` if it doesn't exist
2. download the files one by one.
3. split out the filename from the uri, so the file keeps its 
   original filename.
   
4. Each file is a `zip`, extract the `csv` from the `zip` and delete
the `zip` file.
5. For extra credit, download the files in an `async` manner using the 
   `Python` package `aiohttp`. Also try using `ThreadPoolExecutor` in 
   `Python` to download the files. Also write unit tests to improve your skills.


#### Declaración de problemas
Debe descargar 10 archivos que se encuentran en lo siguiente especificado
URL `HTTP`. Utilizará las `solicitudes` del paquete `Python` para hacer esto
trabajar.

Deberá extraer el nombre del archivo del uri de descarga.

Los archivos son archivos `zip` que también deberán descomprimirse
su formato `csv`.

Deben descargarse en una carpeta llamada "descargas" que
no existe actualmente dentro de la carpeta `Ejercicio-1`. Debería
use `Python` para crear el directorio, no lo haga manualmente.

Generalmente, su script debe hacer lo siguiente...
1. cree el directorio `descargas` si no existe
2. descargue los archivos uno por uno.
3. separe el nombre del archivo de la uri, para que el archivo mantenga su
 nombre de archivo original.

4. Cada archivo es un `zip`, extraiga el `csv` del `zip` y elimínelo.
el archivo `zip`.
5. Para obtener crédito adicional, descargue los archivos de forma "asincrónica" usando el
 Paquete `Python` `aiohttp`. También intente usar `ThreadPoolExecutor` en
 `Python` para descargar los archivos. También escriba pruebas unitarias para mejorar sus habilidades.


#### Download URIs are listed in the `main.py` file.

### Hints
1. Don't assume all the uri's are valid.
2. One approach would be the `Python` method `split()` to retrieve filename for uri,
or maybe find the last occurrence of `/` and take the rest of the string.


#### Los URI de descarga se enumeran en el archivo `main.py`.

### Consejos
1. No asuma que todos los uri son válidos.
2. Un enfoque sería el método `Python` `split()` para recuperar el nombre de archivo para uri,
o tal vez encontrar la última aparición de `/` y tomar el resto de la cadena.