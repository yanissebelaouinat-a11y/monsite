#!/usr/bin/env python3
"""Génère les pages HTML du site BelaConnect.

Les coordonnées, l'en-tête et le pied de page sont définis une seule fois ici.
Après modification : python3 _src/build.py (depuis la racine du dépôt).
Le dossier _src n'est pas publié (Jekyll ignore les dossiers commençant par « _ »).
"""
import json
import math
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- Coordonnées (À COMPLÉTER) ------------------------------------------------
PHONE_DISPLAY = "06 00 00 00 00"      # TODO : vrai numéro
PHONE_LINK = "+33600000000"           # TODO : même numéro au format international
EMAIL = "contact@belaconnect.fr"      # TODO : adresse à créer chez Hostinger
OWNER_NAME = "[Prénom Nom]"           # TODO : nom de l'entrepreneur
OWNER_ADDRESS = "[Adresse professionnelle], Alpes-Maritimes"  # TODO
SIREN = "947 672 481"
EMAIL_CONFIRMED = False              # passer à True quand l'adresse existe
SITE_URL = "https://belaconnect.fr"

# --- Icônes --------------------------------------------------------------------
ICONS = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></symbol>
    <symbol id="i-cam" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h11l4 4-4 4H3z"/><circle cx="9" cy="11" r="2"/><path d="M18 11h3"/><path d="M8 15v4h4"/></symbol>
    <symbol id="i-dome" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 5h18"/><path d="M5 5v3a7 7 0 0 0 14 0V5"/><circle cx="12" cy="9" r="2.5"/></symbol>
    <symbol id="i-alarm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6v6c0 5 3.4 8.3 8 9 4.6-.7 8-4 8-9V6z"/><path d="M12 8v5"/><circle cx="12" cy="16" r=".6" fill="currentColor"/></symbol>
    <symbol id="i-wifi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 9a15 15 0 0 1 20 0"/><path d="M5 12.5a10 10 0 0 1 14 0"/><path d="M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1" fill="currentColor"/></symbol>
    <symbol id="i-nowire" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5a10 10 0 0 1 14 0"/><path d="M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1" fill="currentColor"/><path d="M12 3v4"/></symbol>
    <symbol id="i-cable" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3v5M17 3v5"/><rect x="5" y="8" width="14" height="5" rx="1"/><path d="M12 13v3a4 4 0 0 1-4 4H6"/></symbol>
    <symbol id="i-pc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></symbol>
    <symbol id="i-server" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="7" rx="1.5"/><rect x="3" y="14" width="18" height="7" rx="1.5"/><path d="M7 6.5h.01M7 17.5h.01"/></symbol>
    <symbol id="i-network" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2" width="6" height="5" rx="1"/><rect x="2" y="17" width="6" height="5" rx="1"/><rect x="16" y="17" width="6" height="5" rx="1"/><path d="M12 7v5M5 17v-3h14v3"/></symbol>
    <symbol id="i-backup" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v6c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 11v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/></symbol>
    <symbol id="i-lock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></symbol>
    <symbol id="i-tool" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4 4 0 0 0 5 5L21 13l-8 8-3-3 6.3-6.3"/><path d="M14.7 6.3 13 4.6 3 14.6 6.4 18"/></symbol>
    <symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.7A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></symbol>
    <symbol id="i-mobile" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/></symbol>
    <symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></symbol>
    <symbol id="i-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></symbol>
    <symbol id="i-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.8 7L3 21l2-6.2A8 8 0 1 1 21 12z"/></symbol>
    <symbol id="i-shop" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9 5 4h14l2 5"/><path d="M4 9v11h16V9"/><path d="M3 9h18"/><path d="M9 20v-6h6v6"/></symbol>
    <symbol id="i-food" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 3v7a3 3 0 0 0 6 0V3M7 3v18"/><path d="M17 3c-2 0-3 2.5-3 6s1 4 3 4v8"/></symbol>
    <symbol id="i-office" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="1"/><path d="M9 6h.01M15 6h.01M9 10h.01M15 10h.01M9 14h.01M15 14h.01M10 22v-4h4v4"/></symbol>
    <symbol id="i-box" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/></symbol>
    <symbol id="i-crane" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 21V4h1l13 3"/><path d="M6 7h14"/><path d="M18 7v5"/><rect x="16" y="12" width="4" height="3"/><path d="M3 21h8"/></symbol>
    <symbol id="i-building" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"/><path d="M5 21V8l7-5 7 5v13"/><path d="M9 21v-5h6v5M9 11h.01M15 11h.01"/></symbol>
    <symbol id="i-team" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2 21a7 7 0 0 1 14 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M22 21a7 7 0 0 0-4-6.3"/></symbol>
    <symbol id="i-medal" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="15" r="6"/><path d="M8.5 10 5 2h4l3 6 3-6h4l-3.5 8"/><path d="m12 12 1 2h2l-1.5 1.3.5 2.2-2-1.2-2 1.2.5-2.2L9 14h2z"/></symbol>
    <symbol id="i-eye" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></symbol>
    <symbol id="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z"/></symbol>
    <symbol id="i-bell" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/></symbol>
    <symbol id="i-door" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 4h5v16h-5"/><path d="M4 20V4l9-1v18z"/><path d="M10 12h.01"/></symbol>
    <symbol id="i-radar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12 19 5"/><path d="M19.4 14A8 8 0 1 1 12 4"/><path d="M15.5 12.5A3.5 3.5 0 1 1 12 8.5"/></symbol>
    <symbol id="i-siren" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 18v-6a5 5 0 0 1 10 0v6"/><path d="M5 18h14v3H5z"/><path d="M12 2v2M4.2 5.2l1.4 1.4M19.8 5.2l-1.4 1.4"/></symbol>
    <symbol id="i-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></symbol>
    <symbol id="i-hdd" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="13" width="20" height="8" rx="2"/><path d="M5 13 7 4h10l2 9"/><path d="M6 17h.01M10 17h.01"/></symbol>
    <symbol id="i-info" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></symbol>
    <symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></symbol>
    <symbol id="i-euro" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 7a7 7 0 1 0 0 10"/><path d="M4 10h9M4 14h9"/></symbol>
  </defs>
