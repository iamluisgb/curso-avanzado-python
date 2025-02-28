# 🔹 Fundamentos del Testing en Python

# ¿Qué son las Pruebas Unitarias y por qué es importante?

Probar software no solo es una tarea técnica, es un proceso crítico que puede marcar la diferencia entre el éxito o el fracaso de un proyecto. Un pequeño error no detectado puede causar grandes problemas, como lo demuestra el caso del cohete de la Agencia Espacial Europea en 1996. Afortunadamente, en el desarrollo de software contamos con herramientas como Python y sus módulos para asegurar la calidad del código antes de que llegue a los usuarios.

## **¿Qué tipos de pruebas son necesarias para asegurar la calidad del software?**

- **Pruebas unitarias:** Se encargan de validar que cada componente pequeño del código funcione correctamente de manera aislada.
- **Pruebas de integración:** Verifican que los distintos componentes trabajen bien en conjunto, evitando problemas en la interacción de partes.
- **Pruebas funcionales:** Validan que el sistema en su totalidad funcione como se espera según los requisitos.
- **Pruebas de rendimiento:** Aseguran que el software sea rápido y eficiente, evaluando su comportamiento bajo diferentes condiciones de carga.
- **Pruebas de aceptación:** Determinan si el software cumple con las expectativas del usuario final.


## **¿Qué herramientas de testing ofrece Python?**

- **UnitTest:** Permite crear pruebas unitarias de manera sencilla, asegurando que todas las partes del código realicen su función correctamente.
- **PyTest:** Facilita la creación de pruebas con una configuración avanzada para cubrir diferentes escenarios.
- **DocTest:** Integra pruebas directamente en los comentarios de las funciones, permitiendo validar el código mientras se mantiene la documentación.

## **¿Cómo garantizar que todas las líneas de código están siendo probadas?**

Es crucial identificar las líneas de código que no están cubiertas por pruebas. Para esto, existe **Coverage**, una herramienta que genera un reporte en HTML mostrando qué partes del código no han sido validadas, lo que permite agregar pruebas adicionales donde sea necesario.

## **¿Por qué es importante el testing en software?**

El testing asegura que el software sea funcional, rápido y confiable, pero más allá de eso, puede evitar costosos errores, pérdidas financieras y en casos extremos, salvar vidas. Al probar el software antes de que llegue a producción, los desarrolladores tienen la ventaja de corregir fallos antes de que impacten a los usuarios.

# ¿Qué es el Testing en Software?

Las pruebas en el desarrollo de software son esenciales para garantizar la calidad y estabilidad del código antes de lanzarlo a producción. Tanto las pruebas manuales como las automatizadas juegan un rol fundamental para detectar errores. Usar Python para automatizar estas pruebas no solo ahorra tiempo, sino que también asegura que los errores críticos se detecten antes, evitando posibles pérdidas económicas y de confianza de los usuarios.

## **¿Qué son las pruebas manuales y cómo funcionan?**

Las pruebas manuales consisten en validar el funcionamiento de un cambio en el código mediante la interacción directa con la aplicación. Esto se hace, por ejemplo, al modificar una línea de código, ejecutar la aplicación y verificar si el cambio funciona correctamente. Es similar al trabajo de un mecánico que ajusta un auto y luego lo prueba encendiéndolo cada vez.

## **¿Cómo funcionan las pruebas unitarias?**

Las pruebas unitarias permiten validar que pequeñas piezas de código, como funciones individuales, trabajan correctamente. En el ejemplo de un mecánico, esto sería como revisar solo un neumático: inflarlo, verificar que no tenga fugas y confirmar que esté en buen estado. En Python, estas pruebas se automatizan utilizando la palabra clave `assert`, que compara los resultados esperados con los reales.

## **¿Qué son las pruebas de integración?**

Las pruebas de integración verifican que diferentes componentes de la aplicación funcionen en conjunto sin problemas. En el caso del mecánico, sería comprobar que el neumático instalado en el coche funcione bien con el resto de las piezas del vehículo. En desarrollo de software, esto se traduce a verificar, por ejemplo, que el proceso de inicio de sesión funcione correctamente, desde la entrada del usuario hasta la confirmación del acceso.

## **¿Cómo Python nos ayuda a automatizar pruebas?**

Python ofrece herramientas para automatizar las pruebas, permitiendo ejecutar muchas validaciones rápidamente sin intervención manual. A través de pruebas automatizadas, podemos detectar errores que de otro modo podrían pasar desapercibidos y llegar a producción, como un fallo en el cálculo de una orden de compra. Esto es crítico para evitar situaciones como la que enfrentó CrowdStrike, donde un error no detectado en una actualización paralizó aeropuertos.

```python
#tests.py
def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products) == 12

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
```

# Instalación y Configuración del Entorno de Pruebas

La creación de funciones y pruebas para el código que se va a producción es clave para validar resultados correctamente. En Python, el uso de Unit Testing simplifica este proceso, permitiendo automatizar pruebas y hacerlas más legibles y eficientes, además de integrarse fácilmente con sistemas de Continuous Integration.

### **¿Cómo mejorar la legibilidad de las pruebas con Unit Testing?**

Python incluye Unit Testing de forma nativa, proporcionando clases reutilizables para ejecutar pruebas de manera automática o manual. Esta herramienta no solo permite mejorar la legibilidad, sino también identificar y solucionar errores rápidamente, sin necesidad de depender de `print` para verificar si las pruebas se están ejecutando.

### **¿Cómo estructurar un proyecto de testing en Python?**

1. **Separación de código y pruebas:** Coloca el código fuente en una carpeta `src` y las pruebas en una carpeta `test`.
2. **Entorno virtual:** Crea un entorno virtual para aislar dependencias del proyecto. Esto se hace con `python -m venv env`  , lo que genera una carpeta con binarios y librerías solo para el proyec
3. **Uso de gitignore:** Añade un archivo `.gitignore` para evitar que el entorno virtual y otros archivos no deseados se suban al repositorio.

### **¿Cómo escribir y ejecutar pruebas con Unit Test?**

Para escribir pruebas, sigue estas buenas prácticas:

- Crea un archivo de pruebas, como `test_calculator.py`, y empieza importando Unit Test.
- Define clases que hereden de `unittest.TestCase`.
- Escribe métodos de prueba que validen funciones específicas usando `assertEqual` para verificar resultados.

Ejemplo básico de prueba:

```python
#src/calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

```

```python
#test/test_calculator.py
import unittest
from src.calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

```

Ejecuta las pruebas con `python -m unittest discover` para que Unit Testing encuentre y ejecute las pruebas automáticamente. En nuestro caso: `python -m unittest discover -s test`

### **¿Qué hacer cuando una prueba falla?**

Si una prueba falla, Unittest lo indica con una “F”, mostrando el error detallado, lo que facilita la depuración. Puedes forzar un fallo, por ejemplo, esperando que la suma de `2 + 3` sea `6` en lugar de `5`, para ver cómo se comporta

## 🚀 Reto

Agrega multiplicación y división a calculadora y agrega pruebas unitarias, considera casos específicos como la división entre 0. 

https://github.com/platzi/python-testing/tree/2d5ac48dbcf401758ac0786befe0280cbb2015d2

# 🔹 Conceptos Básicos de Unittest

# Cómo Crear Pruebas Unitarias con UnitTest en Python

Las pruebas unitarias en Python son esenciales para asegurar el correcto funcionamiento del código. Utilizando la clase `TestCase` de la biblioteca `UnitTest`, podemos estructurar pruebas de manera eficiente y limpiar recursos una vez que se han ejecutado. Además, permite automatizar la validación de resultados y la captura de errores. Vamos a profundizar en cómo implementar estas pruebas y algunos métodos clave que facilitan este proceso.

## **¿Cómo configurar las pruebas en Python con TestCase?**

El método `setUp()` nos permite configurar elementos antes de que cada prueba se ejecute. Imagina que tienes cinco pruebas que requieren la misma preparación: en lugar de repetir la configuración, puedes ejecutarla una sola vez aquí. Esto ahorra tiempo y esfuerzo al evitar la duplicación de código.

