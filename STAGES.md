## Plan por etapas (stages) para la Pre-Entrega de Auto-QA con Python para Talento Tech

### Estructura general del proyecto:

```
auto-qa-axel-novo
│
├── tests/
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
│
├── utils/
│   ├── driver_setup.py
│   └── helpers.py
│
├── reports/
│   └── reporte.html
│
├── README.md
└── requirements.txt

```
---

### Etapa 1 - Configuración base y entorno
Objetivo: Preparar entorno, dependencias y estructura inicial.

__Tareas:__

1. Crear entorno virtual y archivo `requirements.txt` con:

    - selenium
    - pytest
    - pytest-html
    - webdriver-manager
2. Configurar `driver_setup.py` para iniciar y cerrar el navegador.
3. Crear repositorio en GitHub y primer commit inicial con estructura vacía.
4. Crear `README.md`con secciones vacías.

__Definition of Done (DoD):__

- El entorno ejecuta pytest sin errores (`pytest --version` funciona).
- ChromeDriver abre y cierra correctamente desde `driver_setup.py`.
- Repositorio público creado y con primer push.
- Archivo `.gitignore` configurado (excluir `/reports`, `__pycache__`, `/venv`).

---

### Etapa 2 - Automatización de Login
Objetivo: Implementar y validar login exitoso en `saucedemo.com`.

__Tareas:__

1. Crear `test_login.py`.
2. Navegar a `https://www.saucedemo.com`.
3. Ingresar credenciales válidas (`standard_user`, `secret_sauce`).
4. Usar espera explícita para redirección a `inventory.html`.
5. Validar que el título sea "Products" y la URL contenga `/inventory.html`.

__Definition of Done (DoD):__

- Test ejecuta sin errores y valida login exitoso.
- Uso correcto de `WebDriverWait` y `expected_conditions`.
- No hay `sleep()`.
- El navegador se cierra al final.
- Commit con mensaje "Add login automation test".

---

### Etapa 3 - Nagegación y Verificación de Catálogo
Objetivo: Validar presencia y datos de productos.

__Tareas:__

1. Extender sesión de login o reutilizar helper
2. Verificar título de la página de inventario.
3. Validar que haya al menos un producto visible.
4. Imprimir nombre y precio del primer producto.

__Definition of Done (DoD):__

- Se verifica correctamente el título.
- Se lista al menos un producto visible.
- Test es independiente del login.
- Commit: "Add catalog navigation and validation test".

---

### Etapa 4 - Interacción con Productos
Objetivo: Automatizar flujo de agregar producto al carrito.

__Tareas:__

1. Localizar y hacer click en "Add to cart" del primer producto.
2. Verificar incremento del contador del carrito.
3. Ir al carrito y comprobar que el producto aparece.

__Definition of Done (DoD):__

- Contador se incrementa correctamente.
- Producto agregado visible en carrito.
- Commit: "Add cart interaction test".

---

### Etapa 5 - Reportes y Documentación
Objetivo: Generar reportes y documentación del proyecto.

__Tareas:__

1. Generar reporte HTML con:
    ```{bash}
    pytest tests/ -v --html=reports/reporte.html
    ```
2. Completar `README.md` con:
    - Propósito del proyecto
    - Tecnologías utilizadas
    - Instalación (`pip install -r requirements.txt`)
    - Ejecución (`pytest -v --html=reports/reporte.html`)
3. Verificar que todos los tests sean independientes.

__Definition of Done (DoD):__

- Reporte HTML generado sin errores.
- README completo y claro.
- Commit "Add report and documentation".

---

### Etapa 6 - Verificación final y entrega
Objetivo: Validar integridad del proyecto.

__Checklist:__

- Todos los tests pasan correctamente.
- Reporte HTML actualizado.
- README completo.
- Estructura del repositorio cumple formato pedido.
- Último commit: "Final pre-entrega TalentoTech".