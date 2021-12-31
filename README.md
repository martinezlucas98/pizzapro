# PizzaPro 🍕
Prueba para candidatos a desarrollador backend en TDP S.A.


## Instalación 💾
> Se recomienda trabajar en un entorno virtual

La instalación es bastante sencilla:
1. Clonar (o descargar) el repositorio.
2. Abrir el directorio/archivo.
3. Instalar las dependencias encontradas en el archivo [requirements.txt](requirements.txt). Puede instalarlo ejecutando en la consola: ```pip install -r requirements.txt```
4. Desplazarse al directorio pizzaProject: ```cd pizzaProject```
5. Ejecutar en la consola el servidor a través del siguiente comando: ```python manage.py runserver```. Esto ejecutará la aplicación por defecto en http://127.0.0.1:8000/
6. Con el servidor ejecutandose, ya podemos realizar consultas a los endpoints (siempre y cuando este se mantenga en ejecución). Para ello puede utilizar Postman junto con el archivo de prueba disponible. Más información sobre Postman y el archivo de prueba a continuación.


## Prueba: Postman 👨🏼‍🚀
> Si no cuenta con Postman instalado puede descargarlo desde [su página oficial.](https://www.postman.com/downloads/)

Lo primero que se debe hacer para poder probar los endpoints es importar el archivo [Pizzeria.postman_collection.json](Pizzeria.postman_collection.json) a su Postman:

1. Abrir/Ejecutar Postman
2. Seleccionar el botón de **Importar** ubicado en la esquina superior izquierda.
3. Seleccionar el archivo Pizzeria.postman_collection.json

Para más detalles puede ver [este video](multimedia/postman_import.mp4) guía.

Luego debemos asignar algunas variables globales. Esto es debido a que utilizamos estas variables para almacenar los tokens de autenticación (token básico de django y JWT) ya que son necesarios para acceder a ciertos endpoints.

Los pasos son:
1. Click en el botón con forma de ojo en la esquina superior derecha.
2. Click en **Agregar** (el que se encuentra al lado de **Globales**)
3. Agregamos en la columna **Variables** la palabra ```jwt_access``` y en la columna del **Valor Actual** escribimos: ```Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwOTUyMjcwLCJpYXQiOjE2NDA5MzA2NzAsImp0aSI6IjVkNjQ3NDU1MzNkNjRkODI4YWUwOGJiZTc2YWRlYTRhIiwidXNlcl9pZCI6Mn0.5PwScJSQ3NhI0SnIgpMKP95T_iroNGNRT-ApmUyJK_g``` un token JWT válido.
4. Ahora hacemos lo misma para el token básico de Django.  Agregamos en la columna **Variables** la palabra ```basic_token``` y en la columna del **Valor Actual** escribimos: ```Token c257a92dac54640a7048e215f78dd36205c7a954``` un token válido.

Debe quedar de la siguiente manera:
![Imagen de ejemplo](multimedia/variables.png)

Si esos tokens ya no son válidos, usted puede obtener los nuevos tokens por medio de las consultas POST ```Get JWT for user``` (el access token) y ```Get Django basic token for user``` respectivamente. Aquí debe proveer el nombre de usuario y la contraseña en los campos del cuerpo de la consulta.

Recuerde agregar las palabras Bearer y Token respectivamente antes del propio token.

Si tiene alguna duda sobre los pasos a realizar para configurar las variables, puede consultar nuestro [video guía](multimedia/tokens.mp4) de tutorial.

Una vez que cuente con los tokens ya puede empezar a realizar las diferentes consultas a los endpoints!!✨

Para activar, desactivar o alternar un token (es decir si quiere usarlo o no) simplemente puede desmarcarlo en el apartado de **Cabeceras** de una consulta en Postman. Ahí podrá ver los tokens que recién fueron mencionados pero **OJO**, solo puede tener activado uno u otro, no ambos al mismo tiempo o no se reconocerá la autenticación.


## Endpoints 🚪
| Endpoint                                            | Verbo&nbsp;HTTP&nbsp; | Parametros | Descripción |
|---------------------------------------------------------|:----------:|------------|-------------|
| /basic-token-auth/                                      | POST       | username :: tipo String <br/> password :: tipo String| Devuelve el token Django de autenticación del usuario cuyas credenciales fueron proveidas (en caso de que sean correctas).|
| /api/token/                                             | POST       | username :: tipo String <br/> password :: tipo String| Devuelve el JWT de autenticación del usuario cuyas credenciales fueron proveidas (en caso de que sean correctas).|
| /api/pizza/                                             | POST       | id :: tipo String<br/> nombre :: tipo String<br/> precio :: tipo Int<br/> activo:: tipo Boolean| Crea una nueva pizza. Se necesita ser usuario staff o superuser.|
| /api/pizza/`<id>`                                       | PATCH      | nombre :: tipo String<br/> precio :: tipo Int<br/> activo :: tipo Boolean| Modifica la pizza cuyo id es `<id>`. Se necesita ser usuario staff o superuser.|
| /api/pizza/                                             | GET        | - | Devuelve todas las pizzas activas. Si el usuario es staff o superuser, también devuelve las no activas.|
| /api/ingrediente/                                       | POST       | id :: tipo String<br/> nombre :: tipo String<br/> categoria :: tipo String (Dos opciones disponibles: BASISCO y PREMIUM)| Agrega un nuevo ingrediente. Se necesita ser usuario staff o superuser.|
| /api/ingrediente/`<id>`                                 | DEL        | - | Elimina un ingrediente si no hay ninguna pizza que lo utilice. Se necesita ser usuario staff o superuser.|
| /api/ingrediente/`<id>`                                 | PATCH      | categoria :: tipo String (Dos opciones disponibles: BASISCO y PREMIUM)<br/> nombre :: tipo String| Modifica el ingrediente cuyo id es `<id>`. Se necesita ser usuario staff o superuser.|
| /api/ingrediente/                                       | GET        | - | Devuelve la lista de ingredientes.|
| /api/ingrediente-x-pizza/                               | POST       | pizza :: tipo String <br/> ingrediente :: tipo String| Permite agregar un ingrediente a una pizza. El parametro `pizza` representa el id de esta, y el parametro `ingrediente` el ingrediente para agregarle.|
| /api/ingrediente-x-pizza/`<pizza_id>`/`<ingrediente_id>`| DEL      | - | Permite quitar el ingrediente (con id igual a `<ingrediente_id>`) de la pizza (con id igual a `<pizza_id>`).|
| /api/pizza-detalle/`<id>`                               | GET        | - | Permite ver el "detalle" (id, nombre, precio, activo, ingredientes) de la pizza con id igual a `<id>`|


## Usuarios 👨🏽‍💻

### Superuser
> username: admin
> 
> password: pizza

### Staff user
>username: worker
>
>password: pizzaWorker123