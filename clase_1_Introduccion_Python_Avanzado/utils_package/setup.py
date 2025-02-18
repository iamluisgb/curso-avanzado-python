from setuptools import setup, find_packages

setup(
    name="pyutils",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-dateutil>=2.8.0",
    ],
    author="Tu Nombre",
    author_email="tu@email.com",
    description="Un paquete de utilidades Python",
    keywords="utils, string, date, number",
    python_requires=">=3.7",
)
