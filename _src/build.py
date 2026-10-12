#!/usr/bin/env python3
"""Génère les pages HTML du site BelaConnect.

Les coordonnées, l'en-tête et le pied de page sont définis une seule fois ici.
Après modification : python3 _src/build.py (depuis la racine du dépôt).
Le dossier _src n'est pas publié (Jekyll ignore les dossiers commençant par « _ »).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- Coordonnées (À COMPLÉTER) ------------------------------------------------
PHONE_DISPLAY = "06 00 00 00 00"      # TODO : vrai numéro
PHONE_LINK = "+33600000000"           # TODO : même numéro au format international
EMAIL = "contact@belaconnect.fr"      # TODO : adresse à créer chez Hostinger
OWNER_NAME = "[Prénom Nom]"           # TODO : nom de l'entrepreneur
OWNER_ADDRESS = "[Adresse professionnelle], Alpes-Maritimes"  # TODO
SIRET = "[SIRET en cours d'attribution]"  # TODO
SITE_URL = "https://belaconnect.fr"
CITIES = ["Nice", "Cannes", "Antibes", "Cagnes-sur-Mer", "Grasse", "Menton",
          "Saint-Laurent-du-Var", "Sophia Antipolis", "Mandelieu", "Vence", "Carros", "Monaco"]

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

LOGO_SVG = '<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#16233F"/><path d="M20 16h14a10 10 0 0 1 4 19 10 10 0 0 1-4 19H20z" fill="none" stroke="#22D3EE" stroke-width="6" stroke-linejoin="round"/></svg>'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230B1426'/%3E%3Cpath d='M20 16h14a10 10 0 0 1 4 19 10 10 0 0 1-4 19H20z' fill='none' stroke='%2322D3EE' stroke-width='6' stroke-linejoin='round'/%3E%3C/svg%3E"

NAV = [
    ("index.html", "Accueil"),
    ("videosurveillance.html", "Vidéosurveillance"),
    ("alarme.html", "Alarme"),
    ("informatique.html", "Informatique & réseau"),
    ("packs.html", "Packs"),
]


CURRENT = ' aria-current="page"'


def ic(name):
    return f'<svg aria-hidden="true"><use href="#i-{name}"/></svg>'


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{ic('check')} {t}</li>" for t in items) + "</ul>"


def faq(items):
    return '<div class="faq reveal">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def faq_jsonld(items):
    import json, re
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in items]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def cta_band(title="Un projet de sécurité pour vos locaux ?",
             text="Nous venons sur place, étudions vos besoins et vous remettons un devis gratuit et sans engagement."):
    return f"""
  <section class="tight">
    <div class="wrap">
      <div class="cta-band reveal">
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
    b = f'<div class="badge"><i></i> {badge}</div>' if badge else ""
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


def layout(filename, title, description, body, extra_head=""):
    links = "\n      ".join(
        f'<a href="{href}"{CURRENT if href == filename else ""}>{label}</a>'
        for href, label in NAV)
    contact_current = CURRENT if filename == "contact.html" else ""
    canonical = SITE_URL + "/" + ("" if filename == "index.html" else filename)
    org = ('{"@context":"https://schema.org","@type":"LocalBusiness","name":"BelaConnect",'
           '"description":"Installation de vidéosurveillance, alarmes et informatique pour les professionnels des Alpes-Maritimes.",'
           f'"url":"{SITE_URL}/","telephone":"{PHONE_LINK}","email":"{EMAIL}",'
           '"areaServed":{"@type":"AdministrativeArea","name":"Alpes-Maritimes"},'
           '"address":{"@type":"PostalAddress","addressRegion":"Alpes-Maritimes","addressCountry":"FR"}}')
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="fr_FR">
<meta name="theme-color" content="#0B1426">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">{org}</script>{extra_head}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
{ICONS}

