import sys
import json
import time
import threading
from pathlib import Path
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WORKSPACE = Path(r"c:\Users\herna\Desktop\Negocio\Energias")
ARTIFACT_DIR = Path(r"C:\Users\herna\.gemini\antigravity\brain\b1d40ca2-0ca6-4095-b420-9640d25e904a")
SCREENSHOT_DIR = ARTIFACT_DIR / "qa_screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def start_server():
    handler = partial(QuietHandler, directory=str(WORKSPACE))
    httpd = HTTPServer(("127.0.0.1", 0), handler)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd, port


def run_e2e():
    httpd, port = start_server()
    base_url = f"http://127.0.0.1:{port}/index.html"
    print(f"Serving Showroom Solar SPA at {base_url}")

    console_errors = []
    page_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 920})
        page = context.new_page()

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        page.goto(base_url, wait_until="networkidle")
        page.wait_for_timeout(300)

        # 1. PASO 0: Validación de campos y portada Showroom
        assert page.locator("#step-0").is_visible(), "Step 0 should be visible initially"
        assert page.locator("#wizardBottomBar").is_hidden(), "Bottom bar hidden on Hero cover Step 0"

        # Probar validación de nombre vacío
        page.fill("#inpProjName", "")
        page.click("#btnStartNewProject")
        assert page.locator("#errProjName").is_visible(), "Validation error should appear if project name empty"

        # Rellenar datos reales del proyecto
        page.fill("#inpProjName", "Residencial Villa Aurora Solar")
        page.fill("#inpClientName", "Comunidad Propietarios Aurora")
        page.fill("#inpEngineerName", "Ing. Carlos Mendoza (Col. 14920)")
        page.fill("#inpProjRef", "EXP-REBT-2026-089")
        page.screenshot(path=str(SCREENSHOT_DIR / "es_desktop_step0_light.png"), full_page=True)

        page.click("#btnStartNewProject")
        page.wait_for_timeout(350)
        assert page.locator("#step-1").is_visible(), "Should advance to Step 1"
        assert page.locator("#wizardBottomBar").is_visible(), "Bottom bar visible on Step 1"

        # Verificar persistencia en localStorage bajo clave exacta pv_project_state_v1
        raw_state = page.evaluate("() => localStorage.getItem('pv_project_state_v1')")
        assert raw_state is not None, "pv_project_state_v1 must exist in localStorage"
        parsed_state = json.loads(raw_state)
        for key in ["projectMeta", "locationAndPVGIS", "consumptionAndTariff", "pvModules", "inverterAndStrings", "cablingAndREBT", "batterySystem", "legalAndFinancials"]:
            assert key in parsed_state, f"Missing key {key} in pv_project_state_v1"
        print("✓ Step 0 & Store (pv_project_state_v1) verified")

        # 2. PASO 1: Consumo, Tarifas y PVGIS
        page.select_option("#selQuickProvince", "Las Palmas")
        page.wait_for_timeout(200)
        assert "IGIC" in page.inner_text("#s1FiscalPill"), "Canarias should auto-set IGIC"

        page.select_option("#selQuickProvince", "Sevilla")
        page.fill("#inpAnnualKwh", "5800")
        page.dispatch_event("#inpAnnualKwh", "input")
        page.wait_for_timeout(150)

        # Probar Segmented Control Tarifa Fija vs 2.0TD
        page.click("#tabTariffFixed")
        assert page.locator("#panelTariffFixed").is_visible()
        assert page.locator("#panelTariff20TD").is_hidden()
        page.click("#tabTariff20TD")
        assert page.locator("#panelTariff20TD").is_visible()

        rec_kwp = float(page.inner_text("#s1KpiRecKwp").replace(",", "."))
        assert rec_kwp > 1.5, f"Expected rec_kwp > 1.5, got {rec_kwp}"
        page.screenshot(path=str(SCREENSHOT_DIR / "es_desktop_step1_light.png"), full_page=True)
        print(f"✓ Step 1 verified (Sevilla 5800 kWh -> Rec {rec_kwp} kWp)")

        # Avanzar a Paso 2
        page.click("#btnWizardNext")
        page.wait_for_timeout(350)
        assert page.locator("#step-2").is_visible()

        # 3. PASO 2: Generador Fotovoltaico (Modo A Catálogo vs Modo B Manual + Geometría)
        assert page.evaluate("() => document.getElementById('inpModPmp').readOnly") is True, "Catalog mode should be readOnly"
        page.click("#tabModCustom")
        assert page.evaluate("() => document.getElementById('inpModPmp').readOnly") is False, "Custom mode must unlock inputs"
        page.fill("#inpModPmp", "520")
        page.dispatch_event("#inpModPmp", "input")
        page.fill("#inpModCount", "10")
        page.dispatch_event("#inpModCount", "input")
        page.wait_for_timeout(150)
        kwp_s2 = page.inner_text("#s2KpiTotalKwp")
        assert kwp_s2 in ("5,20", "5.20"), f"10 x 520Wp should equal 5,20 kWp, got {kwp_s2}"

        # Probar inclinación y azimuth
        page.fill("#inpAzimuth", "45")
        page.dispatch_event("#inpAzimuth", "input")
        assert "Suroeste" in page.inner_text("#s2OrientationText")
        page.click("button:has-text('Óptimo PVGIS')")
        page.screenshot(path=str(SCREENSHOT_DIR / "es_desktop_step2_light.png"), full_page=True)
        print(f"✓ Step 2 verified (Custom 10×520Wp = {kwp_s2} kWp)")

        # Avanzar a Paso 3
        page.click("#btnWizardNext")
        page.wait_for_timeout(350)
        assert page.locator("#step-3").is_visible()

        # 4. PASO 3: Inversor y Arquitectura Multi-MPPT
        page.select_option("#selInverterCatalog", "huawei_sun2000_5ktl")
        page.wait_for_timeout(150)
        # Provocar sobretensión deliberada en MPPT 1 (18 paneles en serie -> >600V en frío)
        mppt1_ns = page.locator("#mpptCardsContainer input[type='number']").nth(1)
        mppt1_ns.fill("18")
        mppt1_ns.dispatch_event("input")
        page.wait_for_timeout(150)
        assert "SOBRETENSIÓN" in page.inner_text("#s3BadgeVoc"), "18 modules in series should trigger cold overvoltage on 600V inverter"
        assert "INCOMPATIBILIDAD" in page.inner_text("#s3GlobalCompatBadge")

        # Auto-repartir paneles en MPPTs y verificar recuperación total
        page.click("button:has-text('Auto-repartir paneles en MPPTs')")
        page.wait_for_timeout(150)
        assert "CUMPLE" in page.inner_text("#s3BadgeVoc")
        assert "COMPATIBLE" in page.inner_text("#s3GlobalCompatBadge")
        page.screenshot(path=str(SCREENSHOT_DIR / "es_desktop_step3_light.png"), full_page=True)
        print("✓ Step 3 Multi-MPPT overvoltage detection & auto-recovery verified")

        # Avanzar a Paso 4
        page.click("#btnWizardNext")
        page.wait_for_timeout(350)
        assert page.locator("#step-4").is_visible()

        # 5. PASO 4: Cableado y Normativa REBT ITC-BT-19 / 20 / 40
        # Forzar fallo por caída de tensión en Tramo DC: L=90m, S=1.5mm²
        page.fill("#inpCableLen", "90")
        page.dispatch_event("#inpCableLen", "input")
        page.select_option("#selCableSection", "1.5")
        page.wait_for_timeout(150)
        verdict_fail = page.inner_text("#s4VerdictTitle")
        assert "NO CUMPLE REBT" in verdict_fail, f"Expected NO CUMPLE REBT, got {verdict_fail}"

        # Pulsar Auto-seleccionar y comprobar cumplimiento REBT
        page.click("button:has-text('Auto-seleccionar')")
        page.wait_for_timeout(150)
        verdict_ok = page.inner_text("#s4VerdictTitle")
        assert "CUMPLE REBT" in verdict_ok, f"Expected CUMPLE REBT after auto-select, got {verdict_ok}"
        selected_sec = float(page.input_value("#selCableSection"))
        assert selected_sec >= 6, f"Expected section >= 6mm² for 90m DC run, got {selected_sec}"

        # Verificar pestaña Tramo AC y esquema unifilar SVG
        page.click("#tabCable_ac")
        page.wait_for_timeout(100)
        assert page.locator("#s4UnifilarContainer svg").is_visible()
        page.screenshot(path=str(SCREENSHOT_DIR / "es_desktop_step4_light.png"), full_page=True)
        print(f"✓ Step 4 REBT ITC-BT-19/20/40 verified (90m DC auto-sized to {selected_sec} mm²)")

        # Avanzar a Paso 5
        page.click("#btnWizardNext")
        page.wait_for_timeout(350)
        assert page.locator("#step-5").is_visible()

        # 6. PASO 5: Sistema de Baterías (Toggle OFF -> ON)
        assert page.locator("#boxBatteryOff").is_visible()
        assert page.locator("#boxBatteryOn").is_hidden()
        page.click("#btnBatteryToggle")
        page.wait_for_timeout(250)
        assert page.locator("#boxBatteryOn").is_visible()
        aut_without = int(page.inner_text("#s5KpiAutarkyWithout"))
        aut_with = int(page.inner_text("#s5KpiAutarkyWith"))
        assert aut_with > aut_without, f"Battery should boost autarky ({aut_without}% -> {aut_with}%)"
        page.screenshot(path=str(SCREENSHOT_DIR / "es_desktop_step5_light.png"), full_page=True)
        print(f"✓ Step 5 Battery verified (Autarky {aut_without}% -> {aut_with}%)")

        # Avanzar a Paso 6
        page.click("#btnWizardNext")
        page.wait_for_timeout(350)
        assert page.locator("#step-6").is_visible()

        # 7. PASO 6: Marco Legal RD 244/2019 y Viabilidad Financiera
        payback_txt = page.inner_text("#s6KpiPayback")
        van_txt = page.inner_text("#s6KpiVan")
        assert len(payback_txt) > 0 and len(van_txt) > 0
        page.screenshot(path=str(SCREENSHOT_DIR / "es_desktop_step6_light.png"), full_page=True)
        print(f"✓ Step 6 Legal & Financials verified (Payback {payback_txt} yrs, VAN {van_txt} €)")

        # Avanzar a Paso 7
        page.click("#btnWizardNext")
        page.wait_for_timeout(450)
        assert page.locator("#step-7").is_visible()

        # 8. PASO 7: Showroom de Resultados + Informe A4 @media print
        assert "CUMPLE REBT" in page.inner_text("#s7KpiRebtStatus")
        page.screenshot(path=str(SCREENSHOT_DIR / "es_desktop_step7_light.png"), full_page=True)

        # Verificar generación de #printReportA4 y reglas CSS @media print
        page.evaluate("() => PrintReport.prepareDOMReport()")
        page.wait_for_timeout(200)
        report_html = page.inner_html("#printReportA4")
        assert "MEMORIA TÉCNICA DE DISEÑO FOTOVOLTAICO" in report_html
        assert "data:image/png;base64," in report_html, "Embedded high-res chart PNGs must be present in A4 report"

        page.emulate_media(media="print")
        app_display_in_print = page.evaluate("() => getComputedStyle(document.getElementById('appShell')).display")
        rep_display_in_print = page.evaluate("() => getComputedStyle(document.getElementById('printReportA4')).display")
        assert app_display_in_print == "none", f"#appShell must be hidden in print, got {app_display_in_print}"
        assert rep_display_in_print == "block", f"#printReportA4 must be visible in print, got {rep_display_in_print}"

        pdf_path = SCREENSHOT_DIR / "informe_tecnico_showroom_a4.pdf"
        page.pdf(path=str(pdf_path), format="A4", print_background=True)
        assert pdf_path.exists() and pdf_path.stat().st_size > 15000
        page.emulate_media(media="screen")
        print(f"✓ Step 7 & A4 PDF Print Report verified ({pdf_path.stat().st_size:,} bytes)")

        # 9. Probar Modo Oscuro + Inglés (EN) + Navegación por Stepper Superior + Overflow 0px
        page.click("#btnThemeToggle")
        page.click("#btnLangEn")
        page.wait_for_timeout(250)
        assert page.evaluate("() => document.documentElement.classList.contains('dark')") is True
        assert page.evaluate("() => document.documentElement.lang") == "en"
        page.screenshot(path=str(SCREENSHOT_DIR / "en_desktop_step7_dark.png"), full_page=True)

        # Clic en Paso 3 desde la barra superior
        page.locator("#wizardStepperList button").nth(3).click()
        page.wait_for_timeout(300)
        assert page.locator("#step-3").is_visible()
        page.screenshot(path=str(SCREENSHOT_DIR / "en_desktop_step3_dark.png"), full_page=True)

        # Verificar 0px desbordamiento horizontal en Desktop (1440px) y Móvil (390px) en ambos idiomas
        for vw, label in [(1440, "desktop"), (390, "mobile")]:
            page.set_viewport_size({"width": vw, "height": 844})
            for lang_btn, lang_code in [("#btnLangEs", "es"), ("#btnLangEn", "en")]:
                page.click(lang_btn)
                for step_idx in [0, 1, 3, 4, 7]:
                    page.evaluate(f"() => Wizard.goToStep({step_idx}, true)")
                    page.wait_for_timeout(150)
                    overflow = page.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
                    assert overflow <= 1, f"Horizontal overflow ({overflow}px) on {label} {lang_code} step {step_idx}"
                    if vw == 390 and step_idx in (0, 1, 4, 7):
                        page.screenshot(path=str(SCREENSHOT_DIR / f"{lang_code}_mobile_step{step_idx}_dark.png"), full_page=True)

        print("✓ Responsive geometry audit passed (0px horizontal overflow across Desktop 1440px & Mobile 390px, ES & EN)")

        assert len(console_errors) == 0, f"Console errors detected: {console_errors}"
        assert len(page_errors) == 0, f"Page errors detected: {page_errors}"
        print("✓ Zero console.error & zero uncaught exceptions!")

        browser.close()
    httpd.shutdown()
    print("\nALL E2E & VISUAL QA CHECKS PASSED 100%!")


if __name__ == "__main__":
    run_e2e()