</svg>"""

LOGO_SVG = '<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="18" fill="#2BC0DC"/><path d="M15 13h11a8.5 8.5 0 0 1 0 17H15zM15 30h13a9.5 9.5 0 0 1 0 19H15z" fill="none" stroke="#0E1A2E" stroke-width="5.5" stroke-linejoin="round"/><path d="M41.09 24.46A9 9 0 0 1 41.09 35.54" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="1"/><path d="M45.82 20.77A15 15 0 0 1 45.82 39.23" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="0.75"/><path d="M50.55 17.07A21 21 0 0 1 50.55 42.93" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="0.5"/></svg>'

NAV = [
    ("index.html", "Accueil"),
    ("videosurveillance.html", "Vidéosurveillance"),
    ("alarme.html", "Alarme"),
    ("informatique.html", "Informatique & réseau"),
]


CURRENT = ' aria-current="page"'
# Couleur de survol propre à chaque service
NAV_CLASS = {"videosurveillance.html": ' class="svc-video"', "alarme.html": ' class="svc-alarm"', "informatique.html": ' class="svc-it"'}

# Logos des marques : déposer le fichier dans assets/marques/<nom>.png pour remplacer le texte
BRAND_FILES = {"Dahua": "dahua", "Hikvision": "hikvision", "Ajax": "ajax", "TP-Link": "tplink"}
BRAND_LOGO = {"Dahua": ("Dahua", 30), "Hikvision": ("Hikvision", 20), "Ajax": ("Ajax", 24),
              "TP-Link": ("VIGI by TP-Link", 40)}


def brands(names, label="Matériel installé"):
    items = []
    for n in names:
        f = ROOT / "assets" / "marques" / (BRAND_FILES[n] + ".png")
        if f.exists():
            alt, hgt = BRAND_LOGO[n]
            items.append(f'<img src="assets/marques/{f.name}" alt="{alt}" style="height:{hgt}px" loading="lazy">')
        else:
            items.append(f"<strong>{n.upper()}</strong>")
    return f'''
  <div class="brands" aria-label="{label}"><div class="wrap">{"".join(items)}</div></div>'''


def ic(name):
    return f'<svg aria-hidden="true"><use href="#i-{name}"/></svg>'


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{ic('check')} {t}</li>" for t in items) + "</ul>"


def faq(items):
    return '<div class="faq">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def faq_jsonld(items):
    import json, re
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in items]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def cta_band(title="Un projet de sécurité pour vos locaux ?",
             text="Nous venons sur place, étudions vos besoins et vous remettons un devis gratuit, sans engagement."):
    return f"""
  <section class="tight">
    <div class="wrap">
      <div class="cta-band">
        <div>
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <div class="actions">
          <a href="contact.html" class="btn btn-primary">Demander un devis gratuit {ic('arrow')}</a>
          <a href="tel:{PHONE_LINK}" class="btn btn-ghost">{ic('phone')} {PHONE_DISPLAY}</a>
        </div>
      </div>
    </div>
  </section>"""


def page_hero(crumb, title, lead, badge=None):
    b = ""
    return f"""
  <section class="hero small">
    <div class="wrap hero-inner">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> / {crumb}</nav>
      {b}
      <h1>{title}</h1>
      <p class="lead">{lead}</p>
      <div class="hero-cta">
        <a href="contact.html" class="btn btn-primary">Demander un devis gratuit {ic('arrow')}</a>
        <a href="tel:{PHONE_LINK}" class="btn btn-ghost">{ic('phone')} Appeler</a>
      </div>
    </div>
  </section>"""


BREADCRUMB = {
    "videosurveillance.html": "Vidéosurveillance",
    "alarme.html": "Alarme",
    "informatique.html": "Informatique et réseau",
    "contact.html": "Contact",
}


def _arc(cx, cy, r, a0, a1):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    return f"M{x0:.1f} {y0:.1f}A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}"


# Ondes Wi-Fi animées en fond du haut de page (motif du logo)
WAVES = ('<svg class="hero-waves" viewBox="0 0 420 600" aria-hidden="true">'
         + "".join(f'<path class="w{i}" d="{_arc(0, 300, r, -50, 50)}"/>'
                   for i, r in enumerate((110, 200, 290, 380), 1))
         + "</svg>")


def placeholder(value):
    return value.startswith("[") or "00 00 00" in value or value == "+33600000000"


def business_schema():
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": SITE_URL + "/#entreprise",
        "name": "BelaConnect",
        "description": "Installation de vidéosurveillance, d'alarmes et d'informatique pour les professionnels des Alpes-Maritimes.",
        "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/apple-touch-icon.png",
        "image": SITE_URL + "/assets/og-image.png",
        "address": {"@type": "PostalAddress", "addressRegion": "Alpes-Maritimes", "addressCountry": "FR"},
        "areaServed": {"@type": "AdministrativeArea", "name": "Alpes-Maritimes (06)"},
        "knowsAbout": ["Vidéosurveillance", "Alarme anti-intrusion", "Réseau informatique", "Remise au propre de baies de brassage", "Wi-Fi professionnel"],
        "brand": [{"@type": "Brand", "name": b} for b in ("Dahua", "Hikvision", "Ajax", "TP-Link")],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": SITE_URL + "/" + u}}
            for n, u in (("Installation de vidéosurveillance", "videosurveillance.html"),
                         ("Installation d'alarme", "alarme.html"),
                         ("Informatique et réseau d'entreprise", "informatique.html"))]},
    }
    if not placeholder(PHONE_LINK):
        data["telephone"] = PHONE_LINK
    if EMAIL != "contact@belaconnect.fr" or EMAIL_CONFIRMED:
        data["email"] = EMAIL
    if not placeholder(SIREN):
        data["identifier"] = {"@type": "PropertyValue", "propertyID": "SIREN", "value": SIREN.replace(" ", "")}
    return data


def layout(filename, title, description, body, extra_head=""):
    links = "\n      ".join(
        f'<a href="{href}"{NAV_CLASS.get(href, "")}{CURRENT if href == filename else ""}>{label}</a>'
        for href, label in NAV)
    contact_current = CURRENT if filename == "contact.html" else ""
    canonical = SITE_URL + "/" + ("" if filename == "index.html" else filename)
    org = json.dumps(business_schema(), ensure_ascii=False)
    crumbs = ""
    if filename in BREADCRUMB:
        crumbs = '\n<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": BREADCRUMB[filename], "item": canonical}]},
            ensure_ascii=False) + "</script>"
    og_title = title.split(" | ")[0]
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="FR-06">
<meta name="geo.placename" content="Alpes-Maritimes">
<meta property="og:site_name" content="BelaConnect">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{SITE_URL}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="BelaConnect, vidéosurveillance et alarme pour les professionnels des Alpes-Maritimes">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0E1A2E">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/favicon-192.png" sizes="192x192" type="image/png">
<link rel="manifest" href="site.webmanifest">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">{org}</script>{crumbs}{extra_head}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
{ICONS}

<header class="site-header">
  <div class="wrap nav">
    <a href="index.html" class="logo" aria-label="BelaConnect, accueil">{LOGO_SVG}<b>bela<span>connect</span></b></a>
    <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav-links" id="menu" aria-label="Navigation principale">
      {links}
      <a href="tel:{PHONE_LINK}" class="nav-phone">{ic('phone')} {PHONE_DISPLAY}</a>
      <a href="contact.html" class="btn btn-primary"{contact_current}>Devis gratuit</a>
    </nav>
  </div>
</header>

<main id="contenu">
{body}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a href="index.html" class="logo">{LOGO_SVG}<b>bela<span>connect</span></b></a>
        <p>Installateur indépendant en vidéosurveillance, alarme et informatique pour les professionnels des Alpes-Maritimes.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="videosurveillance.html">Vidéosurveillance</a></li>
          <li><a href="alarme.html">Alarme</a></li>
          <li><a href="informatique.html">Informatique &amp; réseau</a></li>
          <li><a href="informatique.html#baies">Remise au propre de baies</a></li>
          <li><a href="videosurveillance.html#packs">Packs caméras</a></li>
        </ul>
      </div>
      <div>
        <h4>Infos</h4>
        <ul>
          <li><a href="contact.html">Contact &amp; devis</a></li>
          <li><a href="mentions-legales.html">Mentions légales</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Alpes-Maritimes (06)</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© <span id="year">2026</span> BelaConnect — Tous droits réservés</span>
      <span>Dahua · Hikvision · Ajax · TP-Link</span>
    </div>
  </div>
</footer>

<a href="tel:{PHONE_LINK}" class="btn btn-primary call-fab">{ic('phone')} Appeler BelaConnect</a>
<script src="assets/main.js"></script>
</body>
</html>
"""


