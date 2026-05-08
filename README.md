# Login Flask API - User Management System

Esta es una API REST robusta construida con **Flask** para la gestión de usuarios, autenticación y autorización mediante tokens JWT.

## 🚀 Características

- **Registro de Usuarios**: Creación de cuentas con contraseñas encriptadas.
- **Autenticación JWT**: Inicio de sesión seguro que devuelve un token de acceso.
- **Gestión de Perfil**: Acceso protegido a la información del usuario autenticado.
- **CRUD de Usuarios**: Listado, actualización y eliminación de usuarios (Rutas protegidas).
- **CORS Configurado**: Preparado para integrarse con frontends (Angular/React) en `localhost:4200`.
- **Base de Datos**: SQLite integrada para un despliegue rápido.

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3 & Flask
- **Base de Datos**: SQLAlchemy (ORM) & SQLite
- **Seguridad**: Flask-JWT-Extended & Werkzeug (Hashing)
- **CORS**: Flask-CORS

## 📋 Requisitos Previos

- Python 3.x instalado.
- Pip (gestor de paquetes de Python).

## 🔧 Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/byrosero/Login_flask.git
   cd Login_flask
   ```

2. **Crear un entorno virtual (Recomendado)**:
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install flask flask-sqlalchemy flask-jwt-extended flask-cors
   ```

4. **Ejecutar la aplicación**:
   ```bash
   python run.py
   ```
   La API estará disponible en `http://127.0.0.1:5000/`.

## 🛣️ Endpoints de la API

### Públicos
- `POST /register`: Registra un nuevo usuario.
- `POST /login`: Inicia sesión y devuelve el token JWT.

### Protegidos (Requieren Header `Authorization: Bearer <token>`)
- `GET /profile`: Obtiene la información del usuario actual.
- `GET /users`: Lista todos los usuarios registrados.
- `PUT /users/<id>`: Actualiza los datos de un usuario específico.
- `DELETE /users/<id>`: Elimina un usuario de la base de datos.

## 📂 Estructura del Proyecto

- `app/`: Directorio principal de la aplicación.
  - `models.py`: Definición de la tabla de Usuarios.
  - `routes.py`: Lógica de los endpoints y autenticación.
  - `templates/`: Plantilla HTML de documentación simple.
- `config.py`: Configuraciones de base de datos y llaves secretas.
- `run.py`: Punto de entrada para iniciar el servidor.

---
Desarrollado como una base sólida para sistemas de autenticación en Flask.