Por ejemplo:

- Puedes utilizar `setUp()` para crear una base común de datos, abrir archivos, o preparar datos de entrada.
- Luego, cada prueba reutiliza esta configuración, asegurando que el entorno siempre esté listo para las pruebas.

## **¿Cómo limpiar después de una prueba?**

El método `tearDown()` sirve para limpiar los recursos utilizados en la prueba. Supongamos que has creado cientos de archivos para una prueba, este método permite eliminarlos automáticamente después de que la prueba finaliza, asegurando que el sistema no quede lleno de datos innecesarios.

Algunos ejemplos de cuándo usarlo:

- Eliminar archivos temporales creados durante las pruebas.
- Cerrar conexiones a bases de datos o liberar recursos del sistema.

## **¿Cómo ejecutar pruebas y capturar errores?**

La clase `TestCase` no solo organiza las pruebas, también proporciona un método automático para ejecutar cada una de ellas. El método `runTest()` gestiona la ejecución de las pruebas, captura los errores y valida que todo funcione correctamente. Este proceso automatiza la validación de resultados esperados y la identificación de fallos.

Por ejemplo:

- Si tienes una lista de pruebas, este método las ejecutará una por una, asegurando que todas se validen correctamente.
- Además, capturará las excepciones que se lancen durante la ejecución.

## **¿Cómo validar excepciones en las pruebas unitarias?**

Una situación común en las pruebas de una calculadora es manejar la división por cero. La mejor práctica es lanzar una excepción para evitar errores. Python permite validar que la excepción se ha lanzado correctamente en las pruebas.

Pasos clave:

- Crear una prueba donde `b = 0`.
- Utilizar `assertRaises()` para verificar que se ha lanzado la excepción `ValueError`.

# Cómo usar el método setup en tests de Python

El uso del método `setup` en los tests permite simplificar y evitar la duplicación de código en las pruebas. Al iniciar un test, `setup` se ejecuta automáticamente, preparando el entorno para cada prueba de forma eficiente. En este caso, pasamos de un proyecto de calculadora a uno de una cuenta bancaria, y veremos cómo implementar pruebas unitarias para depósitos, retiros y consultas de saldo utilizando `setup` para optimizar el código.

```python
#src/bank_account.py
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
```

## **¿Cómo implementar pruebas para depósitos en una cuenta bancaria?**

Primero, se crea la clase de test donde se probarán los métodos de una cuenta bancaria. Para hacer un depósito, se debe instanciar una cuenta con un saldo inicial, realizar el depósito y luego validar que el saldo ha cambiado correctamente.

Pasos:

- Crear el archivo `test_bank_account.py`.
- Instanciar una cuenta con saldo inicial.
- Probar que el método de depósito ajusta el saldo correctamente.

![image.png](attachment:960de2c0-a58e-4294-89d9-eb9cf2a9faf8:image.png)

## **¿Cómo optimizar las pruebas con el método setup?**

El método `setup` evita la creación repetitiva de instancias en cada test. Para lograr esto:

- Se crea una instancia de cuenta en `setup`.
- La cuenta creada se comparte entre todas las pruebas usando `self`.

Esto simplifica las pruebas al evitar duplicar el código de instanciación en cada método de test.

## **¿Cómo ejecutar las pruebas de retiro y consulta de saldo?**

Para las pruebas de retiro y consulta de saldo:

- El método `withdraw` debe restar la cantidad del saldo y validar que el resultado sea correcto.
- El método `get_balance` simplemente valida que el saldo actual coincida con lo esperado.

Estas pruebas se benefician del uso de `setup`, ya que reutilizan la misma instancia de cuenta creada para cada prueba.

## **¿Cómo ejecutar pruebas con salida más detallada?**

Al ejecutar las pruebas, es útil utilizar el comando con la opción `-b` para obtener una salida más detallada y visualizar exactamente qué pruebas se están ejecutando y dónde están ubicadas en el código. Esto ayuda a depurar y tener un mejor control sobre el flujo de las pruebas.

```python
import unittest

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800
    
    def test_get_balance(self):
        assert self.account.get_balance() == 1000
```

## 🚀 Reto. **¿Cómo crear pruebas para una nueva funcionalidad de transferencia?**

La tarea final consiste en agregar un método de transferencia a la clase `BankAccount`, el cual debe:

- Permitir transferir saldo entre cuentas.
- Levantar una excepción si el saldo no es suficiente para realizar la transferencia.

Luego, se deben crear dos pruebas unitarias:

1. Validar que la transferencia se realiza correctamente.
2. Validar que se lanza una excepción cuando no hay saldo suficiente para completar la transferencia.

```python
#src/bank_account.py
class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance

        raise ValueError("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance

        raise ValueError("Invalid withdraw amount")

    def get_balance(self):
        return self.balance

    def transfer(self, account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            account.deposit(amount)
            return self.balance

        raise ValueError("Invalid transfer amount")

#tests/test_bank_account.py

from unittest import TestCase

from src.BankAccount import BankAccount

class BankAccountTests(TestCase):
    def setUp(self):
        self.account = BankAccount(1000)

    def test_deposit(self):
        self.account.deposit(500)
        assert self.account.get_balance() == 1500

    def test_withdraw(self):
        self.account.withdraw(500)
        assert self.account.get_balance() == 500

    def test_withdraw_fail(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transfer(self):
        account2 = BankAccount(500)
        self.account.transfer(account2, 500)
        assert self.account.get_balance() == 500
        assert account2.get_balance() == 1000

    def test_transfer_fail(self):
        with self.assertRaises(ValueError):
            account2 = BankAccount(500)
            self.account.transfer(account2, 2000)
```

# Uso de tearDown para limpieza de Pruebas Unitarias en Python

El método `teardown` es esencial para asegurar que nuestras pruebas no interfieran entre sí, y se usa para limpiar cualquier recurso temporal al final de cada prueba. En este caso, lo hemos aplicado a nuestra cuenta bancaria, donde se registra un log cada vez que se realiza una acción. Vamos a explorar cómo implementarlo correctamente y agregar funcionalidades de logging a nuestra cuenta de banco.

## **¿Qué es el método teardown y cuándo lo usamos?**

El método `teardown` se ejecuta al final de cada prueba, y es utilizado para limpiar recursos como archivos temporales o cerrar conexiones. En este caso, lo usamos para eliminar el archivo de logs que se genera durante nuestras pruebas de la cuenta bancaria. De esta manera, cada prueba se ejecuta en un entorno limpio, sin interferencias de pruebas anteriores.

## **¿Cómo agregamos logging a la cuenta de banco?**

Añadimos una funcionalidad de logging en el método `init`, el cual se ejecuta cada vez que se crea una instancia de nuestra clase `BankAccount`. El log incluye eventos como la creación de la cuenta, la consulta de saldo, y cuando se realizan depósitos o retiros. Esto se realiza a través del método `logTransaction`, que escribe el mensaje en un archivo de texto.

- Se define un archivo de log (`logFile`) al crear la cuenta.
- Cada vez que se realiza una transacción o se consulta el saldo, se agrega una línea al archivo.
- Para asegurar que el archivo de log se genera correctamente, creamos pruebas automatizadas.

```python
#src/bank_account.py
class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
```

## **¿Cómo validamos la existencia del archivo de log?**

En nuestras pruebas, verificamos si el archivo de log se crea exitosamente. Utilizamos la función `os.path.exists` para validar su existencia y asegurarnos de que nuestras pruebas están funcionando correctamente.

```python
    #tests/test_bank_account.py
    def test_transaction_log(self):
        self.account.deposit(500)
        assert os.path.exists("transaction_log.txt")

```

## **¿Cómo usamos el teardown para limpiar archivos?**

El `teardown` nos permite eliminar el archivo de log después de cada prueba para que no interfiera con otras. Implementamos una función que, si el archivo existe, lo borra utilizando `os.remove`. Esto asegura que las pruebas se ejecutan en un entorno limpio y los logs no se acumulan entre pruebas.

