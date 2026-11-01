# WORKFLOW MAP — Showroom Solar SPA (v4.3.0)

## 1. Estructura del Proyecto
```
Energias/
├── WORKFLOW_MAP.md                        # Mapa de contexto y arquitectura universal (v4.3.0)
├── README.md                              # Documentación completa del repositorio GitHub
├── .gitignore                             # Filtro de exclusión de artefactos y archivos temporales
├── index.html                             # SPA Principal "Showroom Solar" (Wizard 8 Pasos + Informe A4 @media print)
├── showroom_solar_portable.html           # Entregable portable autocontenido 1-archivo sincronizado
├── ingenieria.html                        # Estación técnica auxiliar preservada (retrocompatible vía localStorage)
├── test_showroom_wizard_e2e.py            # Suite E2E Playwright (8 Pasos, Multi-MPPT, REBT, Baterías, PDF A4, 0-Overflow)
├── subir-a-cloudflare/                    # Entregable listo para producción en Cloudflare Pages
│   ├── index.html                         # SPA Showroom Solar sincronizada byte a byte
│   ├── ingenieria.html                    # Estación técnica auxiliar preservada
│   ├── _headers                           # Cabeceras de seguridad CSP, X-Frame-Options, Permissions-Policy
│   └── functions/api/pvgis.js             # Cloudflare Pages Function Proxy para JRC PVGIS v5.2 (lat, lon, angle, aspect, loss)
└── ai_studio_code(1).html                 # Prototipo histórico preservado
```

## 2. Grafo de Conexiones & Arquitectura Reactiva (`pv_project_state_v1`)
```
                  STORE CENTRALIZADO REACTIVO (localStorage: pv_project_state_v1)
   ┌───────────────┬───────────────────┬─────────────┬───────────────────┬────────────────┐
   ▼               ▼                   ▼             ▼                   ▼                ▼
[Paso 0]        [Paso 1]            [Paso 2]      [Paso 3]            [Paso 4]         [Paso 5-6]
Portada       Consumo/Tarifas     Generador FV   Inversor/MPPTs     Cableado REBT     Baterías/Legal
Metadatos     + PVGIS Satélite    Catálogo/Libre  N_p × N_s         ITC-BT-19/20/40   LiFePO4 + RD244
JSON I/O      Fija vs 2.0TD 3P    Tilt/Azimuth    Voc(-10°C)<Vmax   Ib≤Iz, Δu%, I²R   IVA 21%/IGIC 0%
   │               │                   │             │                   │                │
   └───────────────┴───────────────────┴─────────────┴─────────┬─────────┴────────────────┘
                                                               ▼
                                      PhysicsEngine.recalculateAll() -> Store.computed
                                                               │
                                    ┌──────────────────────────┴──────────────────────────┐
                                    ▼                                                     ▼
                        [Paso 7: Showroom Resultados]                        [#printReportA4 (@media print)]
                     6 KPIs Gigantes + 2 Gráficas Chart.js                Memoria Técnica A4 Vertical + PNGs
                     Tablas Consolidadas FV / MPPT / REBT                 Esquema Unifilar SVG + Cajetín CIE
```