<header class="site-header">
  <div class="wrap nav">
    <a href="index.html" class="logo" aria-label="BelaConnect, accueil">{LOGO_SVG}Bela<span>Connect</span></a>
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
        <a href="index.html" class="logo">{LOGO_SVG}Bela<span>Connect</span></a>
        <p>Installation de vidéosurveillance, d'alarmes et d'équipements informatiques pour les professionnels des Alpes-Maritimes.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="videosurveillance.html">Vidéosurveillance</a></li>
          <li><a href="alarme.html">Alarme</a></li>
          <li><a href="informatique.html">Informatique &amp; réseau</a></li>
          <li><a href="packs.html">Packs caméras</a></li>
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
    ("Dans quelles villes intervenez-vous ?",
     "Partout dans les Alpes-Maritimes : Nice, Cannes, Antibes, Grasse, Menton, Cagnes-sur-Mer, Sophia Antipolis et leurs environs."),
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
        <div class="badge"><i></i> Professionnels · Alpes-Maritimes</div>
        <h1>Vidéosurveillance &amp; alarme <em>pour les professionnels.</em></h1>
        <p class="lead">BelaConnect protège vos commerces, bureaux et entrepôts dans les Alpes-Maritimes : caméras consultables à distance, alarmes connectées et informatique d'entreprise. Installées et suivies par un technicien expérimenté.</p>
        <div class="hero-cta">
          <a href="contact.html" class="btn btn-primary">Demander un devis gratuit {ic('arrow')}</a>
          <a href="packs.html" class="btn btn-ghost">Voir les packs caméras</a>
        </div>
        <div class="hero-points">
          <span>{ic('check')} 5 ans d'expérience</span>
          <span>{ic('check')} Devis gratuit sur place</span>
          <span>{ic('check')} Matériel professionnel</span>
        </div>
      </div>
      <div class="hero-card" aria-hidden="true">
        <div class="hc-head"><span>Magasin — Nice</span><span class="hc-live"><i></i> En ligne</span></div>
        <div class="hc-cams">
          <div class="cam">{ic('cam')}<span class="rec">REC</span><b>Entrée</b></div>
          <div class="cam">{ic('cam')}<span class="rec">REC</span><b>Caisse</b></div>
          <div class="cam">{ic('cam')}<span class="rec">REC</span><b>Réserve</b></div>
          <div class="cam">{ic('cam')}<span class="rec">REC</span><b>Parking</b></div>
        </div>
        <div class="hc-rows">
          <div class="hc-row"><span>{ic('alarm')} Alarme des locaux</span><em>Activée</em></div>
          <div class="hc-row"><span>{ic('hdd')} Enregistreur</span><em>OK</em></div>
        </div>
      </div>
    </div>
  </section>

  <div class="brands" aria-label="Marques installées">
    <div class="wrap">
      <small>Matériel installé</small>
      <strong>DAHUA</strong><strong>HIKVISION</strong><strong>AJAX</strong><strong>TP-LINK</strong>
    </div>
  </div>

  <section>
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Nos services</div>
        <h2>Notre spécialité : la sécurité de vos locaux</h2>
        <p>De l'étude sur place à la mise en service, un seul interlocuteur pour la vidéosurveillance, l'alarme et l'informatique de votre entreprise.</p>
      </div>
      <div class="grid-3">
        <a href="videosurveillance.html" class="card main reveal">
          <span class="tag">Spécialité</span>
          <div class="icon dark">{ic('cam')}</div>
          <h3>Vidéosurveillance</h3>
          <p>Caméras intérieures et extérieures, filaires ou sans fil, avec enregistreur et accès à distance sur smartphone.</p>
          <span class="more">Découvrir {ic('arrow')}</span>
        </a>
        <a href="alarme.html" class="card main reveal">
          <span class="tag">Spécialité</span>
          <div class="icon dark">{ic('alarm')}</div>
          <h3>Alarme</h3>
          <p>Systèmes d'alarme Ajax pour protéger vos locaux contre l'intrusion, avec alertes instantanées sur votre téléphone.</p>
          <span class="more">Découvrir {ic('arrow')}</span>
        </a>
        <a href="informatique.html" class="card reveal">
          <div class="icon">{ic('pc')}</div>
          <h3>Informatique &amp; réseau</h3>
          <p>Postes, serveurs, réseau, Wi-Fi professionnel, sauvegardes et dépannage : toute l'informatique de votre entreprise.</p>
          <span class="more">Découvrir {ic('arrow')}</span>
        </a>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <div class="section-head center reveal">
        <div class="eyebrow">Pour qui</div>
        <h2>Des solutions adaptées à votre activité</h2>
        <p>Chaque local est différent : nous dimensionnons l'installation selon votre surface, vos accès et vos horaires.</p>
      </div>
      <div class="grid-3">
        <div class="card mini reveal"><div class="icon">{ic('shop')}</div><h3>Commerces</h3><p>Surveillance de la surface de vente, de la caisse et de la réserve.</p></div>
        <div class="card mini reveal"><div class="icon">{ic('food')}</div><h3>Restaurants &amp; hôtels</h3><p>Salle, cuisine, entrées et parkings, avec Wi-Fi clients séparé.</p></div>
        <div class="card mini reveal"><div class="icon">{ic('office')}</div><h3>Bureaux &amp; cabinets</h3><p>Alarme des locaux, réseau, postes de travail et sauvegardes.</p></div>
        <div class="card mini reveal"><div class="icon">{ic('box')}</div><h3>Entrepôts &amp; ateliers</h3><p>Caméras longue portée, vision de nuit, quais et périmètre.</p></div>
        <div class="card mini reveal"><div class="icon">{ic('crane')}</div><h3>Chantiers</h3><p>Protection du matériel et des engins sur site.</p></div>
        <div class="card mini reveal"><div class="icon">{ic('building')}</div><h3>Copropriétés</h3><p>Halls, parkings et locaux communs.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap split">
      <div class="reveal">
        <div class="eyebrow">Packs vidéosurveillance</div>
        <h2>Deux packs prêts à installer</h2>
        <p>Pour aller à l'essentiel, nous proposons deux packs complets avec caméras intérieures ou extérieures, enregistreur, installation et configuration sur votre smartphone.</p>
        <div class="hero-cta">
          <a href="packs.html" class="btn btn-dark">Voir les packs {ic('arrow')}</a>
        </div>
      </div>
      <div class="grid-2 reveal">
        <a href="packs.html#pack-4" class="card hover pack">
          <div class="pack-top"><span class="big">4</span><span class="unit">caméras</span></div>
          <p>+ enregistreur. Idéal pour un commerce ou un petit bureau.</p>
          <span class="more">Détails {ic('arrow')}</span>
        </a>
        <a href="packs.html#pack-8" class="card hover pack featured">
          <div class="pack-top"><span class="big">8</span><span class="unit">caméras</span></div>
          <p>+ enregistreur. Pour les grands locaux, entrepôts et sites étendus.</p>
          <span class="more">Détails {ic('arrow')}</span>
        </a>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <div class="section-head center reveal">
        <div class="eyebrow">Pourquoi BelaConnect</div>
        <h2>Un installateur de terrain, impliqué de A à Z</h2>
      </div>
      <div class="grid-4">
        <div class="mini reveal"><div class="icon dark">{ic('medal')}</div><h3>5 ans d'expérience</h3><p>Des dizaines de situations différentes, des conseils concrets.</p></div>
        <div class="mini reveal"><div class="icon dark">{ic('users')}</div><h3>Un seul interlocuteur</h3><p>La même personne du devis à la mise en service, et après.</p></div>
        <div class="mini reveal"><div class="icon dark">{ic('team')}</div><h3>Équipe sur gros chantiers</h3><p>Renfort d'équipe pour les installations importantes.</p></div>
        <div class="mini reveal"><div class="icon dark">{ic('tool')}</div><h3>Maintenance</h3><p>Suivi et entretien de vos équipements dans la durée.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Comment ça se passe</div>
        <h2>Trois étapes, et vos locaux sont protégés</h2>
      </div>
      <div class="grid-3 steps">
        <div class="card step reveal"><h3>Visite gratuite sur place</h3><p>Nous étudions vos locaux, vos points sensibles et vos contraintes.</p></div>
        <div class="card step reveal"><h3>Devis clair et détaillé</h3><p>Matériel, emplacement des équipements, délais : tout est indiqué, sans engagement.</p></div>
        <div class="card step reveal"><h3>Installation et prise en main</h3><p>Pose propre, tests complets, configuration de votre smartphone et explications.</p></div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap split">
      <div class="reveal">
        <div class="eyebrow">Zone d'intervention</div>
        <h2>Partout dans les Alpes-Maritimes</h2>
        <p>Nous intervenons dans tout le département, du littoral à l'arrière-pays.</p>
        <div class="cities">{"".join(f"<span>{c}</span>" for c in CITIES)}</div>
      </div>
      <div class="map-card reveal" aria-hidden="true">
        <svg viewBox="0 0 400 300">
          <defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#22D3EE" stop-opacity=".35"/><stop offset="1" stop-color="#22D3EE" stop-opacity="0"/></radialGradient></defs>
          <path d="M40 210 L70 150 L110 120 L150 70 L210 50 L270 60 L320 90 L350 130 L360 175 L330 205 L290 215 L250 230 L200 245 L150 240 L100 235 Z" fill="rgba(255,255,255,.05)" stroke="rgba(34,211,238,.6)" stroke-width="2" stroke-dasharray="6 6"/>
          <path d="M60 240 Q200 280 370 205" fill="none" stroke="rgba(96,165,250,.35)" stroke-width="10" stroke-linecap="round"/>
          <circle cx="255" cy="205" r="46" fill="url(#g)"/>
          <g fill="#22D3EE"><circle cx="255" cy="205" r="6"/><circle cx="160" cy="225" r="4.5"/><circle cx="195" cy="215" r="4.5"/><circle cx="135" cy="185" r="4.5"/><circle cx="330" cy="190" r="4.5"/><circle cx="215" cy="200" r="4"/></g>
          <g fill="#E2E8F0" font-family="Inter,sans-serif" font-size="13" font-weight="600">
            <text x="262" y="196">Nice</text><text x="124" y="244">Cannes</text><text x="186" y="236">Antibes</text><text x="98" y="178">Grasse</text><text x="300" y="180">Menton</text>
          </g>
          <text x="20" y="34" fill="#94A3B8" font-family="Inter,sans-serif" font-size="13" font-weight="700" letter-spacing="2">ALPES-MARITIMES (06)</text>
        </svg>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head center reveal">
        <div class="eyebrow">Questions fréquentes</div>
        <h2>Vous vous posez des questions ?</h2>
      </div>
      {faq(HOME_FAQ)}
    </div>
  </section>
{cta_band()}
"""

# =============================================================================
# VIDÉOSURVEILLANCE
# =============================================================================
VIDEO_FAQ = [
    ("Puis-je voir mes caméras depuis mon téléphone ?",
     "Oui. Nous configurons l'application du fabricant sur votre smartphone (et celui de vos collaborateurs si besoin) pour voir le direct et les enregistrements à distance."),
    ("Combien de temps les images sont-elles conservées ?",
     "Cela dépend du nombre de caméras et de la capacité du disque de l'enregistreur. Nous réglons la durée selon vos besoins et la réglementation, qui recommande en général de ne pas dépasser un mois."),
    ("Filaire ou sans fil, que choisir ?",
     "Le filaire est le plus fiable pour une installation durable ; le sans fil est plus rapide à poser quand passer des câbles est compliqué. Nous vous conseillons lors de la visite."),
    ("Les caméras fonctionnent-elles la nuit ?",
     "Oui, nos caméras disposent de la vision de nuit. Certains modèles offrent même une image en couleur dans l'obscurité."),
    ("Ai-je des obligations légales en tant que professionnel ?",
     "Oui : informer les personnes filmées par un panneau, informer vos salariés, et demander une autorisation en préfecture pour filmer un lieu ouvert au public. Nous vous indiquons les démarches lors de l'installation."),
]

video = page_hero(
    "Vidéosurveillance",
    "Vidéosurveillance <em>pour professionnels</em> dans les Alpes-Maritimes",
    "Installation de caméras Dahua et Hikvision, intérieures et extérieures, filaires ou sans fil, avec enregistreur et accès à distance depuis votre smartphone.",
    "Spécialité BelaConnect") + f"""
  <div class="brands"><div class="wrap"><small>Marques</small><strong>DAHUA</strong><strong>HIKVISION</strong></div></div>

  <section>
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Ce que nous installons</div>
        <h2>Une installation complète, prête à l'emploi</h2>
        <p>Nous choisissons, posons et configurons l'ensemble de votre système de vidéosurveillance.</p>
      </div>
      <div class="grid-3">
        <div class="card reveal"><div class="icon">{ic('cam')}</div><h3>Caméras extérieures</h3><p>Façades, entrées, parkings, quais de livraison et périmètre. Modèles résistants aux intempéries.</p></div>
        <div class="card reveal"><div class="icon">{ic('dome')}</div><h3>Caméras intérieures</h3><p>Surface de vente, caisse, réserve, bureaux, couloirs. Modèles discrets type dôme.</p></div>
        <div class="card reveal"><div class="icon">{ic('hdd')}</div><h3>Enregistreur</h3><p>Enregistrement continu ou sur détection, avec disque dur dimensionné selon vos besoins.</p></div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <div class="section-head center reveal">
        <div class="eyebrow">Fonctionnalités</div>
        <h2>Gardez un œil sur votre activité, où que vous soyez</h2>
      </div>
      <div class="grid-4">
        <div class="mini reveal"><div class="icon dark">{ic('mobile')}</div><h3>Accès à distance</h3><p>Direct et enregistrements sur smartphone, tablette ou ordinateur.</p></div>
        <div class="mini reveal"><div class="icon dark">{ic('eye')}</div><h3>Image haute définition</h3><p>Des images nettes pour identifier une personne ou une plaque.</p></div>
        <div class="mini reveal"><div class="icon dark">{ic('moon')}</div><h3>Vision de nuit</h3><p>Une surveillance efficace 24 h/24, même sans éclairage.</p></div>
        <div class="mini reveal"><div class="icon dark">{ic('bell')}</div><h3>Détection intelligente</h3><p>Alertes sur détection de personnes ou de véhicules, moins de fausses alertes.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Filaire ou sans fil</div>
        <h2>La technologie adaptée à vos locaux</h2>
      </div>
      <div class="compare">
        <div class="card reveal">
          <h3>{ic('cable')} Caméras filaires</h3>
          {checks(["Connexion la plus stable et la plus fiable", "Alimentation par le câble réseau (PoE)", "Idéal pour les installations durables et nombreuses"])}
          <p class="ideal"><b>Idéal pour :</b> entrepôts, bâtiments neufs ou en rénovation, sites avec beaucoup de caméras.</p>
        </div>
        <div class="card reveal">
          <h3>{ic('nowire')} Caméras sans fil</h3>
          {checks(["Pose rapide, sans gros travaux", "Moins de câbles apparents", "Facile à compléter plus tard"])}
          <p class="ideal"><b>Idéal pour :</b> commerces en activité, locaux loués, bâtiments où passer des câbles est difficile.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">
      <div class="note reveal">
        {ic('info')}
        <div>
          <h3>Vidéosurveillance et réglementation</h3>
          <p>En entreprise, filmer implique quelques obligations : panneau d'information, information des salariés et, pour un lieu ouvert au public, autorisation préfectorale. Nous positionnons les caméras en respectant ces règles et vous indiquons les démarches à effectuer.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="tight">
    <div class="wrap split">
      <div class="reveal">
        <div class="eyebrow">Maintenance</div>
        <h2>Une installation suivie dans le temps</h2>
        <p>Vérification des caméras et de l'enregistreur, nettoyage, mises à jour, remplacement d'un équipement défectueux, ajout de caméras : nous restons à vos côtés après l'installation.</p>
      </div>
      <div class="card reveal">
        {checks(["Contrôle du bon fonctionnement des caméras", "Vérification des enregistrements et du disque", "Mises à jour de sécurité", "Ajout ou déplacement de caméras", "Intervention en cas de panne"])}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head center reveal">
        <div class="eyebrow">Questions fréquentes</div>
        <h2>Vidéosurveillance : vos questions</h2>
      </div>
      {faq(VIDEO_FAQ)}
    </div>
  </section>
{cta_band("Besoin de caméras pour vos locaux ?", "Découvrez nos packs 4 et 8 caméras, ou demandez une étude sur mesure gratuite.")}
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
  <div class="brands"><div class="wrap"><small>Marque</small><strong>AJAX</strong></div></div>

  <section>
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Composition</div>
        <h2>Un système complet, dimensionné pour vos locaux</h2>
        <p>Nous définissons ensemble les zones à protéger et les équipements nécessaires.</p>
      </div>
      <div class="grid-3">
        <div class="card reveal"><div class="icon">{ic('server')}</div><h3>Centrale d'alarme</h3><p>Le cœur du système, connecté à internet et au réseau mobile, avec batterie de secours.</p></div>
        <div class="card reveal"><div class="icon">{ic('radar')}</div><h3>Détecteurs de mouvement</h3><p>Détection des intrusions dans les pièces, avec des modèles capables de prendre une photo pour vérifier l'alerte.</p></div>
        <div class="card reveal"><div class="icon">{ic('door')}</div><h3>Détecteurs d'ouverture</h3><p>Portes, fenêtres, rideaux métalliques : l'alarme se déclenche dès l'ouverture.</p></div>
        <div class="card reveal"><div class="icon">{ic('siren')}</div><h3>Sirènes</h3><p>Sirènes intérieures et extérieures puissantes pour faire fuir les intrus.</p></div>
        <div class="card reveal"><div class="icon">{ic('lock')}</div><h3>Claviers et badges</h3><p>Armement et désarmement simples, avec un accès personnel par salarié.</p></div>
        <div class="card reveal"><div class="icon">{ic('mobile')}</div><h3>Application mobile</h3><p>Alertes instantanées, armement à distance et historique des événements.</p></div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap split">
      <div class="reveal">
        <div class="eyebrow">Au quotidien</div>
        <h2>Vous gardez le contrôle depuis votre téléphone</h2>
        <p>Armez ou désarmez l'alarme à distance, recevez une notification à chaque événement et sachez qui a ouvert ou fermé les locaux.</p>
        {checks(["Notification immédiate en cas d'intrusion", "Historique : qui a armé ou désarmé, et quand", "Accès personnalisés par salarié", "Fonctionne même en cas de coupure internet ou de courant"])}
      </div>
      <div class="visual reveal" aria-hidden="true">
        <div class="hc-head"><span>Entrepôt — Carros</span><span class="hc-live"><i></i> Connecté</span></div>
        <div class="hc-rows">
          <div class="hc-row"><span>{ic('alarm')} Système</span><em>Armé</em></div>
          <div class="hc-row"><span>{ic('door')} Porte quai n°2</span><em>Fermée</em></div>
          <div class="hc-row"><span>{ic('radar')} Détecteur réserve</span><em>OK</em></div>
          <div class="hc-row"><span>{ic('users')} Armé par Julien · 19:42</span><em>Journal</em></div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Sans fil ou filaire</div>
        <h2>Ajax propose les deux</h2>
      </div>
      <div class="compare">
        <div class="card reveal">
          <h3>{ic('nowire')} Alarme sans fil</h3>
          {checks(["Installation rapide, sans travaux", "Détecteurs sur pile longue durée", "Communication radio chiffrée"])}
          <p class="ideal"><b>Idéal pour :</b> commerces et bureaux en activité, locaux loués.</p>
        </div>
        <div class="card reveal">
          <h3>{ic('cable')} Alarme filaire</h3>
          {checks(["Aucune pile à remplacer", "Adaptée aux grands bâtiments", "Parfaite lors de travaux ou en construction neuve"])}
          <p class="ideal"><b>Idéal pour :</b> entrepôts, grands sites, bâtiments neufs.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">
      <div class="note reveal">
        {ic('cam')}
        <div>
          <h3>Alarme + vidéosurveillance : la combinaison la plus efficace</h3>
          <p>L'alarme détecte et dissuade, les caméras vous permettent de vérifier et d'enregistrer. Nous installons les deux ensemble pour une protection complète de vos locaux.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head center reveal">
        <div class="eyebrow">Questions fréquentes</div>
        <h2>Alarme : vos questions</h2>
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
    ("Proposez-vous un suivi régulier ?",
     "Oui, la maintenance de votre parc est possible : mises à jour, vérification des sauvegardes, contrôle de la sécurité et interventions en cas de problème."),
]