```python
#tests/test_bank_account.py
def tearDown(self) -> None:
    if os.path.exists(self.account.log_file):
        os.remove(self.account.log_file)

```

## **¿Cómo probamos que los logs contienen la información correcta?**

Además de verificar que el archivo existe, es fundamental asegurarnos de que el contenido del archivo sea correcto. Para ello, creamos un método que cuenta las líneas del archivo (`countLines`). Luego, en nuestras pruebas, validamos que el número de líneas corresponde al número de transacciones realizadas.

- Contamos las líneas después de crear la cuenta (debe haber una línea).
- Hacemos un depósito y volvemos a contar las líneas (debe haber dos líneas).
- Si no limpiáramos el archivo con `teardown`, el número de líneas sería incorrecto.

```python
#tests/test_bank_account.py
import unittest, os

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename): # al no empezar por test testcase no lo reconoce como test
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transaction_log(self):
        self.account.deposit(500)
        assert os.path.exists("transaction_log.txt")

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
```

## 🚀 Reto. **¿Cómo crear una nueva funcionalidad de logging para transferencias fallidas?**

El siguiente reto es agregar una funcionalidad para registrar un log cuando alguien intente hacer una transferencia sin saldo disponible. El log debe incluir un mensaje indicando la falta de fondos, y también se deben crear pruebas que validen que este log se genera correctamente.

- Se debe registrar el intento fallido en el archivo de log.
- Crear una prueba para asegurarse de que el mensaje “No tiene saldo disponible” aparece en el log.
- Utilizar `teardown` para limpiar el archivo al finalizar cada prueba.

```python
# src/bank_account.py
class BankAccount:
    def __init__(self, balance = 0, log_file = None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self,message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Cantidad depositada {amount}. Nuevo balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Retiro {amount}. Nuevo balance: {self.balance}")
        return self.balance
    
    def transfer(self, amount, target_account):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            self._log_transaction(f"Transferencia de {amount} realizada con éxito. Nuevo balance: {self.balance}")
        else:
            error_message = f"Transferencia fallida por monto {amount}. Saldo disponible {self.balance}"
            self._log_transaction(error_message)
            raise ValueError("No tiene saldo disponible")
        return self.balance
        

    def get_balance(self):
        self._log_transaction(f"Revision de balance. Balance actual {self.balance}")
        return self.balance

# test/bank_account.py
import unittest
import os

from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.account = BankAccount(balance = 1000, log_file = "transaction_log.txt")
        self.target_account = BankAccount(balance=500)

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
            
    def _count_lines(self, filename):
        with open(filename, "r") as f:
		            return len(f.readlines())
		        
		def _log_contains(self, message):
			with open(self.log_file, "r") as f:
			  return any(message in line for line in f.readlines())
		
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500
    
    def test_withdraw(self):
        new_balance = self.account.withdraw(500)
        assert new_balance == 500
    
    def test_transfer(self):
        self.account.transfer(20000, self.target_account)
        self.assertEqual(self.account.get_balance(), 800)
        self.assertEqual(self.target_account.get_balance(), 700)
 
    def test_transfer_fails_insufficient_funds(self):
		    with self.assertRaises(ValueError):
		      self.account.transfer(20000, self.target_account)

        self.assertTrue(self._log_contains("Transferencia fallida por monto 20000"))

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transaction_log(self):
        self.account.deposit(500)
        assert os.path.exists("transaction_log.txt")
    
    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
```

# Cómo validar excepciones y estructuras de datos con Unittest en Python

UnitTest nos proporciona una amplia gama de métodos de aserción que mejoran la forma en que validamos nuestras pruebas. En esta clase, hemos explorado algunos de ellos y cómo utilizarlos en diferentes escenarios.

## **¿Cómo se usa el assertEqual en Unit Test?**

El método `assertEqual` compara dos valores para verificar si son iguales. Acepta dos parámetros para comparar y opcionalmente un mensaje personalizado que se mostrará en la terminal si la prueba falla. Este método se integra bien con los editores, permitiendo ejecutar y depurar pruebas de manera eficiente.

- Parámetros: valor esperado, valor obtenido, mensaje de error (opcional)
- Uso típico: Validar igualdad de números, cadenas, o cualquier otro objeto comparable.

```python
#tests/test_bank_account.py
import unittest, os

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
```

## **¿Qué otros métodos de aserción existen en Unit Test?**

Además de `assertEqual`, Unit Test incluye muchos otros métodos de aserción útiles:

- `assertTrue`: Verifica que una expresión sea verdadera. No compara valores, solo evalúa si una condición es cierta.
- `assertRaises`: Valida que se lance una excepción específica dentro de un bloque de código, utilizando la palabra clave `with` como contexto.
- `assertIn` y `assertNotIn`: Comprueban si un elemento está o no está dentro de una secuencia, como una lista o un conjunto.

## **¿Cómo se manejan excepciones en Unit Test?**

Con `assertRaises`, se puede verificar que una excepción se lance correctamente. Este método es especialmente útil para manejar errores esperados, como cuando un usuario no tiene suficientes fondos para completar una transferencia.

- Se utiliza con `with` para capturar la excepción dentro de un bloque de código.
- Ejemplo: Capturar un `ValueError` al pasar un argumento no válido a una función.

## **¿Cómo comparar listas, diccionarios y sets en Unit Test?**

Unit Test ofrece métodos para comparar estructuras de datos más complejas:

- `assertDictEqual`: Compara dos diccionarios.
- `assertSetEqual`: Compara dos sets para validar que contengan los mismos elementos, independientemente del orden.
- Estos métodos también cuentan con variantes negativas, como `assertNotEqual`, para validar desigualdades.

```python
#tests/tests_all_asserts.py
import unittest

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )
```

# Control de pruebas unitarias con unittest.skip en Python

En el desarrollo de software, es común enfrentarse a situaciones donde las pruebas unitarias no pueden ejecutarse por cambios o desarrollos en curso. En estos casos, comentar el código de las pruebas no es la mejor práctica. Afortunadamente, Python y `unittest` ofrecen decoradores que nos permiten omitir pruebas temporalmente, sin comprometer el flujo de trabajo ni la integridad del proyecto. Aquí aprenderemos cómo usar decoradores como `@skip`, `@skipIf` y `@expectedFailure` para manejar estos casos de manera eficiente.

## **¿Cómo utilizar el decorador @skip?**

El decorador `@skip` se utiliza cuando sabemos que una prueba no debería ejecutarse temporalmente. Esto es útil si estamos trabajando en un feature que aún no está completo y, por lo tanto, las pruebas no tienen sentido. Al aplicar `@skip`, podemos evitar la ejecución de la prueba y aún así tener visibilidad de que está pendiente de ser corregida.

- Aplicamos el decorador con una razón clara.
- Cuando ejecutamos las pruebas, en el reporte se indicará que la prueba fue saltada.

### Ejemplo de uso:

```python
@unittest.skip("Trabajo en progreso, será habilitada nuevamente.")
def test_skip_example(self):
    self.assertEqual("hola", "chau")

```

## **¿Cuándo aplicar @skipIf?**

El decorador `@skipIf` es útil cuando queremos omitir una prueba bajo una condición específica. Esto es común cuando nuestras pruebas dependen del entorno, como servidores diferentes o configuraciones específicas.

- Requiere una condición y una razón para ser aplicado.
- Se ejecutará solo si la condición es verdadera.

### Ejemplo de uso:

```python
server = "server_b"
@unittest.skipIf(server == "server_a", "Saltada porque no estamos en el servidor correcto.")
def test_skipif_example(self):
    self.assertEqual(1000, 100)

```

## **¿Qué hace el decorador @expectedFailure?**

Este decorador se usa cuando sabemos que una prueba fallará debido a un cambio en la lógica del negocio o un bug conocido, pero queremos mantener la prueba visible en el reporte de pruebas.

- Es útil para reflejar fallos esperados sin interferir con el flujo de integración continua.
- El reporte mostrará que la prueba falló como se esperaba.

### Ejemplo de uso:

