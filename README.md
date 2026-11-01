# Showroom Solar — Dimensionador Fotovoltaico & Memoria Técnica REBT

[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](#)
[![Version](https://img.shields.io/badge/Version-v4.3.0-blue.svg)](#)
[![Standards](https://img.shields.io/badge/Standards-REBT%20ITC--BT--19%2F20%2F40%20%7C%20IEC%2061724-orange.svg)](#)
[![Deploy](https://img.shields.io/badge/Deploy-Cloudflare%20Pages-f38020.svg)](#)

Aplicación web interactiva de alto rendimiento (SPA) diseñada para el **dimensionamiento fotovoltaico profesional, ingeniería eléctrica de cadenas Multi-MPPT, cálculo normativo de conductores según el REBT español y balance económico de amortización a 25 años**.

Estructurada para despliegue directo e instantáneo en **Cloudflare Pages** sin pasos de compilación.

---

## 📁 Estructura del Repositorio (Cloudflare Pages Ready)

```
.
├── index.html                   # SPA principal interactiva (HTML5 + Tailwind CSS + JS Vanilla)
├── ingenieria.html              # Estación técnica auxiliar de cálculo avanzado
├── _headers                     # Cabeceras de seguridad de Cloudflare (CSP, X-Frame-Options, HSTS)
├── functions/api/pvgis.js       # Proxy serverless Edge Function para la API de PVGIS (evita bloqueos CORS)
├── .gitignore                   # Exclusión de archivos locales de desarrollo
└── README.md                    # Documentación técnica
```

---

## 🚀 Despliegue en Cloudflare Pages

1. Conecta este repositorio en el panel de **Cloudflare Pages**.
2. **Production branch:** `main`
3. **Framework preset:** `None`
4. **Build command:** *(dejar en blanco)*
5. **Build output directory:** *(dejar en blanco o `/`)*
6. Al desplegar, Cloudflare Pages servirá `index.html` automáticamente y activará la Edge Function `functions/api/pvgis.js` para las consultas satelitales a PVGIS.

---

## 🌟 Características Técnicas

- **Wizard Interactivo en 8 Pasos:**
  - **Paso 0:** Expediente y metadatos del titular.
  - **Paso 1:** Consulta satelital PVGIS v5.2, curvas de demanda y tarifas 2.0TD (3 periodos).
  - **Paso 2:** Generador fotovoltaico Tier-1 con modelo térmico de célula Evans/PVGIS.
  - **Paso 3:** Multi-MPPT (1 a 6 seguidores), ventanas de tensión y comprobaciones a $-10\text{ °C}$ y $+70\text{ °C}$.
  - **Paso 4:** Cableado y normativa REBT (ITC-BT-19/20/40), intensidades admisibles UNE-HD 60364-5-52 y pérdidas Joule ($I^2 R$).
  - **Paso 5:** Acumulación LiFePO4 de alta tensión y autarquía.
  - **Paso 6:** Compensación de excedentes RD 244/2019, VAN, TIR, LCOE y marco fiscal (IVA 21% / IGIC 0%).
  - **Paso 7:** Cuadro de mando de resultados, unifilar SVG dinámico y memoria técnica A4 descargable/imprimible.
- **Motor de Pérdidas y Rendimiento (IEC 61724):** Cero estimaciones ficticias; cálculos analíticos reales o extracción directa de las fichas técnicas de los fabricantes.
- **Seguridad CSP:** Políticas de seguridad de contenido estrictas configuradas en `_headers`.

---

## ⚖️ Normativa de Referencia
- **REBT (Reglamento Electrotécnico para Baja Tensión - RD 842/2002)**: ITC-BT-19, ITC-BT-20, ITC-BT-40.
- **UNE-HD 60364-5-52**: Instalaciones eléctricas de baja tensión. Selección e instalación de canalizaciones.
- **RD 244/2019**: Condiciones administrativas, técnicas y económicas del autoconsumo eléctrico.
- **IEC 61724**: Photovoltaic system performance monitoring.
