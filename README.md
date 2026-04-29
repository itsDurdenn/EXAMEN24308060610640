# Gestor de Tareas

Nombre: Diaz Martinez Angel Joel
No. Control: 24308060610640
Grupo: 4-D
Especialidad: Programación
Fecha: 22 de abril de 2026

## Descripción del proyecto

Este proyecto es una pequeña aplicación web desarrollada con Flask que permite a un usuario registrarse, iniciar sesión y ver su perfil. Además, la interfaz incluye una tabla de tareas en la plantilla principal para mostrar un ejemplo de gestión de actividades.

La aplicación está pensada como un gestor de tareas ligero y básico, con una experiencia visual sencilla pero funcional usando Bootstrap para el estilo.

## Funcionalidades

- Registro de usuario con campos de nombre, email, edad, sexo, peso, altura y contraseña.
- Inicio de sesión que valida el correo y la contraseña con los datos registrados en la sesión.
- Perfil de usuario donde se muestra la información guardada.
- Tabla de tareas en la página principal para representar un ejemplo de actividades pendientes y estados.

## Tecnologías usadas

- Python
- Flask
- HTML
- Bootstrap

## Estructura del proyecto

- `app.py`: aplicación principal de Flask.
- `templates/`: carpeta con las plantillas HTML.
- `static/`: recursos estáticos como imágenes y estilos.

## Cómo ejecutar

1. Instala las dependencias de Flask.
2. Ejecuta `python app.py`.
3. Abre `http://127.0.0.1:5000/` en el navegador.

## Nota

El proyecto es un prototipo educativo y usa sesiones en memoria para guardar los datos de usuario. Para una aplicación real sería necesario agregar una base de datos y seguridad adicional.