# Contribuir al Proyecto

¡Gracias por tu interés en contribuir! Siguiendo estas pautas, podremos garantizar que el proceso sea claro, colaborativo y beneficioso para todos.


## Contribuir con Código

1. Clona el repositorio.
2. Crea una rama propia (`add_nombre/funcion`).
3. Realiza tus cambios.

### Comandos para un mínimo orden

| Comando        | Descripción                        |
|----------------|------------------------------------|
| `git clone`    | Clona un repositorio.             |
| `git checkout` | Cambia a una rama específica.     |
| `git pull`     | Actualiza tu repositorio local.   |
| `git add nombre-del-archivo`     | Agrega un archivo específico al área de preparación.
|
| `git add .`                      | Agrega todos los archivos modificados al área de preparación. 
|
| `git commit -m "mensaje descriptivo"`        | Crea un commit con un mensaje que describe los cambios.  
|
| `git push origin nombre-rama`                | Sube los cambios al repositorio remoto en la rama actual.


## Como cerrar una issue 

--> Tres formatos posibles de cerrar la issue:
Closes #<número-de-issue>
Fixes #<número-de-issue>
Resolves #<número-de-issue>

Esto solo funciona si las palabras clave están en la descripción inicial del PR, no en los comentarios posteriores.

--> O desde la linea de comandos:
`gh issue close <número-de-issue>`