```python
@unittest.expectedFailure
def test_expected_failure_example(self):
    self.assertEqual(100, 150)

```

## **¿Cómo aplicar @skipUnless en casos avanzados?**

El decorador `@skipUnless` es valioso cuando queremos ejecutar una prueba solo si se cumple una condición. Un ejemplo clásico es validar si un servicio externo, como una API, está disponible antes de ejecutar la prueba.

- Es ideal para escenarios donde dependemos de recursos externos, como API’s de terceros.

### Ejemplo de uso:

```python
@unittest.skipUnless(api_available(), "API no disponible.")
def test_skipunless_example(self):
    self.assertEqual(get_currency_rate("USD"), 1.0)

```

## **¿Cuándo utilizar estos decoradores en desarrollo colaborativo?**

El uso de decoradores como `@skip`, `@skipIf`, `@expectedFailure` y `@skipUnless` en un equipo de desarrollo asegura que las pruebas no interfieran en el flujo de trabajo, mientras mantienen la visibilidad de las pruebas pendientes. Es esencial en entornos de integración continua (CI), donde se busca que las pruebas no bloqueen el desarrollo, pero sin ignorarlas por completo.

```python
#tests/tests_all_asserts.py
import unittest

SERVER="server_b"

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )

    @unittest.skip("Trabajo en progreso, será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola", "chao")

    @unittest.skipIf(SERVER == "server_b", "Saltado porque no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)
```

# 🔹 Organización y Gestión de Pruebas

# Cómo organizar y ejecutar pruebas en Python con UnitTest

Cuando estamos desarrollando en Python, ejecutar todas las pruebas desde la terminal es común en entornos de desarrollo. Sin embargo, en producción o integración continua, este enfoque puede no ser ideal, especialmente cuando solo queremos ejecutar pruebas específicas o tener un mejor control sobre cómo organizamos y ejecutamos estas pruebas. Python y su módulo Unit Test nos ofrecen herramientas como las suites de pruebas para modularizar y seleccionar qué pruebas ejecutar.

## **¿Cómo ejecutar pruebas específicas en Python?**

Para ejecutar pruebas específicas, podemos usar el comando `discover` del subcomando Unit Test. Este comando busca automáticamente todas las pruebas dentro de una carpeta y las agrupa en una suite. Sin embargo, este enfoque no es siempre ideal para entornos locales, donde podríamos querer ejecutar solo ciertas pruebas.

### ¿Qué son las suites de pruebas?

Una suite de pruebas es un grupo de pruebas que podemos ejecutar juntas. En proyectos pequeños, generalmente tenemos una sola suite, pero a medida que crece el proyecto, modularizar las pruebas por categorías o características es recomendable. Por ejemplo, podríamos tener una suite para pruebas de calculadora y otra para pruebas de banco.

## **¿Cómo crear y ejecutar una suite de pruebas manualmente?**

1. **Crear una suite manualmente**:
    - Creamos un archivo nuevo, por ejemplo, `test_suites.py`.
    - Importamos `UnitTest` y definimos una suite con `suite = unittest.TestSuite()`.
    - Agregamos pruebas a la suite usando `suite.addTest()`.
2. **Agregar pruebas específicas**:
    - Podemos importar pruebas existentes y añadirlas a la suite. Por ejemplo, si ya tenemos una prueba llamada `test_deposit`, podemos agregarla a la suite con `suite.addTest(bankAccountTests('test_deposit'))`.
3. **Ejecutar las suites con un runner**:
    - Para ejecutar una suite, necesitamos un runner. Python ofrece varios tipos de runners. Un ejemplo sería el `TextTestRunner`, que se usa comúnmente en la terminal.
    - El código básico para ejecutar la suite sería:
        
        ```python
        runner = unittest.TextTestRunner()
        runner.run(suite)
        
        ```
        

```python
#tests/test_suites.py
import unittest

#from tests.test_bank_account import BankAccountTests
from test_bank_account import BankAccountTests

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
```

## **¿Cómo configurar Visual Studio Code para ejecutar pruebas?**

Visual Studio Code facilita la ejecución de pruebas con su interfaz gráfica. Podemos configurar un runner y seleccionar qué pruebas ejecutar directamente desde el editor.

1. **Configurar las pruebas en Visual Studio Code**:
    - En la configuración, seleccionamos Unit Test como el framework de pruebas y especificamos la carpeta donde se encuentran las pruebas.
    - Visual Studio Code lista automáticamente las pruebas, permitiéndonos ejecutarlas con un solo clic.
2. **Ejecutar pruebas individuales**:
    - Al hacer clic en una prueba específica, podemos ver su resultado inmediatamente, ya sea que la prueba haya pasado, fallado o se haya omitido.

## **¿Cómo solucionar errores comunes al ejecutar pruebas?**

Durante la ejecución de las pruebas, es común encontrarse con errores como “módulo no encontrado”. Estos errores se pueden solucionar asegurándonos de que las carpetas contienen archivos `__init__.py` y configurando correctamente el `PYTHONPATH` para que Python encuentre todos los módulos necesarios.

En nuestro caso: `PYTHONPATH=. python tests/test_suites.py`

## **¿Cómo ejecutar pruebas desde la terminal?**

Podemos ejecutar una prueba específica directamente desde la terminal usando la siguiente estructura de comando:

```bash
python -m unittest tests.test_calculator.CalculatorTest.test_add

```

Esto ejecuta únicamente la prueba `test_sum` de la clase `CalculatorTest`.

# Mejores prácticas para organizar y nombrar pruebas en Python

Nombrar pruebas correctamente es clave para el éxito en equipo, facilitando la comprensión del código y la colaboración efectiva. Aunque no es obligatorio, tener un formato claro para las pruebas es muy beneficioso.

## **¿Cómo definir el formato de los nombres de las pruebas?**

- Todos los tests deben agruparse en clases, cada una relacionada con una clase de tu proyecto. Por ejemplo, si tienes una clase llamada `BankAccount`, la clase de prueba debería llamarse `BankAccountTest`.
- Cada prueba debe comenzar con `test_`, para que las herramientas de testing la identifiquen fácilmente.
- El siguiente elemento en el nombre debe ser el método que estás probando. Si es un método `deposit`, el nombre sería `test_deposit_`.

## **¿Cómo estructurar el escenario de la prueba?**

- Después del método, añade el escenario. Esto se refiere a los valores o parámetros que usas en la prueba. Por ejemplo, en el caso de un valor positivo en un depósito, el escenario sería `positive_amount`.

## **¿Cómo describir el resultado esperado?**

- Para finalizar el nombre, indica el resultado esperado. Si el depósito incrementa el saldo, añade algo como `increase_balance`. Así, un nombre de prueba completo sería: `test_deposit_positive_amount_increase_balance`.

## **¿Por qué es útil este formato?**

- Permite a cualquier miembro del equipo entender el propósito de la prueba sin revisar el código completo.
- Facilita el mantenimiento del código y el soporte, ya que con solo leer el nombre, se entiende el objetivo de la prueba.

## 🚀 Reto. **¿Qué reto se propone para mejorar las pruebas actuales?**

- Refactoriza las pruebas que has creado, probando diferentes escenarios y resultados posibles.
- Imagina nuevas circunstancias para probar el código.

```python
#test_bank_account.py 
import unittest, os

from src.exceptions import InsufficientFundsError
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit_increases_balance_by_deposit_amount(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw_decreases_balance_by_withdraw_amount(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance_returns_current_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_withdraw_logs_each_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)
```

# 🔹 Técnicas Avanzadas en Pruebas Unitarias

# Mocking de APIs externas en Python con unittest

La simulación de servicios externos es crucial en proyectos de software para garantizar que las pruebas no dependan de APIs externas. Para lograrlo, utilizamos los Mocks, que permiten evitar las llamadas reales a servicios y, en cambio, retornan respuestas controladas en nuestras pruebas. En este caso, aprenderemos a mockear una API de geolocalización y a realizar pruebas efectivas.

## **¿Qué es un Mock y cómo nos ayuda?**