# =============================================================================
# ACCUEIL
# =============================================================================
HOME_FAQ = [
    ("Où intervenez-vous ?",
     "Dans tout le département des Alpes-Maritimes (06), sur le littoral comme dans l'arrière-pays."),
    ("Le devis est-il gratuit ?",
     "Oui. Nous nous déplaçons gratuitement dans vos locaux pour étudier votre besoin, puis nous vous remettons un devis détaillé, sans engagement."),
    ("Fournissez-vous le matériel ?",
     "Oui, nous fournissons du matériel professionnel (Dahua, Hikvision, Ajax, TP-Link) adapté à votre besoin. Nous pouvons aussi installer un matériel que vous possédez déjà."),
    ("Pouvez-vous gérer de gros chantiers ?",
     "Oui. Pour les installations importantes, nous intervenons en équipe afin de respecter vos délais."),
    ("Assurez-vous la maintenance après l'installation ?",
     "Oui, nous proposons la maintenance de vos installations de vidéosurveillance, d'alarme et de votre parc informatique."),
]

home = f"""
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="kicker">Sécurité · Réseau · Informatique · Alpes-Maritimes</p>
        <h1>Sécurité et informatique pour les professionnels du <em>06</em></h1>
        <p class="lead">Vidéosurveillance, alarme, réseau, Wi-Fi et informatique : nous installons et entretenons les équipements des commerces, bureaux, entrepôts, chantiers et copropriétés, partout dans les Alpes-Maritimes.</p>
        <div class="hero-cta">
          <a href="contact.html" class="btn btn-primary">Demander un devis gratuit</a>
          <a href="#services" class="btn btn-ghost">Voir nos services</a>
        </div>
      </div>
      <aside class="hero-info">
        <dl>
          <dt>Services</dt><dd>Vidéosurveillance, alarme, réseau, informatique</dd>
          <dt>Clients</dt><dd>Entreprises, commerces, copropriétés</dd>
          <dt>Devis</dt><dd>Gratuit, après visite sur place</dd>
          <dt>Zone</dt><dd>Tout le département des Alpes-Maritimes</dd>
          <dt>Matériel</dt><dd>Dahua, Hikvision, Ajax, TP-Link</dd>
        </dl>
        <a href="tel:{PHONE_LINK}" class="hero-phone">{ic('phone')} {PHONE_DISPLAY}</a>
      </aside>
    </div>
  </section>
{brands(["Dahua", "Hikvision", "Ajax", "TP-Link"])}

  <section id="services">
    <div class="wrap">
      <div class="section-head">
        <h2>Ce que nous faisons</h2>
        <p>La vidéosurveillance et l'alarme sont notre cœur de métier. L'informatique vient en complément, pour que tout fonctionne sur un même réseau.</p>
      </div>
      <div class="grid-3">
        <a href="videosurveillance.html" class="card main svc-video">
          <div class="icon">{ic('cam')}</div>
          <h3>Vidéosurveillance</h3>
          <p>Caméras intérieures et extérieures, filaires ou sans fil, avec enregistreur. Vous voyez les images en direct sur votre téléphone.</p>
          {checks(["Dahua et Hikvision", "Vision de nuit", "Packs 4 et 8 caméras"])}
          <span class="more">En savoir plus {ic('arrow')}</span>
        </a>
        <a href="alarme.html" class="card main svc-alarm">
          <div class="icon">{ic('alarm')}</div>
          <h3>Alarme</h3>
          <p>Alarmes Ajax contre l'intrusion. Vous êtes prévenu sur votre téléphone dès qu'un détecteur se déclenche.</p>
          {checks(["Sans fil ou filaire", "Badge ou code par salarié", "Couplage aux caméras"])}
          <span class="more">En savoir plus {ic('arrow')}</span>
        </a>
        <a href="informatique.html" class="card svc-it">
          <div class="icon">{ic('pc')}</div>
          <h3>Informatique et réseau</h3>
          <p>Câblage, Wi-Fi pro, postes de travail, sauvegardes et dépannage pour les entreprises.</p>
          {checks(["Réseau et Wi-Fi TP-Link", "Remise au propre de baies", "Postes, serveurs, maintenance"])}
          <span class="more">En savoir plus {ic('arrow')}</span>
        </a>
      </div>
    </div>
  </section>

  <section class="why">
    <div class="wrap">
      <div class="section-head">
        <h2>Pourquoi choisir BelaConnect</h2>
      </div>
      <div class="grid-4 why-grid">
        <div><b>06</b><h3>tout le département</h3><p>Nous intervenons partout dans les Alpes-Maritimes, sur le littoral comme dans l'arrière-pays.</p></div>
        <div><b>1</b><h3>seul interlocuteur</h3><p>Du devis à la maintenance, vous avez toujours affaire à la même personne.</p></div>
        <div><b>0 €</b><h3>pour la visite et le devis</h3><p>Nous venons voir vos locaux avant de chiffrer quoi que ce soit, sans engagement.</p></div>
        <div><b>4</b><h3>marques professionnelles</h3><p>Dahua, Hikvision, Ajax et TP-Link : du matériel fiable, conçu pour durer.</p></div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap split top">
      <div>
        <h2>Pour quels locaux ?</h2>
        <p>Chaque site est différent. Nous venons voir les lieux avant de proposer quoi que ce soit : surface, accès, éclairage, horaires d'ouverture.</p>
      </div>
      <ul class="plain-list">
        <li><b>Commerces</b> : surface de vente, caisse, réserve.</li>
        <li><b>Restaurants et hôtels</b> : salle, cuisine, entrées, parking.</li>
        <li><b>Bureaux et cabinets</b> : alarme des locaux, réseau, postes.</li>
        <li><b>Entrepôts et ateliers</b> : quais, périmètre, vision de nuit.</li>
        <li><b>Chantiers</b> : protection du matériel et des engins.</li>
        <li><b>Copropriétés</b> : halls, parkings, locaux communs (<a href="videosurveillance.html#copropriete" class="inline-link">en savoir plus</a>).</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap split">
      <div>
        <h2>Deux packs caméras</h2>
        <p>Caméras intérieures ou extérieures, enregistreur, pose et réglage sur votre téléphone. Le prix dépend de vos locaux : nous l'établissons après la visite.</p>
        <div class="hero-cta">
          <a href="videosurveillance.html#packs" class="btn btn-dark">Voir le détail des packs</a>
        </div>
      </div>
      <div class="grid-2">
        <a href="videosurveillance.html#pack-4" class="card pack">
          <div class="pack-top"><span class="big">4</span><span class="unit">caméras</span></div>
          <p>+ enregistreur. Pour un commerce ou un petit bureau.</p>
        </a>
        <a href="videosurveillance.html#pack-8" class="card pack featured">
          <div class="pack-top"><span class="big">8</span><span class="unit">caméras</span></div>
          <p>+ enregistreur. Pour les grands locaux et les extérieurs.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <div class="section-head">
        <h2>Comment ça se passe</h2>
      </div>
      <div class="grid-3 steps">
        <div class="step"><h3>Visite sur place</h3><p>Nous venons voir vos locaux, gratuitement, et faisons le tour des points sensibles avec vous.</p></div>
        <div class="step"><h3>Devis détaillé</h3><p>Matériel, emplacements, délais. Vous décidez sans engagement.</p></div>
        <div class="step"><h3>Installation</h3><p>Pose, tests, réglage de votre téléphone. Nous vous montrons comment tout utiliser.</p></div>
      </div>
      <p class="aside-note">Pour les gros chantiers, nous intervenons en équipe. Après l'installation, nous pouvons assurer la maintenance.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head">
        <h2>Questions fréquentes</h2>
      </div>
      {faq(HOME_FAQ)}
    </div>
  </section>
{cta_band()}
"""

