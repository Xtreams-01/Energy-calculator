// Cloudflare Pages Function: Proxy para PVGIS (Comisión Europea - JRC)
// Resuelve la falta de cabeceras CORS del servidor oficial de la UE

export async function onRequest(context) {
    const url = new URL(context.request.url);
    const lat = url.searchParams.get("lat");
    const lon = url.searchParams.get("lon");
    const angle = url.searchParams.get("angle");
    const aspect = url.searchParams.get("aspect");
    const loss = url.searchParams.get("loss") || "14";

    if (!lat || !lon) {
        return new Response(JSON.stringify({ error: "Faltan parámetros lat y lon" }), {
            status: 400,
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        });
    }

    const geomParams = (angle !== null && angle !== "")
        ? `&angle=${encodeURIComponent(angle)}&aspect=${encodeURIComponent(aspect || "0")}`
        : `&optimalinclination=1`;

    const pvgisUrl = `https://re.jrc.ec.europa.eu/api/v5_2/PVcalc?lat=${encodeURIComponent(lat)}&lon=${encodeURIComponent(lon)}&peakpower=1&loss=${encodeURIComponent(loss)}${geomParams}&outputformat=json`;

    try {
        const response = await fetch(pvgisUrl, {
            headers: {
                "User-Agent": "SolarAI-2.0TD-Proxy/1.0"
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
                "Cache-Control": "public, max-age=86400" // Cache 24h para no saturar al JRC
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