Un Mock es una herramienta que nos permite simular comportamientos de funciones o servicios externos. En lugar de ejecutar una llamada real a una API, podemos definir una respuesta predefinida, lo que permite:

- Evitar depender de servicios externos en pruebas.
- Acelerar la ejecución de las pruebas.
- Controlar los resultados esperados.

## **¿Cómo integramos una API externa en Python?**

Primero, se configura una función que recibe la IP del cliente y devuelve la ubicación mediante una API de terceros. Para hacer esto:

1. Se instala la librería `requests` con `pip install requests`.
2. Se crea un archivo `api_client.py` donde conectamos con la API utilizando `requests.get`.
3. Al recibir la respuesta, se convierte el resultado a JSON para obtener la información de país, ciudad y región.

```python
#src/api_client.py
import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }

if __name__ == "__main__":
    print(get_location("8.8.8.8"))
```

## **¿Cómo probamos sin hacer llamadas reales?**

El problema principal de las pruebas de integraciones con APIs es que pueden requerir tiempo, ya que las respuestas dependen de factores externos. Para evitar esto, se usan Mocks. A través del decorador `@patch` de `unittest.mock`, podemos interceptar la llamada a la API y retornar datos predefinidos.

Pasos a seguir:

- Decorar la función de prueba con `@patch`.
- Simular el valor retornado usando `mock.return_value` para definir qué debe devolver la llamada a la API.
- Definir tanto el código de estado como el contenido del JSON que esperamos recibir.

```python
#tests/test_api_client.py
import unittest
from src.api_client import get_location
from unittest.mock  import patch

class ApiClientTests(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
```

## **¿Cómo validar que nuestra simulación funciona correctamente?**

Además de simular respuestas, debemos asegurarnos de que las pruebas validen correctamente los llamados. Se puede usar `assertCalledOnceWith` para garantizar que la URL y los parámetros pasados son los correctos.

# Uso de Side Effects en Mocking con Python

Mock nos permite simular comportamientos variables, una herramienta útil cuando queremos probar cómo reacciona nuestro código ante diferentes escenarios sin modificar el entorno real. Uno de los usos más poderosos es el “side effect”, que nos ayuda a hacer que un método falle en un caso y funcione en otro. Esto es clave para manejar errores temporales, como en el caso de una API de pagos que rechaza una tarjeta incorrecta, pero acepta una correcta en un segundo intento.

## **¿Cómo se define un “side effect” en Mock?**

El “side effect” en Mock nos permite modificar el comportamiento de un método en distintas llamadas. Se define como una lista de comportamientos, donde cada elemento de la lista corresponde al resultado de una llamada específica. Esto permite:

- Simular fallos de manera controlada, como lanzar excepciones específicas en las pruebas.
- Probar el código bajo diferentes condiciones sin interactuar con los servicios externos.

## **¿Cómo se maneja un error y una respuesta exitosa en pruebas unitarias?**

En una prueba unitaria con Mock, podemos definir comportamientos variables. Por ejemplo, para simular una excepción, usamos la estructura `side_effect`, donde la primera llamada lanza un error y la segunda retorna una respuesta exitosa. Esto permite cubrir ambos casos sin necesidad de realizar un request real.

- Definimos el primer comportamiento con una excepción.
- Luego, para el segundo comportamiento, usamos `Mock` para devolver un objeto con los valores que esperamos, simulando una respuesta exitosa.

## **¿Qué métodos auxiliares facilita Mock?**

Mock facilita métodos como `raiseException`, que lanza una excepción específica, y `mock`, que permite crear objetos personalizados. Estos objetos pueden tener parámetros configurables como `status_code` y devolver datos específicos al llamar métodos como `JSON`. Este tipo de pruebas es crucial para validar la resiliencia del software ante errores temporales.

```python
#tests/test_api_client.py
import unittest, requests
import unittest.mock
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "FLORIDA",
                    "cityName": "MIAMI",
                },
            ),
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")
```

**Nota:** 

En este test, la **lambda** se utiliza dentro de `json=lambda: { ... }` para definir el comportamiento del método `.json()` en el segundo mock de `requests.get`.

**¿Por qué usar una lambda en lugar de un diccionario directamente?**

Si se escribiera directamente así:

```python
json={"countryName": "USA", "regionName": "FLORIDA", "cityName": "MIAMI"}

```

el diccionario quedaría almacenado como un **atributo estático** del mock. Esto significa que cualquier modificación accidental en el código podría afectar su valor.

En cambio, usando una **lambda**:

```python
json=lambda: { "countryName": "USA", "regionName": "FLORIDA", "cityName": "MIAMI" }

```

- Se asegura de que **cada vez que se llame `mock.json()`**, se genere un **nuevo diccionario**, evitando efectos colaterales.
- Esto simula de forma más realista el comportamiento de `requests.Response.json()`, que devuelve una nueva estructura de datos cada vez que se llama.

**Explicación del código**

```python
@patch("src.api_client.requests.get")
def test_get_location_returns_side_effect(self, mock_get):

```

- Se usa `@patch` para **reemplazar `requests.get` por un mock** dentro del test.

```python
mock_get.side_effect = [
    requests.exceptions.RequestException("Service Unavailable"),
    unittest.mock.Mock(
        status_code=200,
        json=lambda: {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        },
    ),
]

```

- `mock_get.side_effect` define **una secuencia de respuestas simuladas** para `requests.get`:
    1. Primero, lanza una `RequestException` simulando que el servicio está caído.
    2. Luego, devuelve un mock que simula una respuesta exitosa con un código `200` y un método `.json()` que devuelve los datos esperados.

```python
with self.assertRaises(requests.exceptions.RequestException):
    get_location("8.8.8.8")

```

- Se espera que el primer intento **genere una excepción** porque la API está "no disponible".

```python
result = get_location("8.8.8.8")
self.assertEqual(result.get("country"), "USA")
self.assertEqual(result.get("region"), "FLORIDA")
self.assertEqual(result.get("city"), "MIAMI")

```

- La segunda llamada devuelve el mock con la respuesta simulada.
- Se verifica que los datos obtenidos sean los esperados.

El uso de **lambda en `json=lambda: {...}`** garantiza que cada llamada a `.json()` devuelva un **nuevo objeto**, simulando el comportamiento real de `requests.Response.json()`.

## 🚀 Reto. **¿Cómo integrar validaciones adicionales en las pruebas?**

Para reforzar las pruebas, puedes agregar validaciones adicionales, como simular el envío de una IP inválida. En este caso, si la IP es incorrecta, se debe lanzar un error, mientras que si es válida, debe retornar los datos de geolocalización. Esto se implementa agregando más casos en la lista de side effects, cubriendo así todas las situaciones posibles.

```python
#src/api_client.py
import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    
    # Manejo de errores HTTP
    if response.status_code != 200:
        raise ValueError(f"API error: {response.status_code}")
    
    data = response.json()
    
    # Manejo de respuesta con error
    if "error" in data:
        raise ValueError(f"Invalid IP address: {data['error']}")
    
    return {
        "country": data.get("countryName", "Unknown"),
        "region": data.get("regionName", "Unknown"),
        "city": data.get("cityName", "Unknown"),
    }

if __name__ == "__main__":
    print(get_location("8.8.8.8"))

```

```python
# tests/test_api_client.py
import unittest
from unittest.mock import patch
import requests
from src.api_client import get_location

class ApiClientTests(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "FLORIDA",
                    "cityName": "MIAMI",
                },
            ),
            unittest.mock.Mock(
                status_code=400,
                json=lambda: {"error": "Invalid IP address"},
            ),
        ]

        # Primer intento: Falla por servicio no disponible
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        # Segundo intento: Responde correctamente
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        # Tercer intento: IP inválida
        with self.assertRaises(ValueError) as context:
            get_location("999.999.999.999")

```

# Uso de Patching para Modificar Comportamientos en Python

Ahora vamos a aprender a modificar el comportamiento de objetos y funciones dentro de nuestras pruebas en Python, utilizando técnicas como el *patch* para simular situaciones específicas, como el control del horario de retiro en una cuenta bancaria. Esta habilidad es crucial cuando necesitamos validar restricciones temporales o cualquier otra lógica de negocio que dependa de factores externos, como el tiempo.

