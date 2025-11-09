**Introducción**

Es un proyecto en donde se busca realizar un preprocesamiento de un dataset de carros usados, para posteriormente realizar un modelo de predicción de precios de carros en base a sus características y condiciones de uso.

**Objetivo del proyecto**

Este proyecto tiene los siguientes objetivos:

* Aplicar el uso de Git y Github para la gestión de versiones en proyectos de ciencias de datos.
  
* Implementar un script en Python que nos permita utilizar la librería panda para realizar un preprocesamiento completo de datasets.

**Funcionalidades aplicadas**
* Funcionalidades aplicadas en Git y Github:
  * Creación de repositorio en Github.
  * Creación y configuración de un archivo .gitignore para evitar subir archivos innecesarios.
  * Crear un archivo README.md.
  * Clonar el repositorio remoto a local.
  * Configurar el usuario y correo electrónico.
  * Crear rama para desarrollar o experimentar sin afectar el código original.
  * Fusionar los cambios de la rama feature-preprocesamiento en main con un pull request.

* Funcionalidades aplicadas en el preprocesamiento:
  * Creación del script preprocesamiento.
  * Importar librerías y módulos necesarios para el preprocesamiento de datos, en este caso fueron pandas, sklearn con submódulo preprocessing.
  * Carga y mostrar las primeras filas del dataset.
  * Identificar y tratamiento de los valores nulos, duplicados.
  * Codificación de variables categóricas.
  * Normalización de los datos.

**Comandos Git Usados**

Entre los comandos Git usados tenemos:

__* git clone:__ Permite copiar un repositorio de una ubicación a otra.

__* git config --global user.name:__ Permite configurar el nombre de usuario para poder identificar el autor de los commits.

__* git config –global user.email:__ Permite configurar el correo para poder identificar el autor de los commits.

__* git checkout -b:__ Crea una nueva rama y cambia a ella automáticamente.

__* git add:__ Agrega los archivos modificados al área de preparación para el siguiente commit.

__* git commit -m:__ Permite poner un mensaje para describir lo realizado.

__* git push origin:__ Permite que los cambios en el repositorio local sean subidos al repositorio remoto.

__* git checkout:__ Permite cambiar a la rama de trabajo a otra.

__* git pull:__ Permite fusionar los cambios de una rama remota a una rama local.

__* git branch -d:__ Elimina una rama local que ya fue fusionada.

__* git push origin –delete:__ Elimina una rama remota del repositorio origin.


**Automatización** 

Se realizo un worflow para simular la revisión simulada de la fusión de feature preprocesamiento con main.
Para la creación del workflow se realizaron las siguientes acciones: 

* primero se creó los directorios \.github \workflows dentro del repositorio local preprocesamiento-ciencia-datos, para la creación de estos directorios utilice el comando mkdir de cmd.
* se creo un archivo simulate-review.yml dentro del directorio \.github \workflows el cual contiene la configuración de la acción automática para generar comentarios cada que se realice un pull request.
* con el comando git add se añadió los cambios realizados a la fila para el próximo commit.
* con el comando git commit -m se realiza un mensaje descriptivo sobre lo que se hizo.
* con el comando git push se aplican los cambios del repositorio local al repositorio remoto.

**Capturas de pantalla**

**Comandos ejecutados:**

<img width="719" height="276" alt="4" src="https://github.com/user-attachments/assets/1e1bc5b0-abc6-4a8c-bbe7-0f13c4b2e762" />

<img width="974" height="610" alt="5" src="https://github.com/user-attachments/assets/5dac9442-8381-43f9-a197-3eee4c76a256" />

<img width="953" height="553" alt="7" src="https://github.com/user-attachments/assets/b323de11-2f26-415b-8656-e467ededace9" />

<img width="769" height="558" alt="9" src="https://github.com/user-attachments/assets/f0e85d20-2823-4c29-a620-0630f61bdecb" />


**Pull request y fusión en GitHub:**

<img width="1237" height="592" alt="6" src="https://github.com/user-attachments/assets/5ae4b4dd-43fa-4512-bdbb-c3489b2719b2" />


**Ejecución exitosa de GitHub Actions:**

<img width="975" height="497" alt="8" src="https://github.com/user-attachments/assets/19fd691d-41ce-4007-b282-8c98b663c184" />



**Link Repositorio:**

https://github.com/JoseG9706/preprocesamiento-ciencia-datos.git 

