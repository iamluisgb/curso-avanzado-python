## Introducción

En el curso básico hemos estudiado los fundamentos de Python: su sintaxis, las estructuras de control, las funciones y la parte básica de programación orientada a objetos. Estos conceptos son esenciales para cualquier programador y nos dan la base para seguiz avanzando.

Ahora es el momento de dar un paso más y enfrentarnos a desafíos más complejos. Aprender a escribir código Pythonico y profesional que nos permitirá resolver problemas de una forma más eficiente y limpia y además , nos abrirá las puertas a proyectos más ambiciosos y demandantes.

## Codigo Pythonico

El **código pythonico** es aquel que sigue las convenciones y principios de Python, aprovechando sus características para escribir código más limpio, legible y eficiente. Se basa en la filosofía del lenguaje, expresada en el **Zen de Python** (PEP 20), que promueve la simplicidad, la claridad y la elegancia.

### Características del código pythonico:

1. **Legible y claro** → Usa nombres descriptivos, sigue PEP 8 y evita complejidad innecesaria.
2. **Aprovecha las características de Python** → Usa listas por comprensión, `zip()`, `enumerate()`, `with` para manejar archivos, etc.
3. **Evita reinventar la rueda** → Utiliza bibliotecas estándar en lugar de escribir funciones desde cero.
4. **Prefiere EAFP (Easier to Ask for Forgiveness than Permission)** → Manejo de excepciones en lugar de comprobaciones innecesarias.
5. **Uso correcto de estructuras de datos** → `dict`, `set`, `tuple` según el caso.

### Ejemplo de código no pythonico vs. pythonico:

❌ **No pythonico (verbose y poco eficiente)**:

```python
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)

```

✅ **Pythonico (usando list comprehension)**:

```python
squared = [num ** 2 for num in numbers]

```

### ¿Por qué es importante?

- Hace el código más fácil de leer y mantener.
- Facilita la colaboración con otros desarrolladores.
- Aprovecha mejor las capacidades del lenguaje.
- Reduce la cantidad de código repetitivo o innecesario.

## **PEP de python**

Las **PEP (Python Enhancement Proposals)** son documentos de mejora de Python que proponen nuevas características, explican decisiones de diseño o proporcionan información sobre las mejores prácticas en el lenguaje.

Algunas de las PEP más conocidas son:

- **PEP 8**: Guía de estilo para escribir código Python limpio y legible.
- **PEP 20**: "El Zen de Python", que define la filosofía del lenguaje.
- **PEP 257**: Reglas para escribir docstrings en Python.
- **PEP 484**: Anotaciones de tipo en Python.
- **PEP 572**: Operador de asignación `:=` (el "walrus operator").

Son mantenidas por la comunidad de Python y pueden ser aceptadas, rechazadas o retiradas.

### Pip en Python

**pip** (Python Package Installer) es el gestor de paquetes de Python. Permite instalar, actualizar y desinstalar bibliotecas y módulos de manera sencilla desde el **Python Package Index (PyPI)**.

### Ejemplos de uso:

- Instalar un paquete:

    ```bash
    pip install requests

    ```

- Actualizar un paquete:

    ```bash
    pip install --upgrade numpy

    ```

- Desinstalar un paquete:

    ```bash
    pip uninstall pandas

    ```

- Listar paquetes instalados:

    ```bash
    pip list

    ```