## **¿Cómo podemos restringir el horario de retiros en una cuenta bancaria?**

Para implementar la restricción de horario, se utiliza la clase `datetime` para obtener la hora actual. Definimos que los retiros solo pueden realizarse durante el horario de oficina: entre las 8 AM y las 5 PM. Cualquier intento fuera de este horario lanzará una excepción personalizada llamada `WithdrawalError`.

- Se implementa la lógica en el método de retiro de la clase `BankAccount`.
- La restricción se basa en comparar la hora actual obtenida con `datetime.now().hour`.
- Si la hora es menor que las 8 AM o mayor que las 5 PM, se lanza la excepción.

```python
#src/exceptions.py
class InsufficientFundsError(Exception):
    pass

class WithdrawalTimeRestrictionError(Exception):
    pass
```

```python
#src/bank_account.py
class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8am to 5pm")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Withdrawal of {amount} exceeds balance {self.balance}"
            )
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
```

```python
#tests/test_bank_account.py
import unittest, os
from unittest.mock import patch
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit_increases_balance_by_deposit_amount(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw_decreases_balance_by_withdraw_amount(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance_returns_current_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_withdraw_logs_each_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
```

## **¿Cómo podemos probar la funcionalidad de manera efectiva?**

Las pruebas unitarias permiten simular diferentes horas del día para validar que las restricciones funcionen correctamente. Para lograrlo, usamos el decorador `patch` del módulo `unittest.mock`, el cual modifica temporalmente el comportamiento de la función `datetime.now()`.

- Con `patch`, podemos definir un valor de retorno específico para `now()`, como las 7 AM o las 10 AM.
- De esta forma, se puede validar que la excepción se lance correctamente si el retiro ocurre fuera del horario permitido.
- En caso de que el retiro sea dentro del horario, la prueba verificará que el saldo de la cuenta se actualice correctamente.

## 🚀 Reto.

Agrega una nueva funcionalidad a nuestra bank account, no permitas retiros ni sábados ni domingos. Crea las pruebas unitarias para esos casos: haz una prueba para el domingo y otra para el lunes.

```python
#src/bank_account.py
from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()

        # Bloquear retiros en sábado (5) y domingo (6)
        if now.weekday() in [5, 6]:
            raise WithdrawalTimeRestrictionError("Withdrawals are not allowed on weekends")

        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8am to 5pm")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Withdrawal of {amount} exceeds balance {self.balance}"
            )
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance

```

```python
#tests/test_bank_account.py
import unittest, os
from unittest.mock import patch
from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit_increases_balance_by_deposit_amount(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw_decreases_balance_by_withdraw_amount(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance_returns_current_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_withdraw_logs_each_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 2, 12, 8)  # Lunes 8:00 AM
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 2, 12, 7)  # Lunes 7:00 AM
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 2, 12, 18)  # Lunes 6:00 PM
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_on_sunday(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 2, 11, 10)  # Domingo 10:00 AM
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_allow_on_monday(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 2, 12, 10)  # Lunes 10:00 AM
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

```

# 🔹 Exploración de Herramientas y Métodos Complementarios

# Cómo parametrizar pruebas en Python con SubTest

El uso de SubTest en UnitTest te permite optimizar tus pruebas evitando la duplicación de código. Imagina que necesitas probar un método con varios valores diferentes. Sin SubTest, tendrías que crear varias pruebas casi idénticas, lo que resulta ineficiente. SubTest permite parametrizar pruebas, lo que significa que puedes ejecutar la misma prueba con diferentes valores sin repetir el código.

## **¿Cómo evitar la duplicación de pruebas con SubTest?**

Al utilizar SubTest, puedes definir todos los valores que deseas probar en una lista o diccionario. Luego, iteras sobre estos valores mediante un bucle `for`, ejecutando la misma prueba con cada conjunto de parámetros. Así, si es necesario modificar la prueba, solo tienes que hacer cambios en un único lugar.

## **¿Cómo implementar SubTest en un caso práctico?**

Para ilustrarlo, se puede crear una prueba llamada `test_deposit_various_values`. En lugar de duplicar la prueba con diferentes valores de depósito, utilizas un diccionario que contiene los valores a probar y el resultado esperado. Después, recorres estos valores con SubTest usando la estructura `with self.subTest(case=case)` y ejecutas la prueba para cada valor del diccionario. Esto asegura que cada prueba sea independiente y evita sumar valores a la cuenta de manera incorrecta.

## **¿Cómo gestionar errores con SubTest?**

SubTest también es útil para identificar errores específicos. Si una prueba falla con un conjunto particular de parámetros, SubTest te permite ver fácilmente qué valores causaron el fallo. Esto facilita mucho la corrección de errores, ya que puedes aislar rápidamente los casos problemáticos y corregirlos de manera eficiente.

```python
#tests/test_bank_account.py
#...

def test_deposit_multiple_amounts(self):
    test_cases = [
        {"ammount": 100, "expected": 1100},
        {"ammount": 3000, "expected": 4000},
        {"ammount": 4500, "expected": 5500},
    ]
    
    for case in test_cases:
        with self.subTest(case=case): 
            self.setUp()  # Reinicia el estado para cada caso
            new_balance = self.account.deposit(case["ammount"])
            self.assertEqual(new_balance, case["expected"])
```

# Documentación de pruebas unitarias con Doctest en Python

El uso de Doctest es una herramienta poderosa que te permite escribir pruebas directamente en la documentación del código, lo que facilita que otros desarrolladores comprendan y verifiquen los resultados esperados. Además de los Unit Tests tradicionales, Doctest permite que tus comentarios sean interactivos, ofreciendo ejemplos funcionales que se ejecutan dentro del código de Python. Veamos cómo puedes utilizarlo de manera eficiente.

## **¿Qué es Doctest y cómo se usa?**

Doctest es una librería que está incluida en Python y que permite crear pruebas en los comentarios del código. Esto lo hace práctico ya que puedes escribir pruebas de manera muy similar a una sesión interactiva de Python. Solo debes añadir los ejemplos dentro de los comentarios y ejecutarlos con el comando `python -m doctest`.

## **¿Cómo se estructuran las pruebas en Doctest?**

Para escribir una prueba, simplemente crea un comentario que simule una sesión interactiva. Estas sesiones se caracterizan por comenzar con `>>>`. Por ejemplo, si tienes una función de suma en tu clase `Calculator`, podrías escribir lo siguiente:

```python
>>> sum(5, 7)
12

```

Esto se ejecutará como si estuvieras en el shell de Python, y esperará que la salida sea `12`. Si el resultado no coincide con lo esperado, Doctest te notificará el error.

## **¿Qué hacer si hay un error en la prueba?**

Si Doctest encuentra un error, revisa el mensaje de error y ajusta el código o la prueba según sea necesario. Por ejemplo, si ejecutas una prueba y esperabas `12` pero el resultado fue `11`, Doctest te informará de la discrepancia. Solucionas el error, corriges el comentario, y ejecutas nuevamente.

## **¿Cómo manejar excepciones en Doctest?**

Doctest también te permite probar excepciones. Si tienes una función que lanza un `ValueError` al intentar dividir por cero, puedes capturar este comportamiento en el comentario:

```python
>>> divide(10, 0)
Traceback (most recent call last):
  ...
ValueError: División por 0 no permitida

```

Este tipo de pruebas asegura que las excepciones se manejen correctamente y ayuda a otros desarrolladores a entender los casos de error.

## **¿Por qué es importante documentar con Doctest?**

La documentación clara es clave en cualquier proyecto de software, y Doctest facilita agregar ejemplos en el código que no solo explican cómo usar las funciones, sino que además se prueban automáticamente. Esto garantiza que la documentación esté siempre alineada con el comportamiento real del código.

```python
#src/calculator
def sum(a, b):
    """
    >>> sum(5, 7)
    12

    >>> sum(4, -4)
    0
    """
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: La división por cero no está permitida
    """

    if b == 0:
        raise ValueError("La división por cero no está permitida")
    return a / b
```