# =============================================================================
# VIDÉOSURVEILLANCE
# =============================================================================
PACK_COMMON = ["Caméras intérieures et/ou extérieures, au choix",
               "Enregistreur avec disque dur",
               "Installation et câblage (ou pose sans fil)",
               "Configuration sur votre smartphone",
               "Prise en main et explications"]

VIDEO_FAQ = [
    ("Puis-je voir mes caméras depuis mon téléphone ?",
     "Oui. Nous configurons l'application du fabricant sur votre smartphone (et celui de vos collaborateurs si besoin) pour voir le direct et les enregistrements à distance."),
    ("Combien de temps les images sont-elles conservées ?",
     "Cela dépend du nombre de caméras et de la capacité du disque de l'enregistreur. Nous réglons la durée selon vos besoins et la réglementation, qui recommande en général de ne pas dépasser un mois."),
    ("Filaire ou sans fil, que choisir ?",
     "Le filaire est le plus fiable pour une installation durable ; le sans fil est plus rapide à poser quand passer des câbles est compliqué. Nous vous conseillons lors de la visite."),
    ("Les caméras fonctionnent-elles la nuit ?",
     "Oui, les caméras que nous installons ont la vision de nuit. Certains modèles offrent même une image en couleur dans l'obscurité."),
    ("Installez-vous des caméras en copropriété ?",
     "Oui : halls, parkings, garages et locaux communs. Nous fournissons un devis détaillé à présenter en assemblée générale, puisque l'installation doit y être votée, et nous orientons les caméras uniquement sur les parties communes."),
    ("Ai-je des obligations légales en tant que professionnel ?",
     "Oui : informer les personnes filmées par un panneau, informer vos salariés, et demander une autorisation en préfecture pour filmer un lieu ouvert au public. Nous vous indiquons les démarches lors de l'installation."),
]