it = page_hero(
    "Informatique & réseau",
    "Informatique <em>d'entreprise</em> &amp; réseau",
    "Postes de travail, serveurs, réseau, Wi-Fi professionnel, sauvegardes et sécurité : nous installons et entretenons toute l'informatique de votre entreprise.") + f"""
  <section>
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Nos prestations</div>
        <h2>Un seul prestataire pour tout votre informatique</h2>
        <p>Vos caméras, votre alarme et votre informatique reposent sur le même réseau : autant confier l'ensemble à un seul interlocuteur.</p>
      </div>
      <div class="grid-3">
        <div class="card reveal"><div class="icon">{ic('network')}</div><h3>Réseau &amp; câblage</h3><p>Câblage réseau, baie de brassage, switchs et routeurs pour un réseau rapide et organisé.</p></div>
        <div class="card reveal"><div class="icon">{ic('wifi')}</div><h3>Wi-Fi professionnel</h3><p>Bornes TP-Link pour couvrir tous vos locaux, avec un réseau invités séparé et sécurisé.</p></div>
        <div class="card reveal"><div class="icon">{ic('pc')}</div><h3>Postes de travail</h3><p>Fourniture, installation et configuration des ordinateurs, imprimantes et périphériques.</p></div>
        <div class="card reveal"><div class="icon">{ic('server')}</div><h3>Serveurs &amp; stockage</h3><p>Serveurs, NAS et partage de fichiers pour travailler en équipe en toute sécurité.</p></div>
        <div class="card reveal"><div class="icon">{ic('backup')}</div><h3>Sauvegardes</h3><p>Mise en place de sauvegardes automatiques pour ne jamais perdre vos données.</p></div>
        <div class="card reveal"><div class="icon">{ic('lock')}</div><h3>Sécurité informatique</h3><p>Pare-feu, antivirus, mises à jour et bonnes pratiques pour protéger votre activité.</p></div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap split">
      <div class="reveal">
        <div class="eyebrow">Dépannage &amp; maintenance</div>
        <h2>Une informatique qui fonctionne, tout simplement</h2>
        <p>Un poste qui ne démarre plus, un réseau lent, une imprimante capricieuse ? Nous intervenons rapidement, et pouvons suivre votre parc dans la durée pour éviter les pannes.</p>
        {checks(["Dépannage sur site", "Mises à jour et entretien des postes", "Vérification régulière des sauvegardes", "Conseils pour faire évoluer votre équipement"])}
      </div>
      <div class="visual reveal" aria-hidden="true">
        <div class="hc-head"><span>Cabinet — Antibes</span><span class="hc-live"><i></i> Réseau OK</span></div>
        <div class="hc-rows">
          <div class="hc-row"><span>{ic('wifi')} Wi-Fi bureaux</span><em>Excellent</em></div>
          <div class="hc-row"><span>{ic('wifi')} Wi-Fi invités</span><em>Isolé</em></div>
          <div class="hc-row"><span>{ic('backup')} Sauvegarde de cette nuit</span><em>Réussie</em></div>
          <div class="hc-row"><span>{ic('pc')} 12 postes</span><em>À jour</em></div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head center reveal">
        <div class="eyebrow">Questions fréquentes</div>
        <h2>Informatique : vos questions</h2>
      </div>
      {faq(IT_FAQ)}
    </div>
  </section>
{cta_band("Un projet informatique ou un dépannage ?", "Expliquez-nous votre besoin : nous vous recontactons rapidement.")}
"""

