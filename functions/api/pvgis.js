// Cloudflare Pages Function: Proxy para PVGIS (Comisión Europea - JRC)
// Soporta PVcalc (producción mensual), printhorizon (horizonte orográfico 3D) y MRcalc (radiación directa/difusa)

export async function onRequest(context) {
    const url = new URL(context.request.url);
    const lat = url.searchParams.get("lat");
    const lon = url.searchParams.get("lon");
    const angle = url.searchParams.get("angle");
    const aspect = url.searchParams.get("aspect");
    const loss = url.searchParams.get("loss") || "14";
    const mode = url.searchParams.get("mode") || "pvcalc";

    if (!lat || !lon) {
        return new Response(JSON.stringify({ error: "Faltan parámetros lat y lon" }), {
            status: 400,
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        });
    }

    let pvgisUrl = "";
    if (mode === "printhorizon") {
        pvgisUrl = `https://re.jrc.ec.europa.eu/api/v5_2/printhorizon?lat=${encodeURIComponent(lat)}&lon=${encodeURIComponent(lon)}&outputformat=json`;
    } else if (mode === "mrcalc") {
        pvgisUrl = `https://re.jrc.ec.europa.eu/api/v5_2/MRcalc?lat=${encodeURIComponent(lat)}&lon=${encodeURIComponent(lon)}&horirrad=1&d2g=1&outputformat=json`;
    } else {
        const geomParams = (angle !== null && angle !== "")
            ? `&angle=${encodeURIComponent(angle)}&aspect=${encodeURIComponent(aspect || "0")}`
            : `&optimalinclination=1`;
        pvgisUrl = `https://re.jrc.ec.europa.eu/api/v5_2/PVcalc?lat=${encodeURIComponent(lat)}&lon=${encodeURIComponent(lon)}&peakpower=1&loss=${encodeURIComponent(loss)}${geomParams}&outputformat=json`;
    }

    try {
        const response = await fetch(pvgisUrl, {
            headers: {
                "User-Agent": "SolarAI-2.0TD-Proxy/1.1"
            }
        });

        if (!response.ok) {
            return new Response(JSON.stringify({ error: `PVGIS error HTTP ${response.status}` }), {
                status: response.status,
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            });
        }

        const data = await response.text();
        return new Response(data, {
            status: 200,
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Cache-Control": "public, max-age=86400"
            }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), {
            status: 500,
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        });
    }
}
