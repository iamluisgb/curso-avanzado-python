# Entornos Virtuales en Python

## 1. Fundamentos y Conceptos Esenciales

### 1.1 ¿Qué es un Entorno Virtual?

Un entorno virtual en Python es como tener una caja de herramientas independiente para cada proyecto. Imagina que eres un chef que trabaja en varios restaurantes diferentes. En cada restaurante, necesitas un conjunto específico de utensilios y ingredientes. No querrías mezclar los ingredientes de un restaurante italiano con los de un restaurante japonés. De la misma manera, un entorno virtual te permite mantener separadas las dependencias y paquetes de diferentes proyectos Python.

### 1.2 ¿Por qué son Necesarios?

Los entornos virtuales resuelven varios problemas comunes:

1. **Conflictos de Versiones**: Diferentes proyectos pueden necesitar diferentes versiones de las mismas bibliotecas.
2. **Aislamiento**: Evitan que los cambios en un proyecto afecten a otros.
3. **Reproducibilidad**: Facilitan la recreación exacta del entorno de desarrollo en otras máquinas.
4. **Limpieza**: Mantienen el sistema Python principal limpio y organizado.

### 1.3 Herramientas Principales

Existen varias herramientas para crear y gestionar entornos virtuales:

1. **venv**: Módulo incluido en Python 3 (recomendado)
2. **virtualenv**: Herramienta externa más antigua pero con más características
3. **conda**: Sistema completo de gestión de entornos (popular en ciencia de datos)

## 2. Código de Demostración

### 2.1 Ejemplo Básico: Creación y Uso de un Entorno Virtual

```bash
# Crear un nuevo entorno virtual
python -m venv mi_entorno

# Activar el entorno virtual
# En Windows:
mi_entorno\Scripts\activate
# En Unix o MacOS:
source mi_entorno/bin/activate

# Verificar la instalación de pip
pip list

# Instalar algunas dependencias
pip install requests pandas

# Crear requirements.txt
pip freeze > requirements.txt

# Desactivar el entorno
deactivate
```

## 3. Ejemplos Prácticos

### 3.1 Caso de Uso Real 1: Proyecto Web con Flask

```bash
# Crear y activar entorno
python -m venv entorno_flask
source entorno_flask/bin/activate  # o activate.bat en Windows

# Instalar dependencias
pip install flask flask-sqlalchemy pytest

# Crear estructura del proyecto
mkdir mi_proyecto
cd mi_proyecto

# Crear archivo de requerimientos
pip freeze > requirements.txt

# Crear archivo de ejemplo
cat > app.py << EOL
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola desde mi entorno virtual!'

if __name__ == '__main__':
    app.run(debug=True)
EOL

# Ejecutar aplicación
python app.py
```

### 3.2 Caso de Uso Real 2: Proyecto de Análisis de Datos

```bash
# Crear y activar entorno
python -m venv entorno_datos
source entorno_datos/bin/activate

# Instalar dependencias científicas
pip install numpy pandas matplotlib jupyter

# Crear notebook de ejemplo
jupyter notebook

# En el notebook:
import pandas as pd
import matplotlib.pyplot as plt

# Crear datos de ejemplo
data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

# Crear gráfico
plt.plot(data.x, data.y)
plt.title('Gráfico desde Entorno Virtual')
plt.show()
```

## 4. Ejercicios Propuestos

### 4.1 Nivel Básico
**Ejercicio 1: Configuración Básica**
* **Descripción**: Crear un entorno virtual e instalar dependencias básicas
* **Objetivo**: Familiarizarse con comandos básicos de entornos virtuales
* **Pasos**:
   1. Crear nuevo entorno virtual
   2. Activar el entorno
   3. Instalar tres paquetes diferentes
   4. Generar requirements.txt
   5. Desactivar el entorno

### 4.2 Nivel Intermedio
**Ejercicio 2: Migración de Entorno**
* **Descripción**: Recrear un entorno existente en otra ubicación
* **Objetivo**: Practicar la portabilidad de entornos virtuales
* **Pasos**:
   1. Crear entorno con dependencias específicas
   2. Exportar environment.yml o requirements.txt
   3. Recrear el entorno en otra carpeta
   4. Verificar que todo funcione igual

### 4.3 Nivel Avanzado
**Ejercicio 3: Gestión de Múltiples Entornos**
* **Descripción**: Crear y gestionar varios entornos para diferentes propósitos
* **Objetivo**: Manejar múltiples configuraciones de proyecto
* **Pasos**:
   1. Crear entornos para desarrollo, pruebas y producción
   2. Configurar diferentes dependencias en cada uno
   3. Crear scripts de automatización
   4. Documentar el proceso

## 5. Recursos Adicionales  

