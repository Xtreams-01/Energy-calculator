# Showroom Solar ☀️ — Guía del Usuario

> **Configurador Solar Fotovoltaico Automatizado & Generador de Memoria Técnica Oficial (REBT)**  
> Diseña, auto-dimensiona y calcula la rentabilidad de una instalación de autoconsumo solar desde tu navegador: en **3 clics directos (Modo Rápido)** o en **8 pasos técnicos (Modo Ingeniería Avanzada)**, sin necesidad de instalar nada ni registrarte.

[![Estado](https://img.shields.io/badge/Estado-Listo%20para%20uso-success.svg)](#)
[![Release](https://img.shields.io/badge/Release-v4.7.1%20(Tutorial%20Datadis%20%2B%20Modo%20R%C3%A1pido%203%20Clics)-success.svg)](https://github.com/Xtreams-01/Energy-calculator/releases/tag/v4.7.1)
[![Normativa](https://img.shields.io/badge/Normativa-REBT%20ITC--BT--19%2F20%2F40%20%7C%20RD%20244%2F2019%20%7C%20CNMC%203%2F2020-blue.svg)](#)
[![Catálogo](https://img.shields.io/badge/Cat%C3%A1logo-30%20Paneles%20%E2%80%A2%2054%20Inversores%20%E2%80%A2%2034%20Bater%C3%ADas-orange.svg)](#)

[📥 **Descargar última versión portable (.html)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.7.1/showroom_solar_portable.html) | [📦 **Descargar paquete completo (.zip)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.7.1/Showroom_Solar_v4.7.1_Offline.zip) | [🚀 **Ver todas las Releases**](https://github.com/Xtreams-01/Energy-calculator/releases)

---

## ⚡ Novedades v4.7.1: Tutorial Pop-Up Interactivo de Datadis

1. **Tutorial Ilustrado de Datadis (Alta y Descarga Paso a Paso):**
   * **Fácil de encontrar pero sin estorbar:** Hemos añadido el botón discreto **`💡 ¿Cómo descargar?`** en la tarjeta de importación del Paso 1, y un enlace directo en la descripción de portada del Modo Rápido (*"¿cómo obtenerlo?"*). Si no te interesa o ya tienes tu archivo, no molesta en absoluto.
   * **Pop-up explicativo en 3 fases claras:**
     * **Qué necesitas (solo 2 datos):** Tu DNI/NIE y el código CUPS de cualquier factura de luz.
     * **Fase 1: Registro oficial en datadis.es (2 min):** Cómo darse de alta como particular o empresa, y verificar tu titularidad al instante por SMS o Certificado Digital/Cl@ve.
     * **Fase 2: Descarga del histórico:** Cómo seleccionar el último año completo, granularidad horaria (1h) y formato CSV.
     * **Fase 3: Carga en Showroom Solar:** Arrastrar o seleccionar el archivo para que el motor autodetecte la tarifa (2.0TD vs 3.0TD CNMC) y dimensione la instalación con máxima rentabilidad.
   * **Acciones integradas:** Botón directo para abrir `datadis.es` en nueva pestaña, descarga de plantilla CSV de ejemplo y cierre mediante la tecla `Escape` o el botón único `✕`.

2. **Modo Rápido ("Normie" en 3 Clics) vs Modo Ingeniería Avanzada (8 Pasos):**
   * **Selector inicial en Portada (Paso 0):** Tarjetas claras para elegir entre el *Modo Rápido (3 Clics)* (recomendado por defecto para propietarios y comerciales) o el *Modo Ingeniería Avanzada (8 Pasos)* (para técnicos e instaladores). Puedes conmutar en cualquier momento desde el botón `⚡ Rápido` / `🛠️ Avanzado` en la cabecera fija.
   * **Flujo directo en 3 clics:** Al completar el Paso 1 (Demanda / Datadis y preferencias de batería), pulsas **`🚀 Ver Estudio y Resultados →`** y **saltas directamente al Paso 7 (Showroom)**. La app auto-selecciona los paneles de máxima rentabilidad, el inversor comercial idóneo, optimiza las ramas Multi-MPPT, dimensiona los cables REBT e incluye la batería necesaria.
   * **Banner de felicitación y acceso a ajustes finos:** En el Paso 7 dispones de un banner con el botón **`🛠️ Abrir Modo Avanzado (8 Pasos)`**, además de accesos directos (*Personalizar Paneles*, *Personalizar Inversor*, *Personalizar Batería*, etc.) en cada tarjeta de equipo para modificar cualquier detalle. Al pulsar *Paso Anterior*, regresas de forma transparente al Paso 1.

3. **Dimensionamiento Dinámico de Batería por Objetivo de Autarquía (Paso 1 - Tarjeta 1D):**
   * En el Paso 1 configuras directamente:
     * **Batería LiFePO4:** `[ ⚡ Sin Batería ]` (solo solar directo diurno) o `[ 🔋 Con Batería LiFePO4 ]` (almacena excedentes para la noche).
     * **Objetivo de Autarquía / Cobertura:** Deslizador y botones de acceso rápido (**70% Equilibrado**, **85% Óptimo LiFePO4**, **95% Máxima Resiliencia**, **100% Autarquía Total**). El motor calcula la demanda nocturna real y auto-dimensiona los kWh de batería recomendados (Huawei LUNA, BYD, Tesla, etc.).
     * **Modalidad Legal RD 244/2019:** Elige entre *Con compensación simplificada de excedentes (con venta)*, *Sin excedentes (inyección cero / anti-vertido certificado)* o *Instalación 100% aislada de la red eléctrica (Off-Grid con 2 días de autonomía continua)*.

4. **Telemetría Real Datadis Inteligente y Bloqueo de Presets:**
   * Al importar tu curva real de Datadis / CSV, los selectores sintéticos se bloquean reactivamente para preservar la telemetría del contador sin adulteraciones.

5. **Detección Automática de Tarifa (`2.0TD` 3P vs `3.0TD` 6P CNMC):**
   * Desglose instantáneo de consumo según la Circular 3/2020 de la CNMC con 4 temporadas estacionales y noches/fines de semana en `P6`.

6. **Máxima Rentabilidad Técnico-Económica (VAN 25 años, Payback y Cashflow):**
   * Algoritmo de optimización que busca la configuración económicamente óptima sin incurrir en vertidos no compensados.

---

## 🧭 Cómo funciona la web

### A. Modo Rápido (3 Clics — Recomendado)
```
[1. Portada] ───────► [2. Consumo & Batería] ───────► [3. Showroom & Memoria A4]
Identificación       Ubicación, Factura o Datadis,     Resultados Óptimos, Dictamen
del Proyecto         Autarquía % y Modalidad Legal     REBT Conforme e Informe Descargable
```

### B. Modo Ingeniería Avanzada (8 Pasos Técnicos)
```
[Paso 0]  ─►  [Paso 1]  ─►  [Paso 2]  ─►  [Paso 3]  ─►  [Paso 4]  ─►  [Paso 5]  ─►  [Paso 6]  ─►  [Paso 7]
Proyecto      Datos,        30 Paneles    54 Invers.    Cables        34 Baterías   Ahorro        Memoria
Titular       Datadis &     & Tejado      & 12 MPPTs    REBT          (Opcional)    & Rentab.     PDF A4
              Tarifas
```

---

## 🛠️ Tecnologías y Arquitectura

* **Frontend:** HTML5 semántico, Tailwind CSS, JavaScript ES6+ modular sin frameworks pesados ni dependencias externas de compilación.
* **Gráficas:** Chart.js embebido de alto rendimiento.
* **Persistencia:** Guardado local seguro (`localStorage`) con importación/exportación JSON.
* **Pruebas y QA:** Suite completa E2E en Playwright con validación responsive (Desktop 1440px y Móvil 390px) en Español e Inglés con 0 desbordamientos (`overflow: 0px`).
* **Despliegue:** Optimizado para **Cloudflare Pages** (carpeta `subir-a-cloudflare/`) y 100% portable para uso offline (`showroom_solar_portable.html`).

---

## 📄 Licencia

Este proyecto está bajo licencia libre para fines formativos, técnicos y profesionales de ingeniería solar fotovoltaica en España y la Unión Europea.
