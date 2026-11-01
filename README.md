# Showroom Solar — Dimensionador Fotovoltaico & Memoria Técnica REBT

[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](#)
[![Version](https://img.shields.io/badge/Version-v4.3.0-blue.svg)](#)
[![Standards](https://img.shields.io/badge/Standards-REBT%20ITC--BT--19%2F20%2F40%20%7C%20IEC%2061724-orange.svg)](#)
[![Deploy](https://img.shields.io/badge/Deploy-Cloudflare%20Pages-f38020.svg)](#)

Aplicación web interactiva de alto rendimiento (SPA) diseñada para el **dimensionamiento fotovoltaico profesional, ingeniería eléctrica de cadenas Multi-MPPT, cálculo normativo de conductores según el REBT español y balance económico de amortización a 25 años**.

Desarrollada con estética industrial de producto (*Huawei FusionSolar / Apple / Xiaomi*), tipografía High-End (*Outfit*, *Plus Jakarta Sans*, *JetBrains Mono*) y un motor físico/electrotécnico con cero estimaciones arbitrarias (IEC 61724).

---

## 🌟 Características Principales

1. **Wizard Interactivo en 8 Pasos (Bento Grid UI):**
   - **Paso 0 (Portada):** Gestión de expediente, metadatos del titular e importación/exportación rápida en `.JSON`.
   - **Paso 1 (Consumo & PVGIS):** Integración satelital con la API de JRC PVGIS v5.2, curvas de demanda horarias y tarifas (Fija vs. 2.0TD en 3 periodos P1/P2/P3).
   - **Paso 2 (Generador Fotovoltaico):** Catálogo de módulos Tier-1 (LONGi, AIKO, Jinko, Trina, Canadian, JA Solar) o modo libre con validación térmica Evans/PVGIS.
   - **Paso 3 (Inversor & Multi-MPPT):** Dimensionamiento de 1 a 6 seguidores MPPT independientes, comprobaciones de tensión en frío ($-10\text{ °C}$) y calor ($+70\text{ °C}$), ventanas de arranque y ratio DC/AC.
   - **Paso 4 (Cableado & REBT):** Cumplimiento estricto de las instrucciones técnicas complementarias **ITC-BT-19, ITC-BT-20 e ITC-BT-40**, métodos de instalación A1..F UNE-HD 60364-5-52, caída de tensión $\Delta u\%$ y pérdidas Joule ($I^2 R$).
   - **Paso 5 (Sistemas de Almacenamiento):** Baterías de litio ferrofosfato (LiFePO4) de alto voltaje con cálculo de autarquía, balance de potencia horaria y degradación.
   - **Paso 6 (Legal & Viabilidad Económica):** Compensación de excedentes según RD 244/2019, amortización a 25 años, VAN, TIR, LCOE y marco fiscal (IVA 21% Península vs. IGIC 0% Canarias).
   - **Paso 7 (Showroom & Memoria Técnica A4):** Dashboard ejecutivo de resultados, esquema unifilar SVG dinámico y generación de memoria técnica oficial imprimible en formato A4 vertical.

2. **Motor de Eficiencia y Auditoría de Pérdidas Reales (IEC 61724):**
   - **Térmica de célula:** Calculada dinámicamente según irradiancia $G_{poa}$, $NOCT$ de ficha ($43\text{--}45\text{ °C}$) y coeficiente $\gamma_{Pmp}$.
   - **Mismatch y Tolerancia:** Leído directamente de la ficha del panel seleccionado ($0,8\%\text{ a }1,2\%$).
   - **Reflexión Angular (IAM):** Modelo físico de Martin-Ruiz/Fresnel con vidrio ARC ($b_0 = 0,05$).
   - **Suciedad (Soiling):** $0,00\%$ estrictamente garantizado mediante contrato de mantenimiento.
   - **Inversor & Batería:** Eficiencia europea nominal y rendimiento Round-Trip extraídos directamente de las tablas de datos de fabricante.
   - **Cableado:** Pérdidas Joule calculadas al 100% por ley de Ohm ($P = I^2 \cdot R$) sobre las líneas DC y AC.

---

## 📁 Estructura del Repositorio

```
.
├── index.html                       # SPA principal interactiva (HTML5 + CSS Tailwind + JS Vanilla)
├── showroom_solar_portable.html     # Versión portable 100% offline autocontenida
├── ingenieria.html                  # Estación técnica auxiliar de cálculo avanzado
├── test_showroom_wizard_e2e.py      # Batería de pruebas E2E automatizadas con Playwright
├── WORKFLOW_MAP.md                  # Mapa de arquitectura reactiva y trazabilidad del proyecto
├── subir-a-cloudflare/              # Paquete optimizado para despliegue directo en Cloudflare Pages
│   ├── index.html                   # SPA sincronizada
│   ├── ingenieria.html              # Estación auxiliar
│   ├── _headers                     # Cabeceras de seguridad (CSP, X-Frame-Options, HSTS)
│   └── functions/api/pvgis.js       # Proxy serverless para la API de PVGIS (evita bloqueos CORS)
└── README.md                        # Documentación técnica
```

---

## 🚀 Despliegue e Instalación

### Ejecución Local
Simplemente abre el archivo `index.html` o `showroom_solar_portable.html` en cualquier navegador moderno:
```bash
# Con cualquier servidor estático local (opcional):
npx serve .
# o con Python:
python -m http.server 8000
```

### Despliegue en Cloudflare Pages
La carpeta `subir-a-cloudflare/` está lista para ser conectada directamente a Cloudflare Pages:
1. Conecta este repositorio en el panel de **Cloudflare Pages**.
2. Configura el **Build output directory** como `subir-a-cloudflare`.
3. ¡Listo! El proxy serverless `functions/api/pvgis.js` gestionará las peticiones a la API europea de radiación solar sin incidencias de CORS.

---

## 🧪 Pruebas Automatizadas (E2E)

El proyecto cuenta con una suite completa de verificación visual y funcional con **Playwright**:
```bash
pip install playwright
playwright install
python test_showroom_wizard_e2e.py
```

La suite valida:
- Recorrido íntegro de los 8 pasos del wizard.
- Algoritmo de reparto de ramas y protección de sobretensión Multi-MPPT.
- Dimensionamiento de conductores según REBT.
- Cero errores en consola (`console.error`) y cero desbordamientos horizontales (`0px horizontal overflow`) en Desktop (1440px) y Móvil (390px).
- Generación de informe técnico oficial A4 en PDF.

---

## ⚖️ Normativa de Referencia
- **REBT (Reglamento Electrotécnico para Baja Tensión - RD 842/2002):**
  - **ITC-BT-19:** Instalaciones interiores o receptoras. Prescripciones generales.
  - **ITC-BT-20:** Instalaciones interiores o receptoras. Sistemas de instalación.
  - **ITC-BT-40:** Instalaciones generadoras de baja tensión (autoconsumo e interconexión).
- **UNE-HD 60364-5-52:** Cálculo de intensidades admisibles en conductores aislados según método de instalación y temperatura ambiente.
- **RD 244/2019:** Condiciones administrativas, técnicas y económicas del autoconsumo de energía eléctrica en España.
- **IEC 61724:** Monitorización de sistemas fotovoltaicos y cálculo de Performance Ratio (PR).

---

## 📄 Licencia
Proyecto desarrollado para uso profesional en dimensionamiento e ingeniería solar fotovoltaica.