# =============================================================================
# PACKS
# =============================================================================
PACK_COMMON = ["Caméras intérieures et/ou extérieures, au choix",
               "Enregistreur avec disque dur",
               "Installation et câblage (ou pose sans fil)",
               "Configuration sur votre smartphone",
               "Prise en main et explications"]

packs = page_hero(
    "Packs",
    "Packs vidéosurveillance <em>4 et 8 caméras</em>",
    "Deux packs complets pour équiper rapidement vos locaux : caméras, enregistreur, installation et configuration incluses. Tarif sur devis après visite gratuite.") + f"""
  <section>
    <div class="wrap">
      <div class="grid-2" style="max-width:900px;margin:0 auto">
        <div class="card pack reveal" id="pack-4">
          <div class="eyebrow">Pack 4</div>
          <div class="pack-top"><span class="big">4</span><span class="unit">caméras + enregistreur</span></div>
          <p>Idéal pour un commerce, un restaurant, un cabinet ou un petit bureau.</p>
          <div class="grow">{checks(PACK_COMMON)}</div>
          <div class="price">Tarif sur devis — visite gratuite</div>
          <a href="contact.html?besoin=pack-4" class="btn btn-dark">Demander un devis Pack 4 {ic('arrow')}</a>
        </div>
        <div class="card pack featured reveal" id="pack-8">
          <span class="tag">Grands locaux</span>
          <div class="eyebrow">Pack 8</div>
          <div class="pack-top"><span class="big">8</span><span class="unit">caméras + enregistreur</span></div>
          <p>Pour les grands commerces, entrepôts, ateliers et sites avec extérieurs.</p>
          <div class="grow">{checks(PACK_COMMON)}</div>
          <div class="price">Tarif sur devis — visite gratuite</div>
          <a href="contact.html?besoin=pack-8" class="btn btn-primary">Demander un devis Pack 8 {ic('arrow')}</a>
        </div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <div class="section-head center reveal">
        <div class="eyebrow">Sur mesure</div>
        <h2>Besoin d'autre chose ?</h2>
        <p>Les packs sont une base : nous adaptons le nombre de caméras et les options à vos locaux.</p>
      </div>
      <div class="grid-3">
        <a href="alarme.html" class="card mini reveal"><div class="icon">{ic('alarm')}</div><h3>Ajouter une alarme</h3><p>Combinez caméras et alarme Ajax pour une protection complète.</p><span class="more">En savoir plus {ic('arrow')}</span></a>
        <a href="contact.html" class="card mini reveal"><div class="icon">{ic('cam')}</div><h3>Plus de caméras</h3><p>Au-delà de 8 caméras, nous réalisons une étude sur mesure.</p><span class="more">Nous contacter {ic('arrow')}</span></a>
        <a href="videosurveillance.html" class="card mini reveal"><div class="icon">{ic('tool')}</div><h3>Maintenance</h3><p>Faites suivre votre installation dans la durée.</p><span class="more">En savoir plus {ic('arrow')}</span></a>
      </div>
    </div>
  </section>
{cta_band("Quel pack pour vos locaux ?", "Nous venons sur place gratuitement pour vous conseiller le pack adapté et vous remettre un devis.")}
"""

