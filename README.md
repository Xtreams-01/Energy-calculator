# Memoria Técnica y Manual de Operación — Showroom Solar (v4.8.0)

> **Plataforma de Simulación Fotovoltaica Determinista, Modelado Volumétrico 3D de Cubiertas, Raytracing de Sombras Cercanas y Remotas PVGIS, Trazado de Cableado y Conectores MC4, Validación Electrotécnica REBT y Análisis de Viabilidad Económico-Financiera.**  
> Aplicación de cálculo y generación automatizada de memorias técnicas de diseño para instalaciones de autoconsumo solar en España, bajo estricto cumplimiento del **Real Decreto 244/2019**, el **Reglamento Electrotécnico para Baja Tensión (REBT)** y la **Circular 3/2020 de la CNMC**.

[![Estado](https://img.shields.io/badge/Estado-Producci%C3%B3n%20Operativa-success.svg)](#)
[![Versión](https://img.shields.io/badge/Versi%C3%B3n-v4.8.0%20(Estudio%203D%20%7C%20Raytracing%20PVGIS%20%7C%20Cables%20MC4)-blue.svg)](https://github.com/Xtreams-01/Energy-calculator/releases/tag/v4.8.0)
[![Normativa](https://img.shields.io/badge/Normativa-RD%20244%2F2019%20%7C%20REBT%20ITC--BT--19%2F20%2F40%20%7C%20CNMC%203%2F2020-navy.svg)](#)
[![Catálogo](https://img.shields.io/badge/Cat%C3%A1logo-30%20M%C3%B3dulos%20%E2%80%A2%2054%20Inversores%20%E2%80%A2%2034%20Bater%C3%ADas-orange.svg)](#)

[📥 **Descargar Versión Portable Autocontenida (.html)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.8.0/showroom_solar_portable.html) | [📦 **Descargar Paquete Técnico Completo (.zip)**](https://github.com/Xtreams-01/Energy-calculator/releases/download/v4.8.0/Showroom_Solar_v4.8.0_Offline.zip) | [📋 **Repositorio Oficial y Versiones**](https://github.com/Xtreams-01/Energy-calculator/releases)

---

## 1. Marco Normativo y Disposiciones Legales de Aplicación

El software ejecuta sus algoritmos de dimensionamiento, verificación física y evaluación económica conforme a los siguientes textos legales y normas técnicas:

1. **Real Decreto 244/2019, de 5 de abril:** Regula las condiciones administrativas, técnicas y económicas del autoconsumo de energía eléctrica en España. Implementa las modalidades de autoconsumo con excedentes acogidas a compensación simplificada (artículo 14), sin excedentes (instalaciones con sistema antivertido homologado conforme a la ITC-BT-40) e instalaciones aisladas de la red de distribución.
2. **Real Decreto 842/2002, de 2 de agosto (Reglamento Electrotécnico para Baja Tensión - REBT):**
   * **ITC-BT-40 (Instalaciones generadoras de baja tensión):** Prescripciones para interconexión, dispositivos de corte omnipolar, protecciones de sobretensión e intensidades de cortocircuito en corriente continua (DC).
   * **ITC-BT-19 e ITC-BT-20 (Instalaciones interiores o receptoras):** Cálculo de conductores, intensidades máximas admisibles ($I_z$) según método de instalación y caída de tensión máxima admisible ($\Delta u \le 1.5\%$ en DC y $\Delta u \le 1.5\%$ en AC).
3. **Normas UNE y Estándares Internacionales:**
   * **UNE-HD 60364-7-712:** Instalaciones eléctricas en edificios. Parte 7-712: Requisitos para instalaciones y emplazamientos especiales. Sistemas de suministro de energía solar fotovoltaica (FV).
   * **UNE-HD 60364-5-52:** Selección e instalación de equipos eléctricos. Canalizaciones y cálculo térmico de conductores.
   * **IEC 61724 (Norma UNE-EN 62446):** Monitorización de sistemas fotovoltaicos, directrices para la medida, intercambio y análisis de datos de rendimiento y Performance Ratio (PR).
4. **Circular 3/2020, de 15 de enero, de la Comisión Nacional de los Mercados y la Competencia (CNMC):** Metodología para el cálculo de los peajes de transporte y distribución de electricidad. Se aplica la diferenciación horaria y de potencia para peajes en baja tensión: **2.0TD** (3 periodos de energía: Punta, Llano y Valle) y **3.0TD** (6 periodos de energía: P1 a P6, con calendario de 4 temporadas estacionales y fines de semana en P6).
5. **Régimen Fiscal Territorial:** Aplicación diferenciada de tipos impositivos indirectos según demarcación: **IVA 21%** (Península y Baleares), **IGIC 0% / 3%** (Comunidad Autónoma de Canarias, según Ley 4/2012) e **IPSI 4% / 1%** (Ciudades Autónomas de Ceuta y Melilla).

---

## 2. Arquitectura de Motores de Cálculo y Algoritmia Determinista

La aplicación opera íntegramente en el cliente mediante un motor determinista en JavaScript ES6+, estructurado en módulos desacoplados y coordinados a través de un estado reactivo centralizado (`pv_project_state_v1`):

```
                                  ARQUITECTURA DEL SISTEMA
                                             │
      ┌──────────────────────────────────────┴──────────────────────────────────────┐
      ▼                                                                             ▼
[MÓDULO DE ENTRADA Y TELEMETRÍA]                                          [MÓDULO DE RADIACIÓN SATELITAL]
 ├── Parseador Datadis (CSV/JSON oficial)                                  ├── PVGIS-SARAH2 / ERA5 (JRC)
 ├── Clasificador Arquetípico CNMC 3/2020                                  ├── Matriz Geográfica (50p + 2CA)
 └── Bloqueo Reactivo de Presets Sintéticos                                └── Corrección Térmica NOCT/NMOT
      │                                                                             │
      └──────────────────────────────────────┬──────────────────────────────────────┘
                                             ▼
                             [MOTOR DE BALANCE ENERGÉTICO HORARIO]
                              ├── Simulación 8.760 horas (Generación vs Demanda)
                              ├── Autoconsumo Instantáneo vs Excedentes Vertidos
                              └── Gestión de Baterías LiFePO4 (Ciclado y Autarquía)
                                             │
      ┌──────────────────────────────────────┴──────────────────────────────────────┐
      ▼                                                                             ▼
[COMPATIBILIDAD ELÉCTRICA MPPT]                                           [VERIFICACIÓN NORMATIVA REBT]
 ├── Solver DP de Agrupación de Cadenas                                    ├── Criterio Térmico: Ib ≤ Iz (UNE 60364-5-52)
 ├── Validación Térmica: Voc(-10°C) ≤ Vmax                                 ├── Caída de Tensión: Δu ≤ 1.5% (ITC-BT-19/40)
 ├── Arranque y MPPT: Vmp(+70°C) ≥ Vmin                                    └── Pérdidas Joule Conductor (I²R)
 └── Ratio de Potencia DC/AC (Inversor)                                    └── Dimensionamiento Sección Cu (mm²)
                                             │
                                             ▼
                             [EVALUACIÓN ECONÓMICA Y MEMORIA A4]
                              ├── Flujo de Caja Descontado 25 años (DCF)
                              ├── VAN (€), TIR (%), Payback Descontado y LCOE
                              └── Memoria Técnica Normalizada UNE-EN ISO 5457 (A4)
```

### 2.1. Módulo de Radiación y Simulación Física (PVGIS JRC)
* **Datos de Radiación:** Conexión vía API REST al servidor del **Joint Research Centre (JRC)** de la Comisión Europea (base de datos PVGIS-SARAH2 / PVGIS-ERA5).
* **Parámetros Geométricos:** Cálculo de irradiación global sobre plano inclinado ($G_{poa}$) en función de latitud, longitud, inclinación ($\beta$) y acimut ($\gamma$).
* **Comportamiento Térmico:** Corrección de rendimiento en célula en función de la temperatura de operación ($T_{cell}$):
  $$T_{cell} = T_{amb} + \left(\frac{\text{NOCT} - 20}{800}\right) \cdot G_{poa}$$
  $$P_{dc} = P_{stc} \cdot \left[1 + \gamma_{Pmp} \cdot (T_{cell} - 25)\right] \cdot \left(\frac{G_{poa}}{1000}\right)$$

### 2.2. Motor de Telemetría Real y Tratamiento de Archivos Datadis
* **Ingesta de Curvas Reales:** Procesamiento determinista de archivos `.csv` y `.json` descargados de la plataforma oficial **Datadis** o distribuidoras locales (Endesa e-distribución, Iberdrola i-DE, Naturgy UFD, EDP E-Redes).
* **Compatibilidad de Formatos:** Admite separador de campos punto y coma (`;`) o coma (`,`), coma decimal española (`,`), identificador CUPS de 20 a 22 caracteres, y marcas temporales en formato horario (`01:00` a `24:00`) o cuartohorario (`00:15` a `24:00`).
* **Autodetección Tarifaria (2.0TD vs 3.0TD):** Detección automática mediante metadatos y análisis de picos de potencia ($P_{max} > 15\text{ kW}$) o volumen anual ($E_{anual} > 15.000\text{ kWh}$).
* **Desglose en Periodos CNMC:**
  * **Tarifa 2.0TD:** Asignación horaria a periodos Punta (P1), Llano (P2) y Valle (P3).
  * **Tarifa 3.0TD:** Clasificación horaria en 6 periodos (P1 a P6) considerando el calendario de 4 temporadas de la Circular 3/2020 de la CNMC (Alta, Media-Alta, Media y Baja) y fines de semana íntegros en P6.

### 2.3. Algoritmo de Optimización Técnico-Económica (`AutoOptimizer`)
A diferencia de los dimensionadores simplificados basados en porcentajes fijos, el sistema ejecuta un barrido multiobjetivo evaluando configuraciones admisibles de módulos fotovoltaicos:
* **Función Objetivo:** Maximizar el Valor Actual Neto a 25 años ($VAN_{25}$) sujeto a restricciones técnicas:
  $$\max_{N_{mod}} VAN_{25} = \sum_{t=1}^{25} \frac{CF_t}{(1 + r)^t} - \text{CAPEX}_{inicial}$$
  $$\text{sujeto a:} \quad V_{oc}(-10\text{ °C}) \le V_{max,inv}, \quad V_{mp}(+70\text{ °C}) \ge V_{min,mppt}, \quad \text{Excedentes}_{compensables} \le \text{Tope RD 244/2019}$$
* **Evitación de Sobreexcedentes Improductivos:** Previene el sobredimensionamiento innecesario del campo generador, dado que el artículo 14 del RD 244/2019 estipula que el valor económico de los excedentes nunca podrá superar el importe del término de energía facturado en el periodo mensual.

### 2.4. Solver de Compatibilidad Eléctrica y Topología Multi-MPPT
* **Programación Dinámica de Agrupaciones:** Algoritmo exacto para repartir $N$ módulos en $M$ seguidores MPPT independientes, considerando el número máximo de entradas en paralelo y módulos en serie por rama ($S_{min} \le S_i \le S_{max}$).
* **Comprobación de Tensiones Críticas (UNE-HD 60364-7-712):**
  * Tensión máxima de circuito abierto a temperatura mínima de diseño ($-10\text{ °C}$):
    $$V_{oc,max} = N_s \cdot V_{oc,stc} \cdot \left[1 + \beta_{Voc} \cdot (-10 - 25)\right] \le V_{max,inv}$$
  * Tensión mínima de máxima potencia a temperatura máxima de célula ($+70\text{ °C}$):
    $$V_{mp,min} = N_s \cdot V_{mp,stc} \cdot \left[1 + \gamma_{Pmp} \cdot (+70 - 25)\right] \ge V_{min,mppt}$$
* **Intensidad de Cortocircuito y Factor de Seguridad:**
  $$I_{sc,total} = N_p \cdot I_{sc,mod} \cdot 1.25 \le I_{sc,max\_mppt}$$

### 2.5. Verificación Electrotécnica de Conductores (REBT)
Cálculo analítico individualizado para los tres tramos de la instalación: **Línea Principal DC**, **Línea de Conexión AC** y **Línea de Enlace a Baterías**:
* **Criterio de Capacidad Térmica:**
  $$I_z \ge I_b \cdot f_c$$
  Donde $I_z$ es la intensidad admisible del cable (cobre clase 5 con aislamiento XLPO/EPR o PVC según UNE-HD 60364-5-52), $I_b$ es la corriente de diseño ($1.25 \cdot I_{sc}$ en DC; $I_{ac,nom}$ en AC) y $f_c$ son los coeficientes de corrección por temperatura ambiente y agrupamiento.
* **Criterio de Caída de Tensión Admisible:**
  * Tramo monofásico AC / DC bipolar:
    $$\Delta u (\%) = \frac{2 \cdot L \cdot I \cdot \cos\varphi}{\gamma \cdot S \cdot V_n} \cdot 100 \le 1.5\%$$
  * Tramo trifásico AC:
    $$\Delta u (\%) = \frac{\sqrt{3} \cdot L \cdot I \cdot \cos\varphi}{\gamma \cdot S \cdot V_n} \cdot 100 \le 1.5\%$$
* **Pérdidas Joule en Conductores (IEC 61724):** Cuantificación de energía disipada anualmente en vatios y kWh mediante la resistencia óhmica corregida por temperatura:
  $$P_{joule} = I_{rms}^2 \cdot R(T) = I_{rms}^2 \cdot \left[\rho_{20} \cdot \frac{L}{S} \cdot (1 + \alpha_{Cu} \cdot (\theta - 20))\right]$$

### 2.6. Acumulación Electroquímica y Modelado de Baterías LiFePO4
* **Tecnología:** Fosfato de hierro y litio (LiFePO4) de alta densidad y estabilidad térmica, libre de cobalto.
* **Dimensionamiento Dinámico por Autarquía:** Estimación de la capacidad útil en función de la fracción de consumo nocturno no cubierta por la generación solar diurna y del objetivo fijado por el usuario (60% a 100% de cobertura):
  $$E_{bat,util} = E_{demanda\_nocturna} \cdot \left[\frac{\text{Autarquía}_{\text{objetivo}} - \text{Autarquía}_{\text{solar}}}{1 - \text{Autarquía}_{\text{solar}}}\right]$$
* **Profundidad de Descarga (DoD) y Eficiencia:** Modelado con DoD del 90% y eficiencia de ida y vuelta (Round-Trip Efficiency) del 95% para baterías conectadas a bus DC y 90% para sistemas con acoplamiento AC.

### 2.7. Análisis Económico y Flujo de Caja Descontado (25 Años)
* **Parámetros Económicos:**
  * Vida útil de la instalación: 25 años.
  * Tasa de descuento nominal ($r$): 3.0% anual.
  * Tasa de inflación energética esperada: 2.5% anual.
  * Degradación del generador fotovoltaico: 0.5% anual.
  * Sustitución programada de inversores: año 13 de explotación.
* **Métricas Financieras Consolidadas:** Valor Actual Neto ($VAN$), Tasa Interna de Retorno ($TIR$), Periodo de Recuperación Simple y Descontado ($Payback$) y Coste Nivelado de la Energía ($LCOE$ en €/kWh).

### 2.8. Estudio Volumétrico 3D, Raytracing de Sombras PVGIS y Cableado Profundo (`Solar3DStudio`)
Integrado exclusivamente en el Modo Profesional, el estudio tridimensional ejecuta simulación física sobre la geometría real del emplazamiento:
* **Referencia Georreferenciada PNOA (IGN):** Descarga dinámica de ortofotografía aérea de máxima resolución espacial desde el servicio WMS del **Instituto Geográfico Nacional** (`https://www.ign.es/wms-inspire/pnoa-ma`) o ingestión de planos técnicos acotados (`.png`, `.jpg`, `.pdf`) mediante `FileReader` con calibración de escala métrica.
* **Modelado Paramétrico de Edificación:** Generación analítica de tipologías arquitectónicas (cubiertas a dos aguas, cuatro aguas, un agua, planta en L, cubiertas planas con peto perimetral y casetón de ascensor, o naves industriales) y calcado vectorial de vértices libres.
* **Catálogo de Obstáculos Físicos y Arbolado Estacional:** Incorporación de elementos sombreadores con propiedades ópticas estacionales: árboles de hoja caduca (con coeficiente de atenuación radiativa invernal $\tau = 0.68$ y estival $\tau = 0.18$), coníferas perennes ($\tau = 0.14$), chimeneas, antenas, climatizadores (HVAC) y prismas colindantes.
* **Algoritmo de Trazado de Rayos con Discretización Half-Cut (6 Subzonas):**
  * Cálculo astronómico continuo del vector de posición solar (Ángulo Cenital $\theta_z$ y Acimut $\gamma_s$) según el algoritmo NOAA para cada hora diurna de los 12 meses representativos.
  * Incorporación del perfil de elevación de horizonte topográfico lejano devuelto por PVGIS JRC (`mode=printhorizon`).
  * Discretización de cada panel fotovoltaico en 6 subzonas de captación (3 subcadenas asociadas a los diodos de paso *bypass* en configuración partida *Half-Cut*). Activación no lineal de pérdidas por mismatch eléctrico: la oclusión de una subcélula activa el diodo correspondiente, reduciendo la producción del módulo un 33% o 66% en lugar del 100%.
  * Evaluación del Factor de Vista al Cielo (*Sky View Factor*, $SVF$) para cuantificar la pérdida por enmascaramiento de radiación difusa y albedo.
* **Cálculo Analítico de Cableado 3D y Conectores MC4:**
  * Posicionamiento espacial de equipos: Inversor, Acumulador LiFePO4 y Cuadro General de Protección (CGMP).
  * Simulación de canalizaciones y topologías de interconexión: **Salto de Rana** (*Leapfrog*, interconectando módulos alternos para minimizar el lazo de inducción magnética) vs **Cadena Lineal** (*Daisy-Chain* con cable de retorno).
  * Determinación métrica exacta de: conductores entre placas ($L_{intra}$), puentes entre filas ($L_{jumper}$), bajantes homerun ($L_{dc+}, L_{dc-}$), línea de enlace al cuadro general ($L_{ac}$), línea de batería ($L_{bat}$), estimación de bobinas comerciales de compra (+15% de holgura de curvatura y conexionado) y cómputo de pares de conectores rápidos estancos tipo **MC4**.

---

## 3. Catálogos Industriales Tier-1 Integrados

La base de datos incorpora equipos certificados según normativas internacionales (IEC 61215, IEC 61730, IEC 62109, UNE 206007-1):

| Subsistema | Cantidad | Rango de Parámetros | Fabricantes Homologados |
| :--- | :---: | :--- | :--- |
| **Módulos Fotovoltaicos** | 30 | 390 Wp a 715 Wp (Compactos, Full Black, Residenciales, PYME e Industriales Bifaciales G12) | Meyer Burger, SunPower Maxeon, REC Alpha, Hyundai, JA Solar, Jinko Tiger Neo, Trina Vertex S+, LONGi Hi-MO, AIKO Neostar, Canadian Solar, Qcells Q.TRON, Huasun HJT. |
| **Inversores Solares** | 54 | 0,8 kW a 125 kW (Microinversores, Monofásicos Híbridos, Trifásicos Comerciales y Centralizados 3.0TD con hasta 12 MPPTs) | Enphase IQ8, Hoymiles, Huawei SUN2000 (L1, M1, MB0, 100KTL), Fronius (Primo, Symo, Tauro), SMA (Sunny Boy, Tripower), Sungrow (SG, SH-RT, CX-P2), GoodWe, Kostal Plenticore, Deye, Solis, Victron MultiPlus-II, Ingeteam. |
| **Baterías LiFePO4** | 34 | 1,2 kWh a 60 kWh (Baja tensión 48V LV, Alta tensión HV y Acoplamiento AC) | Huawei LUNA2000 (S0 y S1), BYD Battery-Box (HVS, HVM, LVS), Pylontech (US2000C, US3000C, Force H2), Sungrow SBR, Tesla Powerwall 2/3, Enphase IQ Battery 5P, Dyness Tower, Deye SE-G5.1, SolaX Triple Power. |

---

## 4. Modalidades Operativas de la Aplicación

La plataforma ofrece dos flujos de trabajo según las necesidades del usuario:

### 4.1. Modo Rápido (3 Clics — Síntesis Ejecutiva)
Diseñado para la confección ágil de propuestas técnicas por parte de comerciales, promotores y clientes:
```
┌────────────────────────┐      ┌───────────────────────────────┐      ┌───────────────────────────────┐
│  1. Datos del Proyecto │ ───► │ 2. Suministro, Demanda y Bat. │ ───► │ 3. Showroom de Resultados A4  │
│  Identificación formal │      │ Ubicación, Datadis, Autarquía │      │ Dimensionado óptimo y REBT OK │
└────────────────────────┘      └───────────────────────────────┘      └───────────────────────────────┘
```
1. **Identificación (Paso 0):** Registro de titular, referencia de expediente y emplazamiento.
2. **Suministro y Almacenamiento (Paso 1):** Introducción de consumo anual o importación de archivo Datadis, selección de batería LiFePO4 (Sí/No), porcentaje de autarquía deseada (70%, 85%, 95%, 100%) y régimen legal RD 244/2019.
3. **Salto Directo a Resultados (Paso 7):** El sistema calcula automáticamente la potencia óptima de paneles, selecciona el inversor de catálogo adecuado, distribuye los strings en los MPPTs, dimensiona los cables REBT y presenta los 6 KPIs ejecutivos, las gráficas anuales y la memoria técnica A4.

### 4.2. Modo Ingeniería Avanzada (8 Fases Técnicas)
Diseñado para ingenieros proyectistas, instaladores autorizados y directores de obra:
* **Fase 0 (Identificación):** Metadatos completos y exportación/importación en formato JSON estandarizado.
* **Fase 1 (Suministro y PVGIS):** Selección entre 52 demarcaciones territoriales, modelado tarifario (Fija, 2.0TD o 3.0TD de 6 periodos) y telemetría de contador.
* **Fase 2 (Generador Fotovoltaico & Estudio 3D):** Selección de módulo de catálogo o manual, orientación, inclinación, cálculo de superficie ocupada ($m^2$), curva $I-V$ / $P-V$, e integración del **Estudio 3D CAD (`Solar3DStudio`)** con ortofoto IGN PNOA, modelado de cubiertas, posicionamiento de obstáculos/árboles, raytracing de 6 subzonas y mapa de calor de sombras.
* **Fase 3 (Inversor y Multi-MPPT):** Asignación de inversor comercial, solver de distribución de cadenas, cálculo de pérdidas por clipping y botón de autocorrección en 1 clic.
* **Fase 4 (Cableado REBT & Métrica 3D):** Verificación analítica de caída de tensión y criterio térmico para tramos DC, AC y Batería con esquema unifilar interactivo SVG y panel métrico de canalizaciones 3D (uniones placa a placa, puentes, bajantes, bobinas de compra y pares de conectores MC4).
* **Fase 5 (Almacenamiento):** Elección de tecnología de acoplamiento, comparativa de factura con/sin batería y cálculo de cobertura de cargas nocturnas.
* **Fase 6 (Legal y Finanzas):** Simulación de flujos de caja a 25 años, deducciones fiscales según territorio y cálculo de VAN, TIR y LCOE.
* **Fase 7 (Showroom y Memoria A4):** Panel ejecutivo consolidado, auditoría de pérdidas IEC 61724, anexo de simulación 3D con captura en alta resolución del gemelo digital y generación de la Memoria Técnica de Diseño oficial en PDF A4.

---

## 5. Protocolo de Acreditación y Descarga de Telemetría Datadis

Para garantizar la exactitud de los cálculos sin incurrir en sesgos estimativos, la plataforma incluye un módulo de ayuda para la obtención del archivo de medidas del contador:

1. **Naturaleza del Servicio:** **Datadis** (`https://datadis.es`) es la pasarela oficial y gratuita de comunicación de datos de medida de las empresas distribuidoras de electricidad de España (regulada por la CNMC).
2. **Requisitos de Acceso:**
   * Documento Nacional de Identidad o Número de Identificación de Extranjero (DNI / NIE / CIF).
   * Código Unificado de Punto de Suministro (**CUPS**), identificador alfanumérico de 20 o 22 caracteres presente en la cabecera de la factura eléctrica.
   * Acreditación de identidad mediante **Certificado Digital / Cl@ve** (acceso inmediato) o recepción de código OTP vía **SMS** al número de teléfono asociado al contrato de suministro.
3. **Parámetros de Extracción en Datadis:**
   * **Sección:** *Consumos* ➔ *Descarga de datos*.
   * **Periodo:** Últimos 12 meses completos (para abarcar el ciclo estacional completo invierno-verano).
   * **Granularidad:** Medida Horaria (lectura cada hora) o Cuartohoraria.
   * **Formato de Salida:** Archivo de texto plano delimitado por punto y coma (`.csv`).

---

## 6. Especificaciones de Despliegue y Distribución

* **Distribución Monomórfica Autónoma (`showroom_solar_portable.html`):** Archivo HTML5 único con estilos Tailwind CSS, motor de renderizado Chart.js y bibliotecas integradas en línea. No requiere instalación de Node.js, compilación local ni dependencias de servidor.
* **Despliegue en Cloudflare Pages (`subir-a-cloudflare/`):** Preparado para publicación en redes de distribución de contenidos (CDN). Incluye fichero de cabeceras `_headers` con políticas estrictas de seguridad (Content Security Policy, X-Frame-Options DENY) y directivas de control de caché (`Cache-Control: public, max-age=0, must-revalidate`) para garantizar la entrega inmediata de nuevas versiones.
* **Salida Normalizada A4 (`@media print`):** La vista del Paso 7 genera una memoria técnica de ingeniería formateada para impresión vertical A4 según norma UNE-EN ISO 5457, incorporando esquemas vectoriales SVG, gráficas renderizadas en mapa de bits de alta resolución y cuadros tabulares con sellos de cumplimiento normativo REBT.

---

## 7. Garantía de Calidad y Verificación Automatizada (QA)

El código fuente se valida continuamente mediante una suite integral de pruebas funcionales y de regresión visual en Playwright (`test_showroom_wizard_e2e.py`):
* Verificación de cálculo causal (entradas preceden a resultados).
* Cumplimiento estricto de límites térmicos y de tensión en los 54 inversores del catálogo.
* Validación matemática de caídas de tensión REBT para longitudes de hasta 150 metros.
* Detección de sobretensión y autorecuperación mediante el botón `🔧 Autocorregir`.
* Ausencia absoluta de desbordamiento horizontal (`overflow: 0px`) en resoluciones de escritorio (1440px) y móviles (390px) en idioma español e inglés.

---

## 8. Licencia y Uso Profesional

Este software ha sido desarrollado como herramienta de ingeniería fotovoltaica y soporte a la redacción de proyectos técnicos en España y el Espacio Económico Europeo. Su uso es libre para fines formativos, técnicos y profesionales.