## 3. Estado del Proyecto
- **Versión:** `4.3.0` — Motor físico y electrotécnico estricto (cero estimaciones arbitrarias; cálculo por ecuaciones analíticas o extracción directa de ficha técnica del fabricante), tipografía High-End y reporte de pérdidas con trazabilidad de origen (CALCULADO vs TABLA FICHA vs MANT. 60€/A).
- **Funcionalidades Activas y Verificadas:**
  1. **Motor de Pérdidas y Eficiencias Físicas / Datasheet (IEC 61724):**
     - **Pérdida Térmica de Célula (CALCULADO):** Modelo térmico Evans/PVGIS en función de irradiación $G_{poa}$, $NOCT$ de ficha ($43\text{--}45\text{ °C}$) y coeficiente de temperatura $\gamma_{Pmp}$ ($-0,26\text{ a }-0,35\text{ \%/°C}$).
     - **Pérdida por Mismatch y Tolerancia (TABLA FICHA):** Extraído directamente de la ficha del panel seleccionado ($0,8\%\text{ a }1,2\%$).
     - **Pérdida Óptica Angular IAM (CALCULADO):** Modelo de Fresnel/Martin-Ruiz para vidrio solar ARC ($b_0 = 0,05$) en función de inclinación y azimut ($1,00\%\text{ a }2,20\%$).
     - **Pérdida por Suciedad / Soiling (MANT. 60€/A):** $0,00\%$ estrictamente garantizado mediante contrato de mantenimiento y limpieza periódica (60 €/año).
     - **Eficiencia del Inversor (TABLA FICHA):** Rendimiento nominal ponderado extraído directamente de la base de datos comercial ($\eta = 97,0\%\text{ a }98,7\% \implies 100 - \eta\%$).
     - **Recorte por Potencia / Clipping (CALCULADO):** Simulación horaria integrada cuando el ratio $P_{dc}/P_{ac} > 1,15$.
     - **Pérdidas Joule en Cableado DC y AC (CALCULADO):** Ley de Ohm/Joule rigurosa ($P_{loss} = I^2 \cdot R$) según longitud real ($L$), sección normalizada ($S$) y resistividad del cobre a $70\text{ °C}$ ($\rho = 0,021\ \Omega\cdot\text{mm}^2/\text{m}$).
     - **Rendimiento Round-Trip Batería (TABLA FICHA):** Rendimiento de ida y vuelta electroquímico extraído de la ficha ($90,0\%\text{ a }95,5\%$), aplicado únicamente sobre los kWh ciclados anuales ($0,0\%$ si no hay acumulador).
  2. **Tipografía High-End & Estética Showroom:** Encabezados y KPIs en `Outfit` con tracking óptico, cuerpo en `Plus Jakarta Sans`, métricas numéricas tabulares en `JetBrains Mono` (`tabular-nums`), bordes hairline y paleta de acentos minimalista.
  3. **Catálogo Comercial Expandido & Clasificado por Optgroups:**
     - **Paneles Solares (13 modelos):** LONGi, AIKO, Jinko Solar, JA Solar, Trina Solar, Canadian Solar y Hyundai (410 Wp a 690 Wp), con parámetros $NOCT$, $mismatchPct$ y tolerancias de fábrica.
     - **Inversores DC/AC (20 modelos):** Monofásicos (2–6 kW), Trifásicos residenciales/terciarios (4–20 kW) e Industriales (33–100 kW) con rendimiento exacto de ficha.
     - **Baterías LiFePO4 (10 modelos):** Huawei LUNA2000, BYD HVS/HVM, SolaX, Sungrow, Pylontech y Tesla Powerwall 2 con rendimientos Round-Trip de fabricante.
  4. **Store Único Reactivo (`pv_project_state_v1`):** Sincronización automática en `localStorage`, importación/exportación `.JSON` y retrocompatibilidad con `ingenieria.html`.
  5. **Motor PVGIS + Demanda 24h (Pasos 1 y 2):** Geocoding Open-Meteo, GPS, matriz de 52 provincias españolas, curvas horarias, tarifas Fija vs. 2.0TD (P1/P2/P3) y geometría Tilt/Azimuth.
  6. **Ingeniería Multi-MPPT y REBT ITC-BT-19/20/40 (Pasos 3 y 4):** Configuración de 1 a 6 MPPTs, comprobación térmica a $-10\text{ °C}$ y $+70\text{ °C}$, dimensionamiento de conductores Cu/Al, métodos A1..F UNE-HD 60364-5-52 y esquema unifilar SVG interactivo.
  7. **Viabilidad Económica a 25 Años e Informe PDF A4:** Fiscalidad Península (IVA 21%) vs. Canarias (IGIC 0%), VAN, TIR, LCOE, Cashflow 25 años y generación de memoria técnica imprimible en PDF A4 vertical.
