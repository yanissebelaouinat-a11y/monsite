// Relais Cloudflare Worker : reçoit les notifications du site belaconnect.fr
// et les envoie sur Telegram. Le jeton du robot n'est JAMAIS dans ce fichier :
// il est stocké dans les variables secrètes du Worker (TG_TOKEN et TG_CHAT).
//
// Mise en place : Cloudflare > Workers & Pages > Créer > Worker > coller ce code > Déployer,
// puis Paramètres > Variables et secrets : ajouter TG_TOKEN (jeton BotFather) et TG_CHAT (votre Id).

const ALLOWED = ["https://belaconnect.fr", "https://www.belaconnect.fr"];

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const cors = {
      "Access-Control-Allow-Origin": ALLOWED.includes(origin) ? origin : ALLOWED[0],
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };
    if (request.method === "OPTIONS") return new Response(null, { headers: cors });
    if (request.method !== "POST" || !ALLOWED.includes(origin)) {
      return new Response("Interdit", { status: 403, headers: cors });
    }

    let data;
    try { data = await request.json(); } catch (e) { return new Response("JSON invalide", { status: 400, headers: cors }); }
    const clip = (v, n) => String(v || "").slice(0, n);
    const esc = (v) => v.replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));

    // Mise en forme lisible : titres en MAJUSCULES et libellés « xxx : » en gras
    // (le texte libre du client, sous « MESSAGE », reste tel quel jusqu'à la ligne vide suivante)
    const pretty = (t) => {
      let free = false;
      return esc(clip(t, 3500)).split("\n").map((l) => {
        if (!l.trim()) { free = false; return l; }
        if (free) return l;
        if (/^\S+ [A-ZÀÂÉÈÊÎÔÛÇ' ]{4,}$/.test(l)) { free = /MESSAGE/.test(l); return "<b>" + l + "</b>"; }
        const i = l.indexOf(" : ");
        return i > 0 && i < 40 ? "<b>" + l.slice(0, i) + "</b> :" + l.slice(i + 2) : l;
      }).join("\n");
    };

    let text;
    if (data.v === 2 && (data.type === "devis" || data.type === "clic")) {
      text = "<b>" + esc(clip(data.title, 120)) + "</b>\n━━━━━━━━━━━━━━━\n" + pretty(data.text);
    } else if (data.type === "devis") {
      text = "📩 <b>" + esc(clip(data.subject, 200)) + "</b>\n\n" + esc(clip(data.message, 3500));
    } else if (data.type === "clic") {
      const what = data.what === "whatsapp" ? "💬 Clic sur WhatsApp" : "📞 Clic sur Appeler";
      text = what + "\nPage : " + esc(clip(data.page, 200));
    } else {
      return new Response("Type inconnu", { status: 400, headers: cors });
    }

    const r = await fetch("https://api.telegram.org/bot" + env.TG_TOKEN + "/sendMessage", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ chat_id: env.TG_CHAT, text, parse_mode: "HTML", disable_web_page_preview: true }),
    });
    return new Response(r.ok ? "ok" : "erreur Telegram", { status: r.ok ? 200 : 502, headers: cors });
  },
};