## 🚀 Reto.

El reto de este enfoque es agregar suficiente documentación con ejemplos ejecutables que cubran todos los casos, incluyendo los casos de borde, como divisiones por cero o parámetros inválidos. Este proceso no solo mejora la calidad del código, sino también la de la documentación, haciéndola más útil para todo el equipo.

# Cómo generar datos de prueba dinámicos con Faker en Python

Generar datos de prueba puede ser una tarea tediosa, pero con la librería Faker, este proceso se simplifica enormemente. Faker nos permite crear datos aleatorios como nombres, correos electrónicos y otros atributos de manera eficiente para validar la compatibilidad de nuestro código con diversas entradas. A continuación, exploramos cómo aprovechar Faker en pruebas automatizadas y cómo integrar la librería en nuestro proyecto.

## **¿Cómo instalar Faker y qué ventajas ofrece?**

Para empezar a utilizar Faker, simplemente debemos instalarla a través de la terminal con el comando:

```bash
pip install faker

```

Una vez instalada, podemos importarla en nuestro proyecto e instanciar un generador de datos aleatorios. Faker nos ofrece una gran variedad de métodos predefinidos para generar nombres, correos, cuentas bancarias, entre otros. La ventaja clave es que nos permite automatizar la generación de múltiples entradas en cada ejecución de nuestras pruebas.

## **¿Cómo integramos Faker en nuestro proyecto?**

Una vez que hemos instalado Faker, es esencial agregar la librería a nuestro archivo `requirements.txt`. Esto asegura que todas las dependencias se mantengan actualizadas y permite su instalación en futuros entornos. También es importante definir una versión fija para evitar problemas con actualizaciones inesperadas que puedan romper nuestro código.

## **¿Cómo crear una clase User con Faker?**

Al integrar Faker, podemos crear pruebas más realistas. Por ejemplo, al generar datos para un usuario con múltiples cuentas bancarias, podemos usar Faker para generar atributos como el nombre, correo electrónico y balances de cuentas de forma dinámica. A continuación, se muestra un ejemplo de cómo podemos definir una clase `User` y generar múltiples cuentas con balances aleatorios:

- Se crea una clase `User` que requiere un nombre, correo electrónico y una lista de cuentas bancarias.
- Faker se utiliza para generar estos valores automáticamente en cada prueba.
- Se pueden generar múltiples cuentas para un mismo usuario, iterando sobre un ciclo `for` para generar diferentes balances y archivos de log.

```python
#src/user.py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)
```

```python
#tests/test_user.py
import unittest, os
from faker import Faker
from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):
    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(), email=self.faker.email())
    
    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated, email=email_generated)
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)
    
    def test_user_with_multiple_accounts(self):
        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension=".txt")
            )
            self.user.add_account(account=bank_account)
        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value, expected_value)
    
    def tearDown(self) -> None:
        for account in self.user.accounts:
            os.remove(account.log_file)
```

## **¿Cómo se estructuran las pruebas con Faker?**

En nuestras pruebas unitarias, podemos instanciar Faker en el método `setUp` para reutilizarla en todas las pruebas. Esto nos permite generar nombres y correos electrónicos dinámicos en cada ejecución. A continuación, se presentan los pasos clave para estructurar las pruebas:

1. Instanciamos Faker en el método `setUp`.
2. Definimos pruebas para la creación de usuarios con múltiples cuentas.
3. Utilizamos Faker para generar atributos aleatorios como balances y nombres de archivo.
4. Validamos que los valores generados sean correctos utilizando `assertEqual` para verificar la integridad de los datos.

## **¿Qué otras configuraciones y opciones ofrece Faker?**

Faker ofrece una amplia gama de configuraciones. Por ejemplo, podemos definir el idioma de los datos generados. Esto es útil si necesitamos que nuestros datos de prueba estén en español o en otro idioma. También es posible generar datos más complejos como nombres de archivos, países o incluso valores numéricos aleatorios con rangos definidos.

## **¿Cómo limpiar el entorno de pruebas?**

Al generar archivos temporales durante las pruebas, es importante asegurarse de limpiar el entorno una vez que finalicen. Esto se puede hacer implementando un método `tearDown` que borre los archivos generados durante la ejecución de las pruebas, garantizando que el entorno de pruebas se mantenga limpio.

# 🔹 Mejora y Automatización de Pruebas

# ¿Cómo asegurar la cobertura de pruebas con Coverage en Python?

En los proyectos grandes de software, resulta difícil identificar qué partes del código están correctamente probadas y cuáles no lo están. Por ello, es esencial usar herramientas como Coverage, que nos permite analizar qué porciones de nuestro código han sido ejecutadas durante las pruebas y cuáles no. Esto facilita la detección de áreas que necesitan cobertura adicional.

## **¿Qué es Coverage y cómo funciona?**

Coverage es una herramienta que se ejecuta junto a las pruebas y captura un reporte sobre qué partes del código han sido probadas. Una vez finalizado el proceso, genera un informe detallado que indica qué porcentaje del código está cubierto. De esta manera, puedes identificar qué secciones de código necesitan nuevas pruebas.

## **¿Cómo instalar y utilizar Coverage?**

Para instalar Coverage en un proyecto Python, sigue los siguientes pasos:

- Abre la terminal e instala la herramienta con `pip install coverage`.
- Después, usa `pip freeze | grep coverage` para agregar la librería a tu archivo de requirements.
- Una vez instalada, ejecuta el comando `coverage run -m unittest discover -s tests`, que corre las pruebas en la carpeta `tests`.

## **¿Cómo generar el reporte de cobertura?**

Para generar el informe de cobertura de código:

1. Usa el comando `coverage report` para obtener un resumen de las pruebas.
2. Si quieres un reporte visual más detallado, ejecuta `coverage html`. Esto creará una carpeta con archivos HTML que podrás abrir en el navegador.

## **¿Cómo mejorar el reporte excluyendo archivos de prueba?**

Para evitar que los archivos de prueba aparezcan en el reporte, agrega el parámetro `--source=src` al comando `coverage run`. Esto asegura que solo se evalúe el código fuente de la aplicación y no las pruebas en sí mismas.

## **¿Cómo detectar y corregir código sin pruebas?**

Coverage permite identificar líneas específicas que no han sido probadas. Usando el reporte HTML, puedes hacer clic en los archivos para ver las líneas de código no ejecutadas. Un ejemplo sería la detección de un método que no maneja una división por cero. Al agregar un test para esta excepción, puedes aumentar la cobertura total del proyecto.

## **¿Cómo validar un porcentaje mínimo de cobertura?**

En proyectos con equipos grandes, es recomendable establecer un porcentaje mínimo de cobertura, como un 80%, para garantizar la calidad del código. Esto se puede configurar en la documentación de Coverage.

# Automatización de Pruebas Unitarias en Python con GitHub Actions

Integrar una suite de pruebas en un sistema de Continuous Integration (CI) es clave para automatizar el proceso de verificación de cambios en el código. En este caso, usaremos GitHub Actions para correr nuestras pruebas de manera automática cada vez que haya un cambio en el repositorio, asegurándonos de que el código esté siempre funcionando correctamente.

## **¿Cómo configurar tu primera GitHub Action?**

Primero, accede a la pestaña de “Actions” dentro de tu repositorio en GitHub. Ahí encontrarás un Marketplace con varias opciones. Busca “Python” y selecciona la Action “Python Application”. Esta configuración correrá pruebas automáticamente cada vez que haya un push o un pull request hacia la rama “Main”.

## **¿Qué pasos incluye el workflow de pruebas?**

- **Clonación del repositorio:** El workflow comienza clonando tu código, similar a un `git clone`.
- **Configuración de Python:** Utiliza la versión 3.10 de Python, asegurando compatibilidad con el código del proyecto.
- **Instalación de dependencias:** Ejecuta las instalaciones de las librerías listadas en el archivo `requirements.txt`, por ejemplo, Faker y Coverage.
- **Modificación del comando de pruebas:** En lugar de utilizar un test genérico, el comando se cambia a `python -m unittest discover test`, adaptado a las pruebas unitarias del proyecto.

