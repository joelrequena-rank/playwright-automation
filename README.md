# Arquitectura del Proyecto

El proyecto sigue el patrón Page Object Model (POM) para separar claramente:

- Lógica de test
- Lógica de interacción con la UI
- Configuración por entorno
- Utilidades reutilizables

```
yobingo_site_login_tests/
│
├── pages/                # Page Objects
│   └── login_page.py
│
├── tests/                # Casos de prueba
│   └── test_login.py
│
├── config/               # Configuración por entorno
│   └── config.py
│
├── utils/                # Helpers reutilizables
│
├── pytest.ini
├── requirements.txt
└── .github/workflows/    # CI pipeline
```

---

# ⚙️ Instalación

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/yobingo_site_login_tests.git
cd yobingo_site_login_tests
```

## 2️⃣ Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
playwright install
```

---

# 🚀 Ejecución de Tests

La ejecución se realiza exclusivamente mediante los comandos definidos en el **Makefile**.

## Ejecutar todos los tests (default)

```bash
make test
```

Internamente ejecuta:

```bash
pytest -v
```

---

## Ejecutar entorno QA

```bash
make test-qa
```

Internamente ejecuta:

```bash
ENV=QA pytest -m qa
```

---

## Ejecutar entorno Staging

```bash
make test-staging
```

Internamente ejecuta:

```bash
ENV=staging pytest -m stg
```

---

## Ejecutar Staging en modo headed

```bash
make test-staging-headed
```

Internamente ejecuta:

```bash
ENV=staging pytest -m stg --headed
```

---

## Pipeline automation (uso en CI)

```bash
make pipeline-automation
```

Internamente ejecuta:

```bash
ENV=QA pytest -m qa
```

---

# 📊 Reportes con Allure

## Generar resultados

```bash
pytest --alluredir=allure-results
```

## Visualizar reporte

```bash
allure serve allure-results
```


---

# 🔁 Integración Continua

El proyecto incluye un pipeline en **GitHub Actions** que:

1. Instala dependencias
2. Instala navegadores de Playwright
3. Ejecuta tests E2E
4. Falla automáticamente si algún test falla