# =============================================================================
# CONTACT
# =============================================================================
contact = page_hero(
    "Contact",
    "Demandez votre <em>devis gratuit</em>",
    "Décrivez votre projet : nous vous recontactons rapidement pour convenir d'une visite gratuite sur place, partout dans les Alpes-Maritimes.") + f"""
  <section>
    <div class="wrap contact-grid">
      <div class="contact-info reveal">
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

      <form id="devis" class="quote reveal" data-to="{EMAIL}" novalidate>
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
            <option value="info">Informatique &amp; réseau</option>
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
      SIRET : {SIRET}<br>
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
      <p>Le site utilise la police Inter, chargée depuis Google Fonts.</p>
    </div>
  </section>
"""

# =============================================================================
# 404
# =============================================================================
notfound = f"""
  <section class="hero">
    <div class="wrap hero-inner">
      <div class="badge"><i></i> Erreur 404</div>
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
    ("index.html", "BelaConnect — Vidéosurveillance et alarme pour professionnels · Alpes-Maritimes",
     "Installation de vidéosurveillance, d'alarmes et d'informatique pour les professionnels des Alpes-Maritimes (Nice, Cannes, Antibes…). Dahua, Hikvision, Ajax. Devis gratuit sur place.",
     home, faq_jsonld(HOME_FAQ)),
    ("videosurveillance.html", "Installation vidéosurveillance professionnelle · Alpes-Maritimes — BelaConnect",
     "Caméras Dahua et Hikvision intérieures et extérieures, filaires ou sans fil, avec enregistreur et accès smartphone. Installation et maintenance dans les Alpes-Maritimes.",
     video, faq_jsonld(VIDEO_FAQ)),
    ("alarme.html", "Alarme Ajax pour professionnels · Alpes-Maritimes — BelaConnect",
     "Installation d'alarmes anti-intrusion Ajax sans fil ou filaires pour commerces, bureaux et entrepôts dans les Alpes-Maritimes. Alertes sur smartphone. Devis gratuit.",
     alarm, faq_jsonld(ALARM_FAQ)),
    ("informatique.html", "Informatique d'entreprise & réseau · Alpes-Maritimes — BelaConnect",
     "Réseau, câblage, Wi-Fi professionnel TP-Link, postes, serveurs, sauvegardes, sécurité et dépannage informatique pour les entreprises des Alpes-Maritimes.",
     it, faq_jsonld(IT_FAQ)),
    ("packs.html", "Packs vidéosurveillance 4 et 8 caméras — BelaConnect",
     "Packs vidéosurveillance 4 caméras + enregistreur et 8 caméras + enregistreur, installation et configuration incluses. Alpes-Maritimes, devis gratuit.",
     packs, ""),
    ("contact.html", "Contact et devis gratuit — BelaConnect",
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
        (ROOT / filename).write_text(layout(filename, title, desc, body, extra), encoding="utf-8")
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for filename, *_ in PAGES:
        if filename in ("404.html", "mentions-legales.html"):
            continue
        loc = SITE_URL + "/" + ("" if filename == "index.html" else filename)
        sitemap.append(f"  <url><loc>{loc}</loc></url>")
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nDisallow: /carnet/\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print("Pages générées :", ", ".join(p[0] for p in PAGES))


if __name__ == "__main__":
    main()