## **¿Cómo verificar si el workflow fue exitoso?**

Una vez configurado el archivo y hecho el commit, puedes ver el progreso de la ejecución en la pestaña de “Actions”. Si todo salió bien, aparecerá un checkmark verde indicando que las pruebas pasaron exitosamente.

## **¿Cómo mejorar la cobertura de pruebas en tu pipeline?**

El reto adicional consiste en ejecutar las pruebas con diferentes versiones de Python utilizando Matrix en GitHub Actions. Esto te permitirá probar tu código en varios entornos, asegurando mayor robustez y evitando problemas de compatibilidad.

# Pruebas Unitarias con PyTest en Python

Python ofrece una gran variedad de herramientas, y una de las más útiles para pruebas automatizadas es PyTest. PyTest mejora considerablemente la experiencia del desarrollador al permitir escribir y ejecutar pruebas de manera más eficiente. En esta guía veremos cómo instalar PyTest, crear pruebas parametrizadas y ejecutar un ejemplo básico.

## **¿Cómo instalar y configurar PyTest?**

- Abre la terminal y ejecuta el siguiente comando para instalar PyTest:
    
    ```
    pip install pytest
    
    ```
    
- Recuerda agregarlo a tu archivo `requirements.txt` con:
    
    ```
    pip freeze | grep pytest > requirements.txt
    
    ```
    

## **¿Cómo crear una prueba con PyTest?**

1. En la carpeta de pruebas, crea un archivo llamado `test_pytest.py`.
2. Importa PyTest en tu archivo:
    
    ```python
    import pytest
    
    ```
    
3. Crea una función de prueba simple como esta:
    
    ```python
    def test_suma():
        a = 4
        b = 4
        assert a + b == 8
    
    ```
    
4. Ejecuta la prueba con el siguiente comando:
    
    ```
    pytest test_pytest.py
    
    ```
    

PyTest no requiere la creación de clases para agrupar pruebas, lo cual simplifica el código. En este caso, las pruebas se agrupan por archivo.

## **¿Cómo parametrizar una prueba en PyTest?**

1. Utiliza decoradores de PyTest para parametrizar la prueba:
    
    ```python
    @pytest.mark.parametrize("amount, expected", [
        (100, 5000),
        (200, 5500),
        (300, 6000)
    ])
    def test_balance(amount, expected):
        assert calcular_balance(amount) == expected
    
    ```
    
2. En este ejemplo, la función de prueba recibe varios casos con valores diferentes de `amount` y `expected`.
3. Ejecuta las pruebas:
    
    ```
    pytest -v
    
    ```
    

## **¿Qué ventajas ofrece PyTest al ejecutar pruebas?**

- PyTest ofrece mensajes de error detallados y fáciles de leer, resaltados con colores.
- Los errores incluyen los valores específicos que causaron la falla.
- Con la opción `v`, PyTest detalla qué pruebas se ejecutaron y sus resultados.

## **¿Qué ocurre si una prueba falla?**

Si una prueba falla, PyTest te indicará exactamente qué valores no coincidieron. Por ejemplo, si uno de los valores esperados es incorrecto:

```python
def test_balance():
    assert calcular_balance(100) == 5400  # Este valor está incorrecto

```

Al ejecutar nuevamente la prueba, PyTest te mostrará la diferencia entre el valor esperado y el real.

## 🚀 Reto

Refactoriza todas las pruebas de tu proyecto para que utilicen PyTest, aplicando lo que hemos visto sobre parametrización y el uso de asserts más sencillos.

# Cómo crear pruebas unitarias con inteligencia artificial en Python

Las herramientas de inteligencia artificial han revolucionado la forma en que desarrollamos software, simplificando tareas como la creación de pruebas unitarias. Estas herramientas permiten generar pruebas más rápido y con mayor precisión, ahorrando tiempo y reduciendo errores. A continuación, exploramos algunas herramientas clave que todo desarrollador debería conocer.

## **¿Qué es GitHub Copilot y cómo puede ayudarte a escribir pruebas?**

GitHub Copilot es una extensión que puedes instalar en tu editor de código. Con ella, puedes chatear, darle contexto sobre tu código y pedirle que genere pruebas unitarias. Esta herramienta se integra directamente en el flujo de trabajo del desarrollador, lo que facilita la creación de pruebas con pocos comandos. Al escribir un prompt claro, como “create a test that doesn’t allow the deposit to be negative”, Copilot genera automáticamente el código de la prueba, optimizando el proceso de TDD (desarrollo guiado por pruebas).

### Beneficios de usar GitHub Copilot:

- Ahorra tiempo generando pruebas automáticamente.
- Mejora la precisión al sugerir código basado en grandes bases de datos de proyectos.
- Facilita la integración en editores populares como Visual Studio Code.

## **¿Qué ofrece Supermaven y cómo se compara con otras herramientas?**

Supermaven es una herramienta similar que permite integrar la API de ChatGPT directamente en tu editor de código. Con esta integración, puedes utilizar las capacidades de ChatGPT para generar y modificar pruebas en tiempo real. Lo interesante de Supermaven es que utiliza la misma suscripción de ChatGPT, lo que lo convierte en una opción versátil y eficiente para desarrolladores que ya usan esta IA.

### Características destacadas de Supermaven:

- Compatibilidad con múltiples editores de código.
- Capacidad para modificar pruebas según el contexto que le proporciones.
- Soporte para autocompletar código y optimizar la generación de pruebas unitarias.

## **¿Cómo usar ChatGPT para generar y modificar pruebas?**

ChatGPT es otra herramienta clave para generar pruebas. Al darle contexto sobre el código, como la clase `BankAccount`, puedes solicitar que modifique o cree pruebas unitarias parametrizadas, lo que simplifica aún más el proceso de validación. Esta interacción con la IA facilita la generación de pruebas más completas, incluyendo distintos casos de prueba como depósitos positivos y negativos.

### Proceso de uso de ChatGPT para pruebas:

1. Proporciona el contexto del código.
2. Pide que modifique o cree una prueba específica.
3. Analiza y ejecuta el código generado para verificar su funcionalidad.

## **¿Cuáles son las precauciones al usar herramientas de inteligencia artificial para pruebas?**

Es crucial recordar que, aunque estas herramientas son extremadamente útiles, no debes copiar y pegar código sin antes revisarlo. La IA utiliza grandes bases de datos de código, algunos de los cuales pueden contener errores o prácticas no recomendadas. Es importante que valides siempre el código generado antes de implementarlo en producción.

### Consejos para un uso adecuado:

- Revisa cuidadosamente cada sugerencia antes de integrarla a tu código.
- Asegúrate de que las pruebas cubran todos los casos posibles.
- Ajusta el código generado según las mejores prácticas de tu equipo o proyecto.

## **¿Qué otras buenas prácticas debes seguir al escribir pruebas unitarias?**

Además de usar herramientas de IA, existen otras buenas prácticas que debes tener en cuenta al desarrollar pruebas unitarias:

- Agrupa las pruebas por funcionalidad o clase.
- Utiliza herramientas como `coverage` para verificar qué partes del código no han sido probadas.
- Borra los comentarios generados automáticamente para mantener el código limpio.

## **5. Recursos Adicionales**

### **Documentación Oficial**

- [unittest — Marco de pruebas unitarias en Python](https://docs.python.org/3/library/unittest.html)
- [assert Methods en unittest](https://docs.python.org/3/library/unittest.html#assert-methods)

### **Artículos Relacionados**

- ["Getting Started with unittest in Python"](https://realpython.com/python-testing/)
- ["Python Unit Testing with unittest"](https://www.guru99.com/unit-test-python.html)
- ["How to Write Unit Tests in Python"](https://dev.to/mohammadfaisal/testing-in-python-with-unittest-3e0f)

### **Videos Recomendados**

- [Python unittest Tutorial for Beginners (YouTube)](https://www.youtube.com/watch?v=6tNS--WetLI)