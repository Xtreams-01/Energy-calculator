# Showroom Solar ☀️ — Guía del Usuario

> **Configurador Solar Fotovoltaico Interactivo & Generador de Memoria Técnica Oficial (REBT)**  
> Diseña, dimensiona y calcula la rentabilidad de una instalación de autoconsumo solar en 8 sencillos pasos desde tu navegador, sin necesidad de instalar nada ni registrarte.

[![Estado](https://img.shields.io/badge/Estado-Listo%20para%20uso-success.svg)](#)
[![Release](https://img.shields.io/badge/Release-v4.3.0%20(Descargable)-success.svg)](https://github.com/Xtreams-01/Energy-calculator/releases/tag/v4.3.0)
[![Normativa](https://img.shields.io/badge/Normativa-REBT%20ITC--BT--19%2F20%2F40%20%7C%20RD%20244%2F2019-blue.svg)](#)
[![Cálculos](https://img.shields.io/badge/Motor-Física%20Real%20%26%20Fichas%20Técnicas-orange.svg)](#)

[📥 **Descargar última versión portable (.html)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.3.0/showroom_solar_portable.html) | [📦 **Descargar paquete completo (.zip)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.3.0/Showroom_Solar_v4.3.0_Offline.zip) | [🚀 **Ver todas las Releases**](https://github.com/Xtreams-01/Energy-calculator/releases)

---

## 🎯 ¿Para qué sirve esta aplicación?

Esta aplicación web está pensada tanto para **particulares** que quieren saber cuántos paneles solares necesitan en su tejado y cuánto van a ahorrar en la factura de la luz, como para **instaladores e ingenieros** que necesitan un dimensionamiento técnico riguroso con esquema unifilar y memoria técnica oficial descargable en PDF.

---

## 🧭 Cómo funciona la web paso a paso

La herramienta te guía a través de un recorrido interactivo de **8 pasos** en el que cada dato que introduces actualiza al instante todos los resultados:

```
[Paso 0]  ─►  [Paso 1]  ─►  [Paso 2]  ─►  [Paso 3]  ─►  [Paso 4]  ─►  [Paso 5]  ─►  [Paso 6]  ─►  [Paso 7]
Proyecto      Consumo       Paneles       Inversor      Cables        Batería       Ahorro        Memoria
Titular       & PVGIS       & Tejado      & Strings     REBT          (Opcional)    & Rentab.     PDF A4
```

---

### Paso 0: Identificación del Proyecto 📋
* **¿Qué haces aquí?** Introduces el nombre del proyecto, el titular de la instalación, la fecha y una referencia de expediente.
* **Guardar y continuar:** Todo lo que hagas se guarda automáticamente en tu navegador. También puedes pulsar en **"Importar / Exportar .JSON"** para descargar tu proyecto en un archivo y abrirlo más tarde en cualquier otro dispositivo.

---

### Paso 1: ¿Dónde está tu tejado y cuánto consumes? 🌍
* **Ubicación satelital con PVGIS:** Elige tu provincia o escribe la dirección/coordenadas. La web se conecta directamente con los satélites de la Comisión Europea (**JRC PVGIS v5.2**) para saber cuánta radiación solar real recibe tu tejado durante cada mes del año.
* **Tu factura de luz:** Indica tu consumo eléctrico anual o mensual (en kWh).
* **Tu tarifa de luz:** Selecciona si pagas un precio fijo por la energía o si tienes discriminación horaria con 3 tramos (Punta P1, Llano P2 y Valle P3).
* **Recomendación instantánea:** Al instante verás una gráfica interactiva de tu consumo frente a la producción solar, junto con la potencia recomendada (kWp) y el ahorro estimado.

---

### Paso 2: Selección de Paneles Solares y Tejado ☀️
* **Elige tus paneles:** Dispones de un catálogo con los modelos más eficientes del mercado (**LONGi, AIKO, Jinko Solar, Trina Solar, Canadian Solar, JA Solar, Hyundai**) o puedes definir libremente las medidas y características de cualquier otro panel.
* **Orientación e Inclinación:** Ajusta con controles deslizantes la inclinación de tu tejado (de 0° a 90°) y hacia dónde mira (Sur, Sureste, Suroeste, Este u Oeste).
* **Resultados en vivo:** La web calcula la superficie de tejado requerida en metros cuadrados ($m^2$) y la energía total que producirán tus paneles cada año.

---

### Paso 3: Inversor y Reparto de Paneles (Strings) ⚡
* **El inversor solar:** Es el equipo que transforma la energía de corriente continua generada por los paneles en corriente alterna para los electrodomésticos de tu hogar.
* **Inversores comerciales:** Selecciona entre modelos residenciales e industriales (**Huawei FusionSolar, Fronius, Sungrow, SMA, SolaX, Ingeteam**), tanto monofásicos (230 V) como trifásicos (400 V).
* **Reparto en cadenas (Multi-MPPT):** Indica cuántos paneles conectas a cada entrada (MPPT) o pulsa el botón **"⚡ Auto-repartir paneles en MPPTs"** para que el sistema lo distribuya de forma equilibrada.
* **Semáforo de seguridad eléctrica en tiempo real:**
  - ✅ **Tensión en frío ($-10\text{ °C}$):** Comprueba que en el día más frío del invierno la tensión no supere el límite máximo de seguridad del inversor.
  - ✅ **Ventana MPPT ($+70\text{ °C}$):** Verifica que en pleno verano a máxima temperatura el inversor trabaje en su zona de máxima eficiencia.
  - ✅ **Ratio DC / AC:** Confirma si la cantidad de paneles está equilibrada respecto a la potencia del inversor (óptimo entre el 100% y el 130%).

---

### Paso 4: Cableado y Seguridad Normativa (REBT) 🔌
* **Distancias:** Indica los metros de cable que separan los paneles del inversor (tramo DC) y los metros desde el inversor hasta el cuadro eléctrico general de tu casa (tramo AC).
* **Cálculo automático de sección:** La aplicación calcula el grosor mínimo de cable de cobre requerido según el **Reglamento Electrotécnico de Baja Tensión (ITC-BT-19, ITC-BT-20 e ITC-BT-40)** y la norma **UNE-HD 60364-5-52**.
* **Pérdidas mínimas:** Garantiza que la caída de tensión sea inferior al 1,5% para no desperdiciar energía en los cables.

---

### Paso 5: Baterías de Litio (Opcional) 🔋
* Si quieres almacenar el sobrante de energía solar durante el día para consumirlo por la noche, activa el interruptor de batería.
* Selecciona entre acumuladores de litio ferrofosfato (**LiFePO4**) de alta tensión (**Huawei LUNA2000, BYD Battery-Box HVS/HVM, Tesla Powerwall, Sungrow, SolaX**).
* **Autarquía solar:** Observa cómo tu grado de independencia de la red eléctrica sube drásticamente (típicamente del 50% al 85%).

---

### Paso 6: Estudio Económico y Rentabilidad a 25 Años 💶
* **Costes e Inversión:** Desglose del presupuesto estimado de equipos e instalación, con selección de régimen fiscal (Península IVA 21% o Canarias IGIC 0%).
* **Ahorro real anual:** Cálculo de cuánto dinero dejas de pagar a la compañía eléctrica en tu factura.
* **Venta de excedentes (RD 244/2019):** Estimación de los ingresos por la energía sobrante que inyectas a la red eléctrica.
* **Métricas financieras:**
  - **Periodo de Amortización (Payback):** Número de años necesarios para recuperar la inversión (habitualmente entre 4 y 7 años).
  - **VAN (Valor Actual Neto) y TIR (Tasa Interna de Retorno):** Rentabilidad financiera del proyecto a 25 años.
  - Gráfica interactiva de flujo de caja acumulado año a año.

---

### Paso 7: Resultados Finales y Memoria Técnica en PDF 📄
* **Dashboard visual:** Resumen ejecutivo de potencia, generación anual, autoconsumo directo y rendimiento global del sistema (Performance Ratio).
* **Esquema unifilar interactivo:** Diagrama eléctrico normalizado en formato vectorial SVG.
* **Descarga e Impresión A4:** Con un solo clic en el botón **"Imprimir / Guardar Memoria Técnica PDF"**, el navegador genera una memoria técnica oficial de ingeniería maquetada profesionalmente en formato A4 vertical, con cajetín de firma, lista para entregar a clientes o presentar ante organismos oficiales.

---

## 🔬 ¿Cómo se calculan la eficiencia y las pérdidas? (Cero datos inventados)

A diferencia de otros simuladores que usan porcentajes fijos o arbitrarios, esta web aplica un **motor de física y electrotecnia transparente** (conforme a la norma internacional **IEC 61724**):

| Pérdida / Rendimiento | Origen del Dato | ¿Cómo se obtiene? |
| :--- | :---: | :--- |
| **Pérdidas térmicas del panel** | `CALCULADO` | Modelo Evans/PVGIS según radiación real y el coeficiente térmico propio ($\gamma_{Pmp}$) de cada panel. |
| **Mismatch y Tolerancia fabril** | `TABLA FICHA` | **100% propio de cada panel.** Extraído de la ficha oficial de cada fabricante (ej. AIKO: $0,8\%$, Jinko: $0,9\%$, LONGi: $1,0\%$, JA Solar: $1,1\%$, Hyundai: $1,2\%$). |
| **Reflexión solar en el cristal** | `CALCULADO` | Modelo óptico de Martin-Ruiz según la inclinación del tejado y la posición del sol. |
| **Suciedad (Soiling)** | `0,00%` | Garantizado mediante el contrato anual de mantenimiento y limpieza periódica del sistema. |
| **Rendimiento del Inversor** | `TABLA FICHA` | **100% propio de cada inversor.** Rendimiento europeo nominal extraído directamente de la ficha técnica de cada modelo (ej. SMA Sunny Boy: $97,0\%$, Fronius Primo: $97,4\%$, Huawei 3KTL: $97,6\%$, Huawei 6KTL: $98,4\%$, Sungrow SG110CX: $98,7\%$). |
| **Pérdidas Joule en cables** | `CALCULADO` | Ley de Ohm/Joule real ($P = I^2 \cdot R$) en función de la longitud, sección del cable y corriente de trabajo. |
| **Rendimiento de la Batería** | `TABLA FICHA` | **100% propio de cada batería.** Eficiencia de ciclo completo (Round-Trip) según especificación del fabricante (ej. Tesla Powerwall 2: $90,0\%$, Pylontech US5000: $94,0\%$, Huawei LUNA2000: $95,0\%$, BYD HVS/HVM: $95,5\%$). |

---

## 💡 Consejos de uso y atajos rápidos

* **Modo Oscuro / Modo Claro:** Pulsa en el icono de luna/sol en la barra superior para cambiar el tema visual según prefieras.
* **Cambio de idioma:** Conmuta entre **Español (ES)** e **Inglés (EN)** al instante sin recargar la página.
* **Navegación flexible:** Puedes hacer clic en cualquiera de los pasos completados de la barra superior para volver atrás y cambiar cualquier dato; todo el proyecto se recalculará automáticamente.
* **Descarga de datos:** Guarda tus configuraciones pulsando en el botón **".JSON"** de la cabecera para recuperarlas en el futuro.

---

## ⚖️ Normativas Legales Aplicadas
* **Reglamento Electrotécnico para Baja Tensión (REBT - RD 842/2002):**
  - **ITC-BT-19:** Prescripciones generales para instalaciones interiores.
  - **ITC-BT-20:** Sistemas de instalación y tipos de canalización.
  - **ITC-BT-40:** Instalaciones generadoras de baja tensión y autoconsumo.
* **Norma UNE-HD 60364-5-52:** Cálculo de intensidades máximas admisibles en conductores.
* **Real Decreto 244/2019:** Regulación de las condiciones administrativas, técnicas y económicas del autoconsumo eléctrico en España.
* **Norma IEC 61724:** Monitorización y rendimiento de sistemas solares fotovoltaicos.
