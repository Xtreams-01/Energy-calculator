# Showroom Solar ☀️ — Guía del Usuario

> **Configurador Solar Fotovoltaico Interactivo & Generador de Memoria Técnica Oficial (REBT)**  
> Diseña, dimensiona y calcula la rentabilidad de una instalación de autoconsumo solar en 8 sencillos pasos desde tu navegador, sin necesidad de instalar nada ni registrarte.

[![Estado](https://img.shields.io/badge/Estado-Listo%20para%20uso-success.svg)](#)
[![Release](https://img.shields.io/badge/Release-v4.4.0%20(Descargable)-success.svg)](https://github.com/Xtreams-01/Energy-calculator/releases/tag/v4.4.0)
[![Normativa](https://img.shields.io/badge/Normativa-REBT%20ITC--BT--19%2F20%2F40%20%7C%20RD%20244%2F2019%20%7C%20CNMC%203%2F2020-blue.svg)](#)
[![Cálculos](https://img.shields.io/badge/Motor-Telemetr%C3%ADa%20Datadis%20%26%20Fichas%20T%C3%A9cnicas-orange.svg)](#)

[📥 **Descargar última versión portable (.html)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.4.0/showroom_solar_portable.html) | [📦 **Descargar paquete completo (.zip)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.4.0/Showroom_Solar_v4.4.0_Offline.zip) | [🚀 **Ver todas las Releases**](https://github.com/Xtreams-01/Energy-calculator/releases)

---

## 🎯 ¿Para qué sirve esta aplicación?

Esta aplicación web está pensada tanto para **particulares, comunidades energéticas y empresas** que quieren evaluar con rigor su autoconsumo solar a partir de curvas reales de contador (**Datadis**) o facturas mensuales, como para **instaladores e ingenieros** que necesitan un dimensionamiento técnico completo con esquema unifilar y memoria técnica oficial descargable en PDF.

---

## 🧭 Cómo funciona la web paso a paso

La herramienta te guía a través de un recorrido interactivo de **8 pasos** con orden causal (primero introduces tus datos reales y después obtienes las métricas derivadas):

```
[Paso 0]  ─►  [Paso 1]  ─►  [Paso 2]  ─►  [Paso 3]  ─►  [Paso 4]  ─►  [Paso 5]  ─►  [Paso 6]  ─►  [Paso 7]
Proyecto      Datos,        Paneles       Inversor      Cables        Batería       Ahorro        Memoria
Titular       Datadis &     & Tejado      & Strings     REBT          (Opcional)    & Rentab.     PDF A4
              Tarifas
```

---

### Paso 0: Identificación del Proyecto 📋
* **¿Qué haces aquí?** Introduces el nombre del proyecto, el titular de la instalación, la fecha y una referencia de expediente.
* **Guardar y continuar:** Todo lo que hagas se guarda automáticamente en tu navegador. También puedes pulsar en **"Importar / Exportar .JSON"** para descargar tu proyecto en un archivo y abrirlo más tarde en cualquier otro dispositivo.

---

### Paso 1: Ubicación PVGIS, Demanda Real (Datadis / 12 Meses) y Tarifas 🌍
1. **Ubicación satelital con PVGIS:** Elige cualquiera de las **50 provincias y 2 ciudades autónomas** de España (incluyendo detección fiscal automática de **IVA** en Península/Baleares, **IGIC** en Canarias e **IPSI** en Ceuta y Melilla) o escribe tu municipio/coordenadas. La web consulta la radiación solar de **JRC PVGIS v5.2**.
2. **Demanda eléctrica rigurosa y sin sesgos estacionales artificiales:**
   * **Opción A Recomendada — Importación directa desde Datadis:** Sube directamente el archivo `.csv` o `.json` descargado de **Datadis** o de tu distribuidora (admite formato oficial con `;`, coma decimal `,`, horas `01:00..24:00` o cuartohorarias `00:15..24:00`). El motor simulará hora a hora tus días reales medidos respetando tus cambios reales de consumo entre meses.
   * **Variabilidad Mensual Real (`Ene`–`Dic`):** Por defecto no se asume que consumas más en verano ni en invierno (estacionalidad neutra). Puedes introducir tus **12 facturas mensuales reales** o seleccionar el régimen climático real del suministro.
   * **Cautela metodológica en curvas sintéticas:** Si no dispones aún de fichero Datadis, puedes emplear perfiles orientativos ajustando el porcentaje real de consumo en ventana solar (`08:00–18:00`).
3. **Estructura tarifaria doméstica y comercial/industrial:**
   * **Tarifa Fija (24h):** Precio único las 24 horas.
   * **Peaje `2.0TD` ($\le 15\text{ kW}$, 3 periodos):** Punta (`P1`), Llano (`P2`) y Valle (`P3`).
   * **Peaje `3.0TD` ($> 15\text{ kW}$, 6 periodos `P1`–`P6`):** Calendario estacional oficial de la **Circular 3/2020 de la CNMC** para comercios, PYMEs e industria.
4. **Síntesis preliminar inferior:** Una vez definidos ubicación, demanda y precios, en la parte inferior obtienes la potencia solar orientativa (kWp), el ahorro preliminar y el balance comparativo de **12 meses** o **perfil 24h por mes** (el modelo concreto y número exacto de paneles se eligen en el Paso 2).

---

### Paso 2: Selección de Paneles Solares y Tejado ☀️
* **Elige tus paneles:** Dispones de un catálogo con los modelos más eficientes del mercado (**LONGi, AIKO, Jinko Solar, Trina Solar, Canadian Solar, JA Solar, Hyundai**) o puedes definir libremente las medidas y características de cualquier otro panel.
* **Orientación e Inclinación:** Ajusta con controles deslizantes la inclinación de tu tejado (de 0° a 90°) y hacia dónde mira (Sur, Sureste, Suroeste, Este u Oeste).
* **Resultados en vivo:** La web calcula el número óptimo de módulos para ese modelo, la superficie de tejado requerida en metros cuadrados ($m^2$) y la energía anual generada.

---

### Paso 3: Inversor y Reparto de Paneles (Strings) ⚡
* **Inversores comerciales:** Selecciona entre modelos residenciales, terciarios e industriales (**Huawei FusionSolar, Fronius, Sungrow, SMA, SolaX, GoodWe**), tanto monofásicos (230 V) como trifásicos (400 V).
* **Reparto en cadenas (Multi-MPPT):** Indica cuántos paneles conectas a cada entrada (MPPT) o pulsa el botón **"⚡ Auto-repartir paneles en MPPTs"** para que el sistema lo distribuya de forma equilibrada.
* **Semáforo de seguridad eléctrica en tiempo real:**
  - ✅ **Tensión en frío ($-10\text{ °C}$):** Comprueba que en el día más frío del invierno la tensión no supere el límite máximo de seguridad del inversor.
  - ✅ **Ventana MPPT ($+70\text{ °C}$):** Verifica que en pleno verano a máxima temperatura el inversor trabaje en su zona de máxima eficiencia.
  - ✅ **Ratio DC / AC:** Confirma si la cantidad de paneles está equilibrada respecto a la potencia del inversor (óptimo entre el 100% y el 130%).

---

### Paso 4: Cableado y Seguridad Normativa (REBT) 🔌
* **Distancias:** Indica los metros de cable que separan los paneles del inversor (tramo DC) y los metros desde el inversor hasta el cuadro eléctrico general (tramo AC).
* **Cálculo automático de sección:** La aplicación calcula la sección normalizada mínima según el **Reglamento Electrotécnico de Baja Tensión (ITC-BT-19, ITC-BT-20 e ITC-BT-40)** y la norma **UNE-HD 60364-5-52**.
* **Pérdidas mínimas:** Garantiza el cumplimiento estricto de caída de tensión ($\Delta u \le 1,5\%$) y cuantifica las pérdidas reales por efecto Joule.

---

### Paso 5: Baterías de Litio (Opcional) 🔋
* Si quieres almacenar el sobrante de energía solar diurna para consumirlo por la noche, activa el interruptor de batería.
* Selecciona entre acumuladores de litio ferrofosfato (**LiFePO4**) de alta tensión (**Huawei LUNA2000, BYD Battery-Box HVS/HVM, Tesla Powerwall, Sungrow, SolaX, Pylontech**).
* **Autarquía solar:** Observa cómo evoluciona tu grado de cobertura sobre la curva real o mensual de tu suministro.

---

### Paso 6: Estudio Económico y Rentabilidad a 25 Años 💶
* **Costes e Inversión:** Desglose del presupuesto estimado de equipos e instalación, con régimen fiscal adaptable (**Península y Baleares IVA 21%**, **Canarias IGIC 0%** o **Ceuta y Melilla IPSI 4%/1%**).
* **Compensación de excedentes (RD 244/2019):** Estimación mensual con tope regulatorio sobre el término de energía consumido cada mes.
* **Métricas financieras:** Payback descontado/simple, **VAN (Valor Actual Neto)**, **TIR**, **LCOE** y gráfica de flujo de caja acumulado a 25 años.

---

### Paso 7: Resultados Finales y Memoria Técnica en PDF 📄
* **Dashboard visual:** Resumen ejecutivo de potencia, generación anual, autoconsumo directo y rendimiento global del sistema (Performance Ratio).
* **Esquema unifilar interactivo:** Diagrama eléctrico normalizado en formato vectorial SVG.
* **Descarga e Impresión A4:** Con un solo clic en **"Imprimir / Guardar Memoria Técnica PDF"**, el navegador genera una memoria técnica de ingeniería maquetada en formato A4 vertical, trazando el origen de la curva de carga, la tarifa (`Fija`, `2.0TD` o `3.0TD`) y el cumplimiento REBT.

---

## 🔬 ¿Cómo se calculan la eficiencia y las pérdidas? (Cero datos inventados)

A diferencia de otros simuladores que usan porcentajes fijos o arbitrarios, esta web aplica un **motor de física y electrotecnia transparente** (conforme a la norma internacional **IEC 61724**):

| Pérdida / Rendimiento | Origen del Dato | ¿Cómo se obtiene? |
| :--- | :---: | :--- |
| **Pérdidas térmicas del panel** | `CALCULADO` | Modelo Evans/PVGIS según radiación real y el coeficiente térmico propio ($\gamma_{Pmp}$) de cada panel. |
| **Mismatch y Tolerancia fabril** | `TABLA FICHA` | **100% propio de cada panel.** Extraído de la ficha oficial de cada fabricante (ej. AIKO: $0,8\%$, Jinko: $0,9\%$, LONGi: $1,0\%$, JA Solar: $1,1\%$, Hyundai: $1,2\%$). |
| **Reflexión solar en el cristal** | `CALCULADO` | Modelo óptico de Martin-Ruiz según la inclinación del tejado y la posición del sol. |
| **Suciedad (Soiling)** | `0,00%` | Garantizado mediante el contrato anual de mantenimiento y limpieza periódica del sistema (60 €/año). |
| **Rendimiento del Inversor** | `TABLA FICHA` | **100% propio de cada inversor.** Rendimiento europeo nominal extraído directamente de la ficha técnica de cada modelo (ej. SMA Sunny Boy: $97,0\%$, Fronius Primo: $97,4\%$, Huawei 3KTL: $97,6\%$, Huawei 6KTL: $98,4\%$, Sungrow SG110CX: $98,7\%$). |
| **Pérdidas Joule en cables** | `CALCULADO` | Ley de Ohm/Joule real ($P = I^2 \cdot R$) en función de la longitud, sección del cable y corriente de trabajo. |
| **Rendimiento de la Batería** | `TABLA FICHA` | **100% propio de cada batería.** Eficiencia de ciclo completo (Round-Trip) según especificación del fabricante (ej. Tesla Powerwall 2: $90,0\%$, Pylontech US5000: $94,0\%$, Huawei LUNA2000: $95,0\%$, BYD HVS/HVM: $95,5\%$). |

---

## ⚖️ Normativas Legales Aplicadas
* **Reglamento Electrotécnico para Baja Tensión (REBT - RD 842/2002):** ITC-BT-19, ITC-BT-20 e ITC-BT-40.
* **Circular 3/2020 de la CNMC:** Peajes de transporte y distribución `2.0TD` (3 periodos) y `3.0TD` (6 periodos).
* **Norma UNE-HD 60364-5-52:** Cálculo de intensidades máximas admisibles en conductores.
* **Real Decreto 244/2019:** Condiciones administrativas, técnicas y económicas del autoconsumo en España.
* **Norma IEC 61724:** Monitorización y análisis de rendimiento de sistemas solares fotovoltaicos.
