# Python starts here

Hola equipo, he creado este repositorio para realizar prácticas de programación con python.

Para utilizar este repositorio deberán clonarlo en su computadora (local),
utilizando el comando `git clone` y copiando la dirección SSH que pueden encontrar en el mismo repositorio.

Desde la terminal:

1. Clona el repositorio: `git clone git@github.com:qaton/python-skills.git`.
2. `cd python-skills` y `ls` para verificar que se hayan copiado los archivos.
3. Abre Pycharm y selecciona la carpeta para comenzar a trabajar.

Cada reto que vayas a resolver, podrás crear una nueva rama que llamarás por tu nombre o apodo, por ejemplo: `git checkout -b omar`. Con esto podremos identificar rápidamente el trabajo de cada persona.

Ahora sí, podrás entrar a los diferentes retos y comenzar a resolverlos, sin olvidar subir tus cambios al repositorio para que todos los podamos ver. Para subir tus cambios utiliza: `git push origin <el-nombre-de-tu-rama>`

Otros comandos útiles de Git:

* `git status` Visualiza el estado de los cambios.
* `git add <nombre-archivo>` Agrega los archivos para dar seguimiento.
* `git commit -m 'mensaje'` Guarda los cambios.
* `git pull origin <nombre-rama>` Trae los últimos cambios de la rama desde GitHub.

## Algunas recomendaciones para trabajar con Python

* Verifica que tienes los paquetes o módulos requeridos previamente instalados: `pip install...`.
* Recuerda que la identación es importante.
* Puedes generar un ambiente virtual con:

 `python3 -m venv venv` donde `-m` ejecuta el módulo del ambiente virtual y el segundo `venv` es el nombre del ambiente virtual (puede modificarse).

    * Activa el ambiente virtual con `source venv/bin/activate`.
    * `pip freeze`  Congela las librerías y sus versiones para saber cuáles tenemos instaladas.
    * `pip install -r requirements.txt` instala las dependencias utilizadas por el resto del equipo.
