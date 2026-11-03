# Showroom Solar ☀️ — Guía del Usuario

> **Configurador Solar Fotovoltaico Automatizado & Generador de Memoria Técnica Oficial (REBT)**  
> Diseña, auto-dimensiona y calcula la rentabilidad de una instalación de autoconsumo solar en 8 sencillos pasos desde tu navegador, sin necesidad de instalar nada ni registrarte.

[![Estado](https://img.shields.io/badge/Estado-Listo%20para%20uso-success.svg)](#)
[![Release](https://img.shields.io/badge/Release-v4.6.0%20(Datadis%203.0TD%20%2B%20Rentabilidad%20%C3%93ptima)-success.svg)](https://github.com/Xtreams-01/Energy-calculator/releases/tag/v4.6.0)
[![Normativa](https://img.shields.io/badge/Normativa-REBT%20ITC--BT--19%2F20%2F40%20%7C%20RD%20244%2F2019%20%7C%20CNMC%203%2F2020-blue.svg)](#)
[![Catálogo](https://img.shields.io/badge/Cat%C3%A1logo-30%20Paneles%20%E2%80%A2%2054%20Inversores%20%E2%80%A2%2034%20Bater%C3%ADas-orange.svg)](#)

[📥 **Descargar última versión portable (.html)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.6.0/showroom_solar_portable.html) | [📦 **Descargar paquete completo (.zip)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.6.0/Showroom_Solar_v4.6.0_Offline.zip) | [🚀 **Ver todas las Releases**](https://github.com/Xtreams-01/Energy-calculator/releases)

---

## ⚡ Novedades v4.6.0: Telemetría Datadis Inteligente, Bloques 3.0TD y Rentabilidad Óptima

1. **Bloqueo Inteligente de Presets al Cargar Datadis:**
   * Al importar el archivo oficial de **Datadis** o curva de contador real, los botones de presets sintéticos (*Piso*, *Vivienda Familiar*, *Hogar + VE*, *Comercio 3.0TD*), el deslizador de consumo y los perfiles horarios quedan **bloqueados y pausados de forma reactiva**, garantizando que los cálculos se alimenten exclusivamente de la telemetría real del contador sin adulteraciones.
   * Si deseas regresar al dimensionamiento sintético, basta con pulsar **`Quitar CSV`** y los controles se restauran al instante.
2. **Autodetección de Tarifa (`2.0TD` vs `3.0TD`) y Cálculo de Bloques de Energía:**
   * La app inspecciona las cabeceras, columnas, nombres y picos de potencia ($P_{max} > 15\text{ kW}$) o consumos anuales ($> 15.000\text{ kWh/a}$) del archivo.
   * Si detecta un suministro $\le 15\text{ kW}$, activa la tarifa **`2.0TD`** y calcula los 3 periodos (`P1`, `P2`, `P3`).
   * Si detecta un suministro $> 15\text{ kW}$ o comercial/industrial, conmuta automáticamente a **`3.0TD`** y desglosa los 6 periodos (`P1`, `P2`, `P3`, `P4`, `P5`, `P6`) respetando el calendario estacional de 4 temporadas y noches/fines de semana en `P6` de la **Circular 3/2020 de la CNMC**.
3. **Dimensionamiento Estándar de Máxima Rentabilidad Global (`AutoOptimizer`):**
   * El dimensionamiento por defecto (y el botón *Usar Recomendada*) ya no aplica un porcentaje plano arbitrario: realiza un **barrido técnico-económico multiobjetivo** simulando el flujo de caja a 25 años.
   * Selecciona el número exacto de paneles que **maximiza el Valor Actual Neto (VAN €)**, **minimiza el Payback** y **optimiza el autoconsumo diurno**, previniendo excedentes vertidos masivos que quedarían topados por el **RD 244/2019**.
4. **Piloto Automático y Autocorrección en 1 Clic:**
   * Cascada continua en vivo desde el Paso 1 (Demanda / Datadis → Paneles Óptimos → Inversor Óptimo → Reparto Multi-MPPT → Cables REBT → Batería → CAPEX).
   * Botón contextual y global **`🔧 Autocorregir`** para solucionar instantáneamente cualquier alerta térmica de arranque, sobretensión o sobrecarga.

---

## 🧭 Cómo funciona la web paso a paso

```
[Paso 0]  ─►  [Paso 1]  ─►  [Paso 2]  ─►  [Paso 3]  ─►  [Paso 4]  ─►  [Paso 5]  ─►  [Paso 6]  ─►  [Paso 7]
Proyecto      Datos,        30 Paneles    54 Invers.    Cables        34 Baterías   Ahorro        Memoria
Titular       Datadis &     & Tejado      & 12 MPPTs    REBT          (Opcional)    & Rentab.     PDF A4
              Tarifas
```

### Paso 0: Identificación del Proyecto 📋
* Introduces el nombre del proyecto, titular, fecha y referencia de expediente. Todo se autoguarda en tu navegador (`localStorage`) y puede exportarse/importarse en formato `.JSON`.

### Paso 1: Ubicación PVGIS, Demanda Real (Datadis / 12 Meses) y Tarifas 🌍
1. **Ubicación satelital con PVGIS:** Cobertura de las **50 provincias y 2 ciudades autónomas** de España (detección fiscal automática de **IVA 21%** en Península/Baleares, **IGIC 0%/3%** en Canarias e **IPSI 4%/1%** en Ceuta y Melilla) conectada a **JRC PVGIS v5.2**.
2. **Demanda eléctrica sin sesgos artificiales:**
   * **Importación nativa desde Datadis:** Acepta directamente el `.csv` o `.json` oficial de **Datadis** (delimitador `;`, coma decimal `,`, convención `01:00..24:00` o cuartohoraria `00:15..24:00`). Detecta tarifa y calcula bloques de energía en caliente.
   * **Editor de 12 Facturas (`Ene`–`Dic`):** Estacionalidad neutra por defecto (sin inflar verano sobre invierno) y edición mes a mes real.
3. **Tarifas domésticas e industriales:** **Fija (24h)**, **`2.0TD`** ($\le 15\text{ kW}$, 3 periodos) y **`3.0TD`** ($> 15\text{ kW}$, 6 periodos `P1`–`P6` según Circular 3/2020 de la CNMC).

### Paso 2: Selección de Paneles Solares y Tejado (30 Modelos Tier-1) ☀️
* **Catálogo ampliado (390 Wp a 715 Wp):** Organizado en gamas *Compacta/Full Black*, *Residencial Alta Eficiencia*, *Comercial/PYME* e *Industrial Bifacial G12* (**Meyer Burger, Hyundai, JA Solar, REC, Jinko, SunPower, Trina, LONGi, AIKO, DMEGC, Canadian Solar, Risen, Qcells, Huasun**) o modo manual libre.
* **Sincronización en vivo:** Bajo el selector de cantidad de módulos ves en tiempo real qué inversor, reparto de strings y sección de cable REBT se han auto-asignado al modificar el número de paneles.

### Paso 3: Inversor, Multi-MPPT (1 a 12 MPPTs) y Autocorrección ⚡
* **54 Inversores comerciales (0,8 kW a 125 kW):** Microinversores (**Hoymiles, Enphase**) para 1–4 paneles, monofásicos híbridos/string (**Huawei, Fronius, SMA, GoodWe, SolaX, Deye, Victron, Solis, Ingeteam**), trifásicos residenciales/PYME (**Kostal, Fronius Symo, Sungrow**) e industriales `3.0TD` hasta **125 kW y 12 seguidores MPPT**.
* **Optimizador exacto de ramas y botón `🔧 Autocorregir`:** Verifica tensión en frío ($-10\text{ °C}$), arranque/ventana MPPT en calor ($+70\text{ °C}$), intensidad máxima y ratio DC/AC, corrigiendo cualquier insuficiencia o desajuste con un clic.

### Paso 4: Cableado y Cumplimiento Normativo REBT 🔌
* **Normativa Española:** Caída de tensión máxima $\le 1.5\%$ en DC (ITC-BT-40), $\le 1.5\%$ en AC (ITC-BT-19) y $\le 1.0\%$ en tramo de batería, con comprobación de corriente admisible ($I_z \ge 1.25 \cdot I_{sc}$ en DC e $I_z \ge 1.25 \cdot I_{ac}$ en AC).
* **Auto-selección de sección de cable y esquema unifilar SVG:** Muestra el calibre óptimo en cobre libre de halógenos y genera el diagrama esquemático con protecciones sobretensiones, magnetotérmico y diferencial.

### Paso 5: Almacenamiento con Baterías LiFePO4 (34 Modelos Opcionales) 🔋
* **Baterías Tier-1 (1,2 a 60 kWh):** Modelos de baja tensión (48V LV), alta tensión (HV) y acoplamiento AC (**Pylontech, Deye, Dyness, BYD, Huawei LUNA S0/S1, Sungrow, SolaX, GoodWe, Enphase, Tesla Powerwall 2/3**).
* **Cálculo de cobertura nocturna y modo aislada:** Comparativa de factura y balance con y sin batería.

### Paso 6: Marco Legal (RD 244/2019) y Viabilidad Financiera 💰
* **Mecanismos de compensación simplificada:** Balance mensual con límite legal regulado (factura de energía hasta 0 € sin compensar término de potencia) o venta a mercado.
* **Métricas a 25 años:** Ahorro anual estimado (€), Payback simple y descontado (años), VAN (€) y TIR (%).

### Paso 7: Showroom de Resultados y Memoria Técnica A4 Vertical 📄
* **Panel ejecutivo:** 6 KPIs gigantes, gráficas anuales y desgloses mensuales de generación, consumo y excedentes.
* **Memoria Técnica A4 Oficial:** Diseñada bajo `@media print` para imprimir en formato vertical limpio con tablas completas, firmas de autor y gráficos PNG embebidos.

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
