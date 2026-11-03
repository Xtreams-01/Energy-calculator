# Showroom Solar ☀️ — Guía del Usuario

> **Configurador Solar Fotovoltaico Automatizado & Generador de Memoria Técnica Oficial (REBT)**  
> Diseña, auto-dimensiona y calcula la rentabilidad de una instalación de autoconsumo solar en 8 sencillos pasos desde tu navegador, sin necesidad de instalar nada ni registrarte.

[![Estado](https://img.shields.io/badge/Estado-Listo%20para%20uso-success.svg)](#)
[![Release](https://img.shields.io/badge/Release-v4.5.0%20(Auto--Pilot%20%2B%20Descargable)-success.svg)](https://github.com/Xtreams-01/Energy-calculator/releases/tag/v4.5.0)
[![Normativa](https://img.shields.io/badge/Normativa-REBT%20ITC--BT--19%2F20%2F40%20%7C%20RD%20244%2F2019%20%7C%20CNMC%203%2F2020-blue.svg)](#)
[![Catálogo](https://img.shields.io/badge/Cat%C3%A1logo-30%20Paneles%20%E2%80%A2%2054%20Inversores%20%E2%80%A2%2034%20Bater%C3%ADas-orange.svg)](#)

[📥 **Descargar última versión portable (.html)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.5.0/showroom_solar_portable.html) | [📦 **Descargar paquete completo (.zip)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.5.0/Showroom_Solar_v4.5.0_Offline.zip) | [🚀 **Ver todas las Releases**](https://github.com/Xtreams-01/Energy-calculator/releases)

---

## ⚡ Piloto Automático en Cascada y Autocorrección en 1 Clic

La aplicación cuenta con un motor de **Auto-Ajuste Integral (`⚡ Auto-Ajuste: ON`)** activado por defecto en la barra superior para automatizar al máximo la ingeniería del proyecto:

1. **Auto-ajuste total al cargar tu consumo o curva Datadis (Paso 1 → Paso 6):** En cuanto subes tu archivo de **Datadis**, introduces tu media de consumo/facturas o eliges un perfil (ej. `Comercio 3.0TD`), la app calcula automáticamente los paneles necesarios, selecciona el **inversor comercial óptimo** (microinversor, monofásico o trifásico), reparte las cadenas **MPPT** sin errores térmicos, dimensiona las secciones de **cableado REBT** (DC, AC y batería) y actualiza el presupuesto **CAPEX**.
2. **Re-escalado reactivo si cambias los paneles a tu gusto (Paso 2 → Paso 6):** Si decides poner más o menos paneles manualmente en el Paso 2 o cambiar de modelo/potencia de módulo, el inversor, los strings MPPT, los cables REBT y el presupuesto se reajustan solos al instante. *(Si prefieres bloquear un equipo concreto sin re-escalado automático, puedes conmutar a `🔒 Modo Manual` desde la cabecera).*
3. **Botón `🔧 Autocorregir` (Resolución de insuficiencias en 1 clic):** Si eliges un inversor específico que exige un mínimo de módulos en serie para arrancar en verano (por ejemplo, **mínimo 4 paneles** para superar $100\text{ V}$ a $+70\text{ °C}$) o si provocas una sobretensión, sobrecarga o caída de tensión REBT, aparece un botón directo **`🔧 Autocorregir`** (tanto en la alerta como en la barra inferior) que configura automáticamente esa disposición viable sin errores.

---

## 🧭 Cómo funciona la web paso a paso

```
[Paso 0]  ─►  [Paso 1]  ─►  [Paso 2]  ─►  [Paso 3]  ─►  [Paso 4]  ─►  [Paso 5]  ─►  [Paso 6]  ─►  [Paso 7]
Proyecto      Datos,        30 Paneles    54 Invers.    Cables        34 Baterías   Ahorro        Memoria
Titular       Datadis &     & Tejado      & 12 MPPTs    REBT          (Opcional)    & Rentab.     PDF A4
              Tarifas
```

### Paso 0: Identificación del Proyecto 📋
* Introduces el nombre del proyecto, titular, fecha y referencia de expediente. Todo se autoguarda en tu navegador y puede exportarse/importarse en `.JSON`.

### Paso 1: Ubicación PVGIS, Demanda Real (Datadis / 12 Meses) y Tarifas 🌍
1. **Ubicación satelital con PVGIS:** Cobertura de las **50 provincias y 2 ciudades autónomas** de España (detección fiscal automática de **IVA** en Península/Baleares, **IGIC** en Canarias e **IPSI** en Ceuta y Melilla) conectada a **JRC PVGIS v5.2**.
2. **Demanda eléctrica sin sesgos artificiales:**
   * **Importación nativa desde Datadis:** Sube directamente el `.csv` o `.json` oficial de **Datadis** (`;`, coma decimal `,`, horas `01:00..24:00` o cuartohorarias `00:15..24:00`). Simula sobre los días reales medidos y **auto-dimensiona toda la planta**.
   * **Editor de 12 Facturas (`Ene`–`Dic`):** Estacionalidad neutra por defecto (sin inflar verano sobre invierno) y edición mes a mes real.
3. **Tarifas domésticas e industriales:** **Fija (24h)**, **`2.0TD`** ($\le 15\text{ kW}$, 3 periodos) y **`3.0TD`** ($> 15\text{ kW}$, 6 periodos `P1`–`P6` según Circular 3/2020 de la CNMC).

### Paso 2: Selección de Paneles Solares y Tejado (30 Modelos Tier-1) ☀️
* **Catálogo ampliado (390 Wp a 715 Wp):** Organizado en gamas *Compacta/Full Black*, *Residencial Alta Eficiencia*, *Comercial/PYME* e *Industrial Bifacial G12* (**Meyer Burger, Hyundai, JA Solar, REC, Jinko, SunPower, Trina, LONGi, AIKO, DMEGC, Canadian Solar, Risen, Qcells, Huasun**) o modo manual libre.
* **Sincronización en vivo:** Bajo el selector de cantidad de módulos ves en tiempo real qué inversor, reparto de strings y sección de cable REBT se han auto-asignado al modificar el número de paneles.

### Paso 3: Inversor, Multi-MPPT (1 a 12 MPPTs) y Autocorrección ⚡
* **54 Inversores comerciales (0,8 kW a 125 kW):** Microinversores (**Hoymiles, Enphase**) para 1–4 paneles, monofásicos híbridos/string (**Huawei, Fronius, SMA, GoodWe, SolaX, Deye, Victron, Solis, Ingeteam**), trifásicos residenciales/PYME (**Kostal, Fronius Symo, Sungrow**) e industriales `3.0TD` hasta **125 kW y 12 seguidores MPPT**.
* **Optimizador exacto de ramas y botón `🔧 Autocorregir`:** Verifica tensión en frío ($-10\text{ °C}$), arranque/ventana MPPT en calor ($+70\text{ °C}$), intensidad máxima y ratio DC/AC, corrigiendo cualquier insuficiencia o desajuste con un clic.

### Paso 4: Cableado y Seguridad Normativa (REBT) 🔌
* Cálculo automático de secciones normalizadas Cu/Al según **REBT (ITC-BT-19, ITC-BT-20 e ITC-BT-40)** y **UNE-HD 60364-5-52**, garantizando $I_b \le I_z$, caída de tensión $\Delta u \le 1,5\%$ y cuantificación exacta de pérdidas por efecto Joule ($I^2R$).

### Paso 5: Baterías de Litio (34 Sistemas LV / HV / AC / C&I) 🔋
* **34 modelos reales LiFePO4 (1,2 kWh a 60 kWh):** Baja tensión 48 V (**Pylontech, Deye, Dyness, BYD LVL**), alta tensión híbrida (**Huawei LUNA2000 S0/S1, BYD HVS/HVM, Sungrow SBR, SolaX, GoodWe, SMA**), sistemas AC/All-in-One (**Enphase IQ, EcoFlow, Tesla Powerwall 2 y 3**) y racks industriales C&I, con **emparejamiento automático de ecosistema y bus DC/AC** respecto al inversor elegido.

### Paso 6 y Paso 7: Viabilidad Financiera (25 Años) y Memoria Técnica PDF A4 📄
* Compensación de excedentes **RD 244/2019**, **Payback, VAN, TIR y LCOE** a 25 años, esquema unifilar SVG dinámico y exportación directa a **Memoria Técnica A4 vertical imprimible en PDF**.

---

## 🔬 ¿Cómo se calculan la eficiencia y las pérdidas? (Cero datos genéricos)

Conforme a la norma **IEC 61724**, cada equipo utiliza **exclusivamente los parámetros reales de su propia ficha técnica de fabricante**:

| Pérdida / Rendimiento | Origen del Dato | ¿Cómo se obtiene? |
| :--- | :---: | :--- |
| **Pérdidas térmicas del panel** | `CALCULADO` | Modelo Evans/PVGIS según radiación, `NOCT` y coeficiente térmico propio ($\gamma_{Pmp}$) de cada panel. |
| **Mismatch y Tolerancia fabril** | `TABLA FICHA` | **100% propio de cada panel** (ej. SunPower Maxeon: $0,6\%$, REC/Meyer Burger: $0,7\%$, AIKO: $0,8\%$, LONGi: $1,0\%$, Hyundai: $1,2\%$). |
| **Reflexión solar angular (IAM)** | `CALCULADO` | Modelo óptico de Martin-Ruiz según inclinación y acimut de la cubierta. |
| **Suciedad (Soiling)** | `0,00%` | Garantizado mediante el contrato anual de mantenimiento y limpieza periódica (60 €/año). |
| **Rendimiento del Inversor** | `TABLA FICHA` | **100% propio de cada inversor** (ej. Victron MultiPlus-II: $95,0\%$, Hoymiles HMS: $96,5\%$, Fronius Primo: $97,6\%$, Huawei 10KTL: $98,4\%$, Sungrow SG125CX: $98,8\%$). |
| **Pérdidas Joule en cables** | `CALCULADO` | Ley de Ohm/Joule real ($P = I^2 \cdot R$) según longitud, material, sección y corriente de cada línea. |
| **Rendimiento de la Batería** | `TABLA FICHA` | **100% propio de cada batería** (ej. Enphase AC: $89,0\%$, Tesla Powerwall 2: $90,0\%$, Pylontech US5000: $94,5\%$, Huawei LUNA: $95,0\%$, BYD HVS/HVM: $95,6\%$). |

---

## ⚖️ Normativas Legales Aplicadas
* **Reglamento Electrotécnico para Baja Tensión (REBT - RD 842/2002):** ITC-BT-19, ITC-BT-20 e ITC-BT-40.
* **Circular 3/2020 de la CNMC:** Peajes de transporte y distribución `2.0TD` (3 periodos) y `3.0TD` (6 periodos).
* **Norma UNE-HD 60364-5-52 y 7-712:** Intensidades admisibles e instalaciones solares fotovoltaicas.
* **Real Decreto 244/2019 & Norma IEC 61724:** Autoconsumo eléctrico y balance energético normalizado.
