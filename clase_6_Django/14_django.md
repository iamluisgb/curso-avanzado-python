# Django: Desarrollo Web con Python

## Introducción al Curso

A lo largo de las próximas sesiones, exploraremos cómo construir aplicaciones web robustas, escalables y seguras utilizando uno de los frameworks de desarrollo web más populares y potentes del ecosistema Python.

Para asegurar que todos aprendamos los fundamentos y mejores prácticas directamente de la fuente, seguiremos el tutorial oficial de Django, disponible en:

**[Tutorial oficial de Django](https://docs.djangoproject.com/es/stable/intro/tutorial01/)**

Este recurso, mantenido por la Django Software Foundation, es considerado la guía definitiva para iniciarse en el framework y cubre todos los conceptos fundamentales de manera estructurada y progresiva.

### Integración con GitLab y CI/CD

Como valor añadido a nuestro curso, implementaremos prácticas de desarrollo profesional mediante:

1. **Control de versiones con GitLab**: Todo el código que desarrollemos será versionado y almacenado en repositorios de GitLab. Esto nos permitirá:
   - Mantener un historial completo de cambios
   - Facilitar la colaboración en equipo
   - Implementar revisiones de código
   - Acceder a nuestro proyecto desde cualquier lugar

2. **Integración Continua (CI)**: Configuraremos pipelines de CI en GitLab para:
   - Ejecutar pruebas automáticamente con cada commit
   - Verificar el estilo y calidad del código (usando herramientas como flake8, black)
   - Detectar problemas tempranamente antes de llegar a producción
   - Generar informes de cobertura de pruebas

Estas prácticas reflejan los estándares de la industria y complementan perfectamente lo aprendido en el tutorial oficial, preparándote no solo para desarrollar con Django sino también para trabajar en entornos profesionales de desarrollo.

### ¿Por qué Django?

Django fue creado en 2003 por Adrian Holovaty y Simon Willison mientras trabajaban en un periódico. Necesitaban desarrollar aplicaciones web complejas rápidamente, con un código limpio y mantenible. Esta necesidad dio origen a un framework que sigue el principio "baterías incluidas" - ofreciendo casi todo lo que necesitas para desarrollar aplicaciones web sin depender de bibliotecas externas.

Las ventajas clave de Django incluyen:

* **Rapidez de desarrollo**: Reduce drásticamente el tiempo necesario para construir aplicaciones web
* **Seguridad integrada**: Protección contra vulnerabilidades comunes como SQL injection, XSS y CSRF
* **Escalabilidad**: Capaz de manejar desde pequeños sitios personales hasta aplicaciones con millones de usuarios
* **Versatilidad**: Utilizado en sitios de noticias, redes sociales, plataformas de comercio electrónico, aplicaciones científicas y más
* **Comunidad activa**: Amplia documentación, constantes actualizaciones y numerosos recursos de aprendizaje

### Estructura del Curso

Siguiendo el tutorial oficial, nuestro curso estará estructurado en seis partes principales:

1. **Configuración inicial y creación de proyecto**: Instalación de Django, configuración del entorno y creación de nuestro primer proyecto
2. **Models y administración**: Diseño de modelos de datos y utilización del sistema de administración automático
3. **Vistas y templates**: Creación de la interfaz de usuario y procesamiento de solicitudes
4. **Formularios y vistas genéricas**: Manejo de datos de usuario y optimización de código con vistas genéricas
5. **Testing**: Escritura de pruebas automatizadas para verificar la funcionalidad de nuestra aplicación
6. **Personalización avanzada**: Estilos CSS, archivos estáticos y optimización

A esta estructura, añadiremos sesiones específicas sobre:

7. **Configuración de GitLab y repositorios**: Creación de repositorio, estructura de branches y flujo de trabajo
8. **Implementación de CI/CD en GitLab**: Configuración de .gitlab-ci.yml para testing automático
9. **Despliegue continuo**: Automatización del despliegue en entornos de desarrollo, staging y producción

### Proyecto del Curso: Una Aplicación de Encuestas

Durante el curso, construiremos una aplicación de encuestas completamente funcional donde los usuarios podrán:
* Ver encuestas disponibles
* Votar en las encuestas
* Ver los resultados de las votaciones

Aunque pueda parecer sencilla, esta aplicación nos permitirá explorar todos los aspectos fundamentales de Django, incluyendo:
* Modelos para almacenar datos
* El panel de administración para gestionar contenido
* Vistas para procesar solicitudes
* Templates para renderizar páginas
* URLs para definir la estructura del sitio
* Forms para la entrada de datos
* Tests para garantizar la calidad del código

### Requisitos Previos

Para aprovechar al máximo este curso, es recomendable tener:
* Conocimientos básicos de Python
* Familiaridad con conceptos web básicos (HTTP, HTML, CSS)
* Un editor de código o IDE instalado (como VS Code, PyCharm, Sublime Text)
* Python 3.8 o superior instalado en tu sistema
* Una cuenta en GitLab (pueden crear una gratuita en gitlab.com)
* Git instalado en su sistema