video = page_hero(
    "Vidéosurveillance",
    "Vidéosurveillance <em>pour professionnels</em> dans les Alpes-Maritimes",
    "Installation de caméras Dahua et Hikvision, intérieures et extérieures, filaires ou sans fil, avec enregistreur et accès à distance depuis votre smartphone.",
    "Spécialité BelaConnect") + f"""
{brands(["Dahua", "Hikvision"], "Marques installées")}

  <section>
    <div class="wrap">
      <div class="section-head">
        <h2>Ce que nous installons</h2>
        <p>Nous choisissons le matériel, le posons et le réglons. Vous n'avez rien à gérer.</p>
      </div>
      <div class="grid-3">
        <div class="card"><div class="icon">{ic('cam')}</div><h3>Caméras extérieures</h3><p>Façades, entrées, parkings, quais de livraison et périmètre. Modèles résistants aux intempéries.</p></div>
        <div class="card"><div class="icon">{ic('dome')}</div><h3>Caméras intérieures</h3><p>Surface de vente, caisse, réserve, bureaux, couloirs. Modèles discrets type dôme.</p></div>
        <div class="card"><div class="icon">{ic('hdd')}</div><h3>Enregistreur</h3><p>Enregistrement continu ou sur détection, avec disque dur dimensionné selon vos besoins.</p></div>
      </div>
    </div>
  </section>

  <section class="alt" id="packs">
    <div class="wrap">
      <div class="section-head">
        <h2>Les packs caméras</h2>
        <p>Deux packs complets pour équiper vos locaux rapidement. Le prix dépend de vos locaux : nous l'établissons après la visite, qui est gratuite. Au-delà de 8 caméras, ou pour ajouter une alarme, nous réalisons une étude sur mesure.</p>
      </div>
      <div class="grid-2">
        <div class="card pack" id="pack-4">
          <div class="pack-top"><span class="big">4</span><span class="unit">caméras + enregistreur</span></div>
          <p>Idéal pour un commerce, un restaurant, un cabinet ou un petit bureau.</p>
          <div class="grow">{checks(PACK_COMMON)}</div>
          <div class="price">Tarif sur devis — visite gratuite</div>
          <a href="contact.html?besoin=pack-4" class="btn btn-dark">Demander un devis Pack 4 {ic('arrow')}</a>
        </div>
        <div class="card pack featured" id="pack-8">
          <span class="tag">Grands locaux</span>
          <div class="pack-top"><span class="big">8</span><span class="unit">caméras + enregistreur</span></div>
          <p>Pour les grands commerces, entrepôts, ateliers et sites avec extérieurs.</p>
          <div class="grow">{checks(PACK_COMMON)}</div>
          <div class="price">Tarif sur devis — visite gratuite</div>
          <a href="contact.html?besoin=pack-8" class="btn btn-primary">Demander un devis Pack 8 {ic('arrow')}</a>
        </div>
      </div>
    </div>
  </section>

  <section id="copropriete">
    <div class="wrap split top">
      <div>
        <h2>Vidéosurveillance en copropriété</h2>
        <p>Halls d'entrée, parkings, garages, locaux vélos et poubelles : nous équipons les parties communes des résidences et travaillons avec le syndic et le conseil syndical, de la visite jusqu'à la mise en service.</p>
        {checks(["Visite gratuite et devis détaillé, à présenter en assemblée générale", "Caméras orientées uniquement sur les parties communes", "Accès aux images limité aux personnes autorisées", "Panneaux d'information des résidents fournis", "Maintenance de l'installation dans la durée"])}
        <div class="hero-cta"><a href="contact.html?besoin=copro" class="btn btn-dark">Demander un devis copropriété {ic('arrow')}</a></div>
      </div>
      <div class="note">
        {ic('info')}
        <div>
          <h3>Les règles à connaître</h3>
          <p>L'installation de caméras dans les parties communes doit être votée en assemblée générale. Les caméras ne doivent filmer ni l'intérieur des logements ni les portes palières, les résidents doivent être informés par des panneaux, et les images ne sont conservées que quelques jours, un mois au maximum. Nous vous aidons à préparer le projet en conséquence.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <div class="section-head">
        <h2>Au quotidien</h2>
      </div>
      <div class="grid-4">
        <div class="mini"><div class="icon dark">{ic('mobile')}</div><h3>Accès à distance</h3><p>Direct et enregistrements sur smartphone, tablette ou ordinateur.</p></div>
        <div class="mini"><div class="icon dark">{ic('eye')}</div><h3>Image haute définition</h3><p>Des images nettes pour identifier une personne ou une plaque.</p></div>
        <div class="mini"><div class="icon dark">{ic('moon')}</div><h3>Vision de nuit</h3><p>Une surveillance efficace 24 h/24, même sans éclairage.</p></div>
        <div class="mini"><div class="icon dark">{ic('bell')}</div><h3>Détection intelligente</h3><p>Alertes sur détection de personnes ou de véhicules, moins de fausses alertes.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head">
        <h2>Filaire ou sans fil ?</h2>
      </div>
      <div class="compare">
        <div class="card">
          <h3>{ic('cable')} Caméras filaires</h3>
          {checks(["Connexion la plus stable et la plus fiable", "Alimentation par le câble réseau (PoE)", "Idéal pour les installations durables et nombreuses"])}
          <p class="ideal"><b>Idéal pour :</b> entrepôts, bâtiments neufs ou en rénovation, sites avec beaucoup de caméras.</p>
        </div>
        <div class="card">
          <h3>{ic('nowire')} Caméras sans fil</h3>
          {checks(["Pose rapide, sans gros travaux", "Moins de câbles apparents", "Facile à compléter plus tard"])}
          <p class="ideal"><b>Idéal pour :</b> commerces en activité, locaux loués, bâtiments où passer des câbles est difficile.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">
      <div class="note">
        {ic('info')}
        <div>
          <h3>Vidéosurveillance et réglementation</h3>
          <p>En entreprise, filmer implique quelques obligations : panneau d'information, information des salariés et, pour un lieu ouvert au public, autorisation préfectorale. Nous plaçons les caméras en respectant ces règles et vous indiquons les démarches.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="tight">
    <div class="wrap split">
      <div >
        <h2>Maintenance</h2>
        <p>Vérification des caméras et de l'enregistreur, nettoyage, mises à jour, remplacement d'un équipement défectueux, ajout de caméras. Nous restons joignables après l'installation.</p>
      </div>
      <div class="card">
        {checks(["Contrôle du bon fonctionnement des caméras", "Vérification des enregistrements et du disque", "Mises à jour de sécurité", "Ajout ou déplacement de caméras", "Intervention en cas de panne"])}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head">
        <h2>Questions fréquentes</h2>
      </div>
      {faq(VIDEO_FAQ)}
    </div>
  </section>
{cta_band("Besoin de caméras pour vos locaux ?", "Visite gratuite sur place pour choisir un pack ou une installation sur mesure.")}
"""

# =============================================================================
# ALARME
# =============================================================================
ALARM_FAQ = [
    ("Pourquoi Ajax ?",
     "Ajax est une marque reconnue pour la fiabilité de ses alarmes : communications chiffrées, autonomie des détecteurs, application simple et très complète."),
    ("L'alarme fonctionne-t-elle en cas de coupure de courant ?",
     "Oui. La centrale dispose d'une batterie de secours et peut communiquer par carte SIM si internet est coupé."),
    ("Peut-on donner des accès différents à chaque salarié ?",
     "Oui. Chaque utilisateur dispose de son propre accès (application, badge ou code), et vous voyez qui a armé ou désarmé l'alarme."),
    ("L'alarme peut-elle fonctionner avec les caméras ?",
     "Oui. Alarme et vidéosurveillance se complètent : en cas d'alerte, vous pouvez vérifier immédiatement ce qui se passe grâce aux images."),
]

