# Proyecto Integrador de Automatización - Talento Tech - Axel Novo (PRE-ENTREGA)

Proyecto para Automatización QA con Python para Talento Tech. Hecho por Axel Novo.

## Propósito del proyecto
El propósito del proyecto es automatizar sobre una página web (saucedemo) los diferentes procesos como:
- Loguearse en la página web.
- Verificar la existencia de productos en la página principal.
- Verificar la correcta funcionalidad del carrito de compras.

## Tecnologías utilizadas
- Python
- Pytest
- Pytest-html
- Selenium
- Webdriver-manager

## Instalación de dependencias
Para una correcta instalación de dependencias, se recomienda ejecutar el siguiente comando:
```
pip install -r requirements.txt
```

## Ejecución de las pruebas
Para ejecutar las pruebas, es recomendado ejecutar los siguientes comandos:
- Para ejecutar todos los casos de prueba:
    ```
    pytest tests/
    ```
- Para ejecutar todos los casos de prueba con reporte:
    ```
    pytest tests/ --html=reports/full-tests-report.html
    ```
- Para ejecutar los casos de prueba del login:
    ```
    pytest tests/test_login.py
    ```
- Para ejecutar los casos de prueba del login con reporte:
    ```
    pytest tests/test_login.py --html=reports/login-report.html
    ```
- Para ejecutar los casos de prueba del carrito:
    ```
    pytest tests/test_shopping_cart.py
    ```
- Para ejecutar los casos de prueba del carrito con reporte:
    ```
    pytest tests/test_carrito.py --html=reports/shopping-cart-report.html
    ```
- Para ejecutar todos los casos de prueba del catálogo:
    ```
    pytest tests/test_catalog.py
    ```
- Para ejecutar todos los casos de prueba del catálogo con reporte:
    ```
    pytest tests/test_catalogo.py --html=reports/catalog-report.html
    ```

## Estructura del proyecto
La estructura actual del proyecto se divide, principalmente, en reports, tests y utils:
```
pre-entrega-automation-testing-axel-novo
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_catalog.py
│   └── test_shopping_cart.py
│
├── utils/
│   ├── __init__.py
│   ├── driver_setup.py
│   └── login_setup.py
│
├── reports/
│   ├── assets/
│   ├── catalog-report.html
│   ├── full-tests-report.html
│   ├── login-report.html
│   └── shopping-cart-report.html
│
├── .gitignore
├── README.md
├── requirements.txt
└── STAGES.md
```
- ```tests/``` contiene todas las pruebas, separadas por funcionalidad.
- ```utils/``` contiene las funciones utilizadas en las pruebas.
- ```reports/``` contiene los reportes generados por las pruebas.
- ```requirements.txt``` contiene las dependencias utilizadas en el proyecto.
- ```STAGES.md``` contiene la estructura general del proyecto. Se decidió separarlo en etapas para facilitar la lectura y entendimiento del proyecto.


## Resultados Esperados
- Login
    - Con credenciales válidas: redirección a ```/inventory.html```.
    - Con credenciales inválidas: mensaje de error visible en el formulario.
- Catálogo
    - Los productos se listan correctamente.
    - El primer producto se muestra correctamente en la lista.
- Carrito
    - Los productos se agregan correctamente al carrito.
    - El contador del carrito se actualiza correctamente.
    - Los productos se muestran correctamente en el carrito.

## Autor
Axel Brian Novo (AtselB)
