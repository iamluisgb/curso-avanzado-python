# Objetivos de Aprendizaje

## Fundamentos del Testing en Python

### 1. Conceptos Básicos de Pruebas Unitarias
- Comprender la importancia del testing en el desarrollo de software
- Diferenciar entre tipos de pruebas: unitarias, integración, funcionales, rendimiento y aceptación
- Identificar las herramientas de testing disponibles en Python (UnitTest, PyTest, DocTest)
- Reconocer la importancia de la cobertura de código en el proceso de testing
- Implementar pruebas manuales y automatizadas para verificar la funcionalidad del código

### 2. Implementación con UnitTest
- Configurar correctamente el entorno de pruebas usando `unittest`
- Estructurar proyectos separando el código fuente de las pruebas
- Crear clases de prueba que hereden de `unittest.TestCase`
- Implementar métodos de configuración y limpieza con `setUp` y `tearDown`
- Aplicar diferentes tipos de aserciones para validar resultados esperados
- Manejar excepciones en pruebas usando `assertRaises`
- Validar diferentes tipos de datos como listas, diccionarios y conjuntos

### 3. Técnicas Avanzadas de Testing
- Controlar la ejecución de pruebas utilizando decoradores como `@skip`, `@skipIf` y `@expectedFailure`
- Organizar pruebas en suites para una mejor gestión
- Implementar pruebas parametrizadas usando `subTest`
- Aplicar mocking para simular comportamientos de APIs externas
- Utilizar side effects para probar diferentes escenarios con una misma función
- Implementar patching para modificar temporalmente el comportamiento de funciones y objetos

### 4. Herramientas Complementarias
- Documentar código y pruebas simultáneamente usando doctest
- Generar datos de prueba dinámicos con la biblioteca Faker
- Analizar la cobertura de pruebas con Coverage
- Integrar pruebas en sistemas de Continuous Integration con GitHub Actions
- Utilizar PyTest como alternativa a unittest
- Aprovechar herramientas de inteligencia artificial para generar pruebas unitarias