alarm = page_hero(
    "Alarme",
    "Alarme anti-intrusion <em>Ajax</em> pour vos locaux",
    "Des systèmes d'alarme fiables, sans fil ou filaires, pour protéger commerces, bureaux et entrepôts. Vous êtes alerté immédiatement sur votre téléphone.",
    "Spécialité BelaConnect") + f"""
{brands(["Ajax"], "Marque installée")}

  <section>
    <div class="wrap">
      <div class="section-head">
        <h2>Ce que comprend une alarme</h2>
        <p>Nous définissons avec vous les zones à protéger, puis choisissons les équipements.</p>
      </div>
      <div class="grid-3">
        <div class="card"><div class="icon">{ic('server')}</div><h3>Centrale d'alarme</h3><p>Le cœur du système, connecté à internet et au réseau mobile, avec batterie de secours.</p></div>
        <div class="card"><div class="icon">{ic('radar')}</div><h3>Détecteurs de mouvement</h3><p>Détection des intrusions dans les pièces, avec des modèles capables de prendre une photo pour vérifier l'alerte.</p></div>
        <div class="card"><div class="icon">{ic('door')}</div><h3>Détecteurs d'ouverture</h3><p>Portes, fenêtres, rideaux métalliques : l'alarme se déclenche dès l'ouverture.</p></div>
        <div class="card"><div class="icon">{ic('siren')}</div><h3>Sirènes</h3><p>Sirènes intérieures et extérieures puissantes pour faire fuir les intrus.</p></div>
        <div class="card"><div class="icon">{ic('lock')}</div><h3>Claviers et badges</h3><p>Armement et désarmement simples, avec un accès personnel par salarié.</p></div>
        <div class="card"><div class="icon">{ic('mobile')}</div><h3>Application mobile</h3><p>Alertes instantanées, armement à distance et historique des événements.</p></div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap split">
      <div >
        <h2>Depuis votre téléphone</h2>
        <p>Armez ou désarmez l'alarme à distance, recevez une notification à chaque événement et sachez qui a ouvert ou fermé les locaux.</p>
      </div>
      <div class="card">
        {checks(["Notification immédiate en cas d'intrusion", "Historique : qui a armé ou désarmé, et quand", "Accès personnalisés par salarié", "Fonctionne même en cas de coupure internet ou de courant"])}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head">
        <h2>Sans fil ou filaire ?</h2>
      </div>
      <div class="compare">
        <div class="card">
          <h3>{ic('nowire')} Alarme sans fil</h3>
          {checks(["Installation rapide, sans travaux", "Détecteurs sur pile longue durée", "Communication radio chiffrée"])}
          <p class="ideal"><b>Idéal pour :</b> commerces et bureaux en activité, locaux loués.</p>
        </div>
        <div class="card">
          <h3>{ic('cable')} Alarme filaire</h3>
          {checks(["Aucune pile à remplacer", "Adaptée aux grands bâtiments", "Parfaite lors de travaux ou en construction neuve"])}
          <p class="ideal"><b>Idéal pour :</b> entrepôts, grands sites, bâtiments neufs.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">
      <div class="note">
        {ic('cam')}
        <div>
          <h3>Alarme et caméras ensemble</h3>
          <p>L'alarme détecte et dissuade, les caméras vous permettent de vérifier et d'enregistrer. Nous installons souvent les deux ensemble.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head">
        <h2>Questions fréquentes</h2>
      </div>
      {faq(ALARM_FAQ)}
    </div>
  </section>
{cta_band("Protégez vos locaux contre l'intrusion", "Visite gratuite sur place pour définir les zones à protéger et vous remettre un devis détaillé.")}
"""

# =============================================================================
# INFORMATIQUE
# =============================================================================
IT_FAQ = [
    ("Intervenez-vous pour un simple dépannage ?",
     "Oui, nous intervenons aussi bien pour un dépannage ponctuel que pour l'installation complète ou la gestion de votre parc informatique."),
    ("Pouvez-vous fournir les ordinateurs et le matériel réseau ?",
     "Oui. Nous fournissons et configurons postes de travail, serveurs, NAS, imprimantes et équipements réseau, ou installons le matériel que vous avez déjà."),
    ("Pouvez-vous remettre au propre une baie existante ?",
     "Oui. Nous reprenons le câblage d'une baie déjà en place : tri des câbles, cordons à la bonne longueur, étiquetage des ports et plan de brassage. L'intervention est organisée pour limiter la coupure du réseau."),
    ("Proposez-vous un suivi régulier ?",
     "Oui, la maintenance de votre parc est possible : mises à jour, vérification des sauvegardes, contrôle de la sécurité et interventions en cas de problème."),
]