### Documentación oficial  
- [Python venv documentation](https://docs.python.org/3/library/venv.html)  
- [pip user guide](https://pip.pypa.io/en/stable/user_guide/)  

### Herramientas útiles  
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)  
- [pipenv](https://pipenv.pypa.io/en/latest/)  
- [poetry](https://python-poetry.org/)  

### Artículos recomendados  
- ["Python Dependency Management"](https://realpython.com/python-dependency-management/)  
 

## 6. Solución de Ejercicios

### Solución Ejercicio 1: Configuración Básica
```bash
# 1. Crear entorno virtual
python -m venv mi_primer_entorno

# 2. Activar el entorno
# Windows:
mi_primer_entorno\Scripts\activate
# Unix/MacOS:
source mi_primer_entorno/bin/activate

# 3. Instalar paquetes
pip install requests
pip install python-dotenv
pip install pytest

# 4. Generar requirements.txt
pip freeze > requirements.txt

# 5. Desactivar el entorno
deactivate

# Verificación
cat requirements.txt  # Debería mostrar los paquetes instalados
```

### Solución Ejercicio 2: Migración de Entorno
```bash
# 1. Crear primer entorno
python -m venv entorno_original
source entorno_original/bin/activate
pip install django djangorestframework pytest-django

# Guardar dependencias
pip freeze > requirements.txt

# 2. Crear script de verificación
cat > test_environment.py << EOL
import django
import rest_framework
import pytest

def test_imports():
    assert django.__version__
    assert rest_framework.__version__
    assert pytest.__version__
EOL

# 3. Crear nuevo entorno
python -m venv entorno_nuevo
source entorno_nuevo/bin/activate
pip install -r requirements.txt

# 4. Verificar instalación
python -m pytest test_environment.py
```

### Solución Ejercicio 3: Gestión de Múltiples Entornos
```bash
#!/bin/bash
# create_environments.sh

# Función para crear entorno
create_env() {
    ENV_NAME=$1
    REQUIREMENTS=$2
    
    echo "Creando entorno: $ENV_NAME"
    python -m venv $ENV_NAME
    
    # Activar entorno
    source $ENV_NAME/bin/activate
    
    # Instalar dependencias
    pip install -r $REQUIREMENTS
    
    # Generar requirements actual
    pip freeze > "${ENV_NAME}_requirements.txt"
    
    # Desactivar entorno
    deactivate
}

# Requirements para cada entorno
cat > dev_requirements.txt << EOL
django
djangorestframework
pytest
pytest-django
debug-toolbar
EOL

cat > test_requirements.txt << EOL
django
djangorestframework
pytest
pytest-django
coverage
EOL

cat > prod_requirements.txt << EOL
django
djangorestframework
gunicorn
psycopg2-binary
EOL

# Crear los entornos
create_env "env_dev" "dev_requirements.txt"
create_env "env_test" "test_requirements.txt"
create_env "env_prod" "prod_requirements.txt"

# Crear script de verificación
cat > verify_environments.py << EOL
import os
import subprocess

def check_environment(env_name):
    print(f"\nVerificando entorno: {env_name}")
    activate_script = os.path.join(env_name, 
        'Scripts' if os.name == 'nt' else 'bin', 
        'activate')
    
    # Listar paquetes instalados
    cmd = f"source {activate_script} && pip freeze"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)

environments = ['env_dev', 'env_test', 'env_prod']
for env in environments:
    check_environment(env)
EOL

# Ejecutar verificación
python verify_environments.py
```

### Documentación del Proyecto
```markdown
# Gestión de Entornos Virtuales

Este proyecto demuestra la gestión de múltiples entornos virtuales para diferentes
etapas de desarrollo.

## Estructura
- `env_dev/`: Entorno de desarrollo
- `env_test/`: Entorno de pruebas
- `env_prod/`: Entorno de producción

## Requisitos por Entorno

### Desarrollo
- Django con herramientas de debug
- Paquetes de prueba completos
- Herramientas de desarrollo

### Pruebas
- Django básico
- Herramientas de prueba y cobertura
- Sin herramientas de desarrollo

### Producción
- Django optimizado
- Servidor de producción (gunicorn)
- Dependencias de base de datos

## Uso

1. Crear entornos:
   ```bash
   ./create_environments.sh
   ```

2. Activar entorno específico:
   ```bash
   source env_dev/bin/activate  # Desarrollo
   source env_test/bin/activate # Pruebas
   source env_prod/bin/activate # Producción
   ```

3. Verificar instalación:
   ```bash
   python verify_environments.py
   ```
```

Estas soluciones demuestran:
1. Manejo básico de entornos virtuales
2. Automatización de tareas comunes
3. Documentación apropiada
4. Verificación de entornos
5. Buenas prácticas de gestión de dependencias

¿Te gustaría que profundizáramos en algún aspecto específico de las soluciones o que añadiéramos más ejemplos prácticos?