it = page_hero(
    "Informatique & réseau",
    "Informatique <em>d'entreprise</em> &amp; réseau",
    "Postes de travail, serveurs, réseau, Wi-Fi professionnel, remise au propre de baies, sauvegardes et sécurité. Nous installons et entretenons toute l'informatique de votre entreprise.") + f"""
  <section>
    <div class="wrap">
      <div class="section-head">
        <h2>Nos prestations informatiques</h2>
        <p>Vos caméras, votre alarme et votre informatique reposent sur le même réseau : autant confier l'ensemble à un seul interlocuteur.</p>
      </div>
      <div class="grid-3">
        <div class="card"><div class="icon">{ic('network')}</div><h3>Réseau &amp; câblage</h3><p>Câblage réseau, baie de brassage, switchs et routeurs pour un réseau rapide et organisé.</p><a href="#baies" class="more">Remise au propre de baies {ic('arrow')}</a></div>
        <div class="card"><div class="icon">{ic('wifi')}</div><h3>Wi-Fi professionnel</h3><p>Bornes TP-Link pour couvrir tous vos locaux, avec un réseau invités séparé et sécurisé.</p></div>
        <div class="card"><div class="icon">{ic('pc')}</div><h3>Postes de travail</h3><p>Fourniture, installation et configuration des ordinateurs, imprimantes et périphériques.</p></div>
        <div class="card"><div class="icon">{ic('server')}</div><h3>Serveurs &amp; stockage</h3><p>Serveurs, NAS et partage de fichiers pour travailler en équipe en toute sécurité.</p></div>
        <div class="card"><div class="icon">{ic('backup')}</div><h3>Sauvegardes</h3><p>Mise en place de sauvegardes automatiques pour ne jamais perdre vos données.</p></div>
        <div class="card"><div class="icon">{ic('lock')}</div><h3>Sécurité informatique</h3><p>Pare-feu, antivirus, mises à jour et bonnes pratiques pour protéger votre activité.</p></div>
      </div>
    </div>
  </section>


  <section class="alt" id="baies">
    <div class="wrap">
      <div class="section-head">
        <h2>Remise au propre de baies</h2>
        <p>Une baie de brassage en désordre, ce sont des pannes difficiles à trouver, des équipements qui chauffent et des interventions qui durent. Nous la remettons au propre, en organisant le chantier pour limiter la coupure du réseau.</p>
      </div>
      <div class="compare">
        <div class="card">
          <h3>{ic('cable')} Avant</h3>
          <ul class="plain-list">
            <li>Câbles emmêlés, de toutes les longueurs</li>
            <li>Ports non identifiés : impossible de savoir qui est branché où</li>
            <li>Mauvaise circulation de l'air, équipements qui chauffent</li>
            <li>Chaque dépannage prend du temps</li>
          </ul>
        </div>
        <div class="card main">
          <h3>{ic('server')} Après</h3>
          {checks(["Câbles inutiles retirés, cordons à la bonne longueur", "Passe-câbles et code couleur", "Chaque port repéré et étiqueté", "Switchs, box, enregistreur et onduleur rangés", "Plan de brassage remis en fin d'intervention"])}
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap split">
      <div >
        <h2>Dépannage et maintenance</h2>
        <p>Un poste qui ne démarre plus, un réseau lent, une imprimante capricieuse ? Nous intervenons rapidement, et pouvons suivre votre parc dans la durée pour éviter les pannes.</p>
      </div>
      <div class="card">
        {checks(["Dépannage sur site", "Mises à jour et entretien des postes", "Vérification régulière des sauvegardes", "Conseils pour faire évoluer votre équipement"])}
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <div class="section-head">
        <h2>Questions fréquentes</h2>
      </div>
      {faq(IT_FAQ)}
    </div>
  </section>
{cta_band("Un projet informatique ou un dépannage ?", "Expliquez-nous votre besoin, nous vous rappelons rapidement.")}
"""

# =============================================================================
# PACKS
# =============================================================================
PACK_COMMON = ["Caméras intérieures et/ou extérieures, au choix",
               "Enregistreur avec disque dur",
               "Installation et câblage (ou pose sans fil)",
               "Configuration sur votre smartphone",
               "Prise en main et explications"]

# =============================================================================
# CONTACT
# =============================================================================
contact = page_hero(
    "Contact",
    "Demandez votre <em>devis gratuit</em>",
    "Décrivez votre projet en quelques mots. Nous vous rappelons pour fixer une visite gratuite sur place, partout dans les Alpes-Maritimes.") + f"""
  <section>
    <div class="wrap contact-grid">
      <div class="contact-info">
        <a class="ci" href="tel:{PHONE_LINK}">
          <div class="ci-icon">{ic('phone')}</div>
          <div><small>Téléphone</small><strong>{PHONE_DISPLAY}</strong></div>
        </a>
        <a class="ci" href="mailto:{EMAIL}">
          <div class="ci-icon">{ic('mail')}</div>
          <div><small>Email</small><strong>{EMAIL}</strong></div>
        </a>
        <div class="ci">
          <div class="ci-icon">{ic('pin')}</div>
          <div><small>Zone d'intervention</small><strong>Tout le département des Alpes-Maritimes (06)</strong></div>
        </div>
        <div class="ci">
          <div class="ci-icon">{ic('euro')}</div>
          <div><small>Devis</small><strong>Gratuit, après visite sur place</strong></div>
        </div>
      </div>

      <form id="devis" class="quote" data-to="{EMAIL}" novalidate>
        <div class="full">
          <label for="f-entreprise">Entreprise <span class="opt">(facultatif)</span></label>
          <input id="f-entreprise" name="entreprise" autocomplete="organization">
        </div>
        <div>
          <label for="f-nom">Nom *</label>
          <input id="f-nom" name="nom" autocomplete="name" required>
        </div>
        <div>
          <label for="f-tel">Téléphone *</label>
          <input id="f-tel" name="tel" type="tel" autocomplete="tel" required>
        </div>
        <div>
          <label for="f-mail">Email <span class="opt">(facultatif)</span></label>
          <input id="f-mail" name="email" type="email" autocomplete="email">
        </div>
        <div>
          <label for="f-ville">Ville *</label>
          <input id="f-ville" name="ville" autocomplete="address-level2" required>
        </div>
        <div class="full">
          <label for="f-besoin">Votre besoin</label>
          <select id="f-besoin" name="besoin">
            <option value="video">Vidéosurveillance</option>
            <option value="pack-4">Pack 4 caméras + enregistreur</option>
            <option value="pack-8">Pack 8 caméras + enregistreur</option>
            <option value="alarme">Alarme</option>
            <option value="video-alarme">Vidéosurveillance + alarme</option>
            <option value="copro">Vidéosurveillance en copropriété</option>
            <option value="info">Informatique &amp; réseau</option>
            <option value="baie">Remise au propre de baie</option>
            <option value="maintenance">Maintenance / dépannage</option>
            <option value="autre">Autre</option>
          </select>
        </div>
        <div class="full">
          <label for="f-msg">Votre projet <span class="opt">(facultatif)</span></label>
          <textarea id="f-msg" name="message" placeholder="Ex. : commerce de 150 m², 6 caméras dont 2 extérieures, consultables sur téléphone"></textarea>
        </div>
        <p id="form-error" class="form-error full" role="alert">Merci de remplir votre nom, votre téléphone et votre ville.</p>
        <div class="full">
          <button type="submit" class="btn btn-primary">Envoyer ma demande {ic('arrow')}</button>
        </div>
        <p class="form-note full">En cliquant, votre application email s'ouvre avec votre demande pré-remplie : il ne vous reste qu'à l'envoyer. Vos informations servent uniquement à répondre à votre demande (voir les <a href="mentions-legales.html" style="text-decoration:underline">mentions légales</a>).</p>
      </form>
    </div>
  </section>
"""

# =============================================================================
# MENTIONS LÉGALES
# =============================================================================
legal = f"""
  <section class="hero small">
    <div class="wrap hero-inner">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> / Mentions légales</nav>
      <h1>Mentions légales</h1>
    </div>
  </section>
  <section>
    <div class="wrap prose">
      <h2>Éditeur du site</h2>
      <p>BelaConnect — {OWNER_NAME}, entrepreneur individuel (micro-entreprise).<br>
      Adresse : {OWNER_ADDRESS}<br>
      SIREN : {SIREN}<br>
      TVA non applicable, article 293 B du Code général des impôts.<br>
      Téléphone : {PHONE_DISPLAY} — Email : <a href="mailto:{EMAIL}">{EMAIL}</a><br>
      Directeur de la publication : {OWNER_NAME}.</p>

      <h2>Hébergement</h2>
      <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis — <a href="https://github.com" rel="noopener">github.com</a>.</p>

      <h2>Propriété intellectuelle</h2>
      <p>L'ensemble des contenus de ce site (textes, visuels, logo) est la propriété de BelaConnect, sauf mention contraire. Toute reproduction sans autorisation est interdite. Les marques citées (Dahua, Hikvision, Ajax, TP-Link) appartiennent à leurs propriétaires respectifs.</p>

      <h2>Données personnelles</h2>
      <p>Ce site ne dépose aucun cookie publicitaire ni de mesure d'audience. Le formulaire de contact ne stocke aucune donnée sur le site : il prépare un email que vous choisissez d'envoyer.</p>
      <p>Les informations que vous nous transmettez (nom, téléphone, email, ville, description du projet) sont utilisées uniquement pour répondre à votre demande et établir un devis. Elles ne sont jamais cédées à des tiers et sont conservées au maximum 3 ans après le dernier contact.</p>
      <p>Conformément au RGPD, vous disposez d'un droit d'accès, de rectification et de suppression de vos données : écrivez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a>. Vous pouvez également adresser une réclamation à la CNIL (<a href="https://www.cnil.fr" rel="noopener">cnil.fr</a>).</p>

      <h2>Polices de caractères</h2>
      <p>Le site utilise la police Barlow, chargée depuis Google Fonts.</p>
    </div>
  </section>
"""

# =============================================================================
# 404
# =============================================================================
notfound = f"""
  <section class="hero">
    <div class="wrap hero-inner">
      <p class="kicker">Erreur 404</p>
      <h1>Cette page <em>n'existe pas.</em></h1>
      <p class="lead">Le lien est peut-être incorrect ou la page a été déplacée.</p>
      <div class="hero-cta">
        <a href="index.html" class="btn btn-primary">Retour à l'accueil {ic('arrow')}</a>
        <a href="contact.html" class="btn btn-ghost">Nous contacter</a>
      </div>
    </div>
  </section>
"""

PAGES = [
    ("index.html", "Vidéosurveillance, alarme et informatique pour professionnels (06) | BelaConnect",
     "Installation de vidéosurveillance, d'alarmes, de réseaux et d'informatique pour les entreprises, commerces et copropriétés des Alpes-Maritimes (06). Dahua, Hikvision, Ajax, TP-Link. Devis gratuit sur place.",
     home, faq_jsonld(HOME_FAQ)),
    ("videosurveillance.html", "Installation de caméras de surveillance pour professionnels (06) | BelaConnect",
     "Pose de caméras Dahua et Hikvision intérieures et extérieures, filaires ou sans fil, avec enregistreur et accès smartphone. Packs 4 et 8 caméras, copropriétés. Intervention dans tout le 06.",
     video, faq_jsonld(VIDEO_FAQ)),
    ("alarme.html", "Installation d'alarme Ajax pour commerces et bureaux (06) | BelaConnect",
     "Installation d'alarmes anti-intrusion Ajax sans fil ou filaires pour commerces, bureaux et entrepôts dans les Alpes-Maritimes. Alertes sur smartphone. Devis gratuit.",
     alarm, faq_jsonld(ALARM_FAQ)),
    ("informatique.html", "Informatique d'entreprise, réseau, baies et Wi-Fi pro (06) | BelaConnect",
     "Réseau, câblage, remise au propre de baies de brassage, Wi-Fi professionnel TP-Link, postes, serveurs, sauvegardes et dépannage informatique pour les entreprises du 06.",
     it, faq_jsonld(IT_FAQ)),
    ("contact.html", "Devis gratuit vidéosurveillance et alarme (06) | BelaConnect",
     "Demandez un devis gratuit pour votre projet de vidéosurveillance, d'alarme ou d'informatique dans les Alpes-Maritimes. Visite sur place offerte.",
     contact, ""),
    ("mentions-legales.html", "Mentions légales — BelaConnect",
     "Mentions légales et politique de confidentialité du site BelaConnect.",
     legal, '\n<meta name="robots" content="noindex">'),
    ("404.html", "Page introuvable — BelaConnect",
     "Cette page n'existe pas.",
     notfound, '\n<meta name="robots" content="noindex">'),
]


def main():
    for filename, title, desc, body, extra in PAGES:
        # Espace insécable avant « ? » et « ! » (typographie française)
        body = body.replace(" ?", "&nbsp;?").replace(" !", "&nbsp;!")
        body = body.replace('<section class="hero">', '<section class="hero">' + WAVES, 1)
        body = body.replace('<section class="hero small">', '<section class="hero small">' + WAVES, 1)
        (ROOT / filename).write_text(layout(filename, title, desc, body, extra), encoding="utf-8")
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for filename, *_ in PAGES:
        if filename in ("404.html", "mentions-legales.html"):
            continue
        loc = SITE_URL + "/" + ("" if filename == "index.html" else filename)
        sitemap.append(f"  <url><loc>{loc}</loc><lastmod>{date.today().isoformat()}</lastmod></url>")
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    (ROOT / "packs.html").write_text(
        '<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><title>Packs caméras — BelaConnect</title>'
        f'<link rel="canonical" href="{SITE_URL}/videosurveillance.html#packs">'
        '<meta name="robots" content="noindex">'
        '<meta http-equiv="refresh" content="0; url=videosurveillance.html#packs"></head>'
        '<body><p>Les packs sont maintenant sur la page <a href="videosurveillance.html#packs">Vidéosurveillance</a>.</p></body></html>\n',
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nDisallow: /carnet/\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print("Pages générées :", ", ".join(p[0] for p in PAGES))


if __name__ == "__main__":
    main()
