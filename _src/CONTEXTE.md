# CONTEXTE — site BELACONNECT

Résumé du projet pour reprendre le travail rapidement, avec ou sans Claude.
Mis à jour le 7 novembre 2026.

> Ce fichier est dans `_src/`, et non à la racine. Comme tous les dossiers qui commencent par `_`, GitHub Pages ne le publie pas : il reste privé au dépôt et n'apparaît pas sur belaconnect.fr.

---

## 1. Objectif

**BELACONNECT** est une micro-entreprise (SIREN 947 672 481) qui installe et entretient de la **vidéosurveillance**, des **alarmes** et des **réseaux / équipements informatiques** pour les professionnels.

- **Cible prioritaire** : les commerçants. Viennent ensuite les restaurants, les pharmacies, les cabinets médicaux, les bureaux, les copropriétés (syndics), les entrepôts et les chantiers.
- **Zone** : « le Sud », c'est-à-dire les Alpes-Maritimes et le Var, plus les Bouches-du-Rhône pour les gros chantiers.
- **But du site** : obtenir des **demandes de devis** et des **appels ou messages WhatsApp**.
- **Leviers** : référencement naturel (dont le blog), Google Ads, fiche Google Business, Apple Plans, prospection des syndics par e-mail.

Contact affiché : 06 59 76 27 85 (aussi sur WhatsApp), belaconnect06@gmail.com.

---

## 2. Règles éditoriales (à respecter partout)

- Écrire **« nous »**, jamais « je ». Vouvoyer le lecteur. Écrire **BELACONNECT** en majuscules dans les textes.
- **Aucune ville citée** et **plus de « 06 »** : écrire « le Sud », ou « les Alpes-Maritimes et le Var ». L'adresse de Nice ne figure que dans les mentions légales, parce que c'est obligatoire.
- **Aucun prix**, **aucune ancienneté**.
- **Aucune marque** (Dahua, Hikvision, Ajax, TP-Link…), **sauf dans les articles Conseils**.
- **Rien d'inventé** : ni témoignage, ni chantier fictif, ni garantie, ni assurance, ni délai précis (écrire « rapidement »).
- **Aucune actualité** et aucun événement dans le site ni dans les annonces.
- Sujets juridiques : rester prudent et ajouter une note `small-note` qui renvoie vers cnil.fr ou service-public.fr.
- Ne pas mettre le nom ni le prénom du dirigeant dans les e-mails de prospection : signer « L'équipe BELACONNECT ».

---

## 3. Stack

| Élément | Choix |
|---|---|
| Site | **HTML statique généré** par un script Python : `_src/build.py` |
| Hébergement | **GitHub Pages**, qui publie la branche `claude/beautiful-volta-qfuhcb`. Pousser sur cette branche revient à mettre en ligne. |
| Domaine | `belaconnect.fr` (DNS chez **Hostinger**, fichier `CNAME`) |
| Style | `assets/style.css`, une seule feuille, sans framework |
| Script | `assets/main.js`, en JavaScript pur : formulaire en étapes, validation du téléphone, cookies, notifications |
| Polices | **Inter** (texte) et **Space Grotesk** (titres), hébergées dans `assets/fonts/` (aucun appel à Google) |
| Formulaire | Envoi par Web3Forms (clé `FORM_KEY` dans `build.py`) + notification Telegram |
| Notifications | **Telegram** via un relais **Cloudflare Worker** (`_src/telegram-worker.js`) |
| Mesure | **Google Ads** (balise et conversion « Demande de devis ») + **Microsoft Clarity**, chargés seulement après « Accepter » dans le bandeau cookies |
| Automatisation | GitHub Action `.github/workflows/notif-article.yml` + tâche planifiée Claude « Blog BELACONNECT » |

---

## 4. Structure des fichiers

```
_src/                     ← sources (non publiées par GitHub Pages)
  build.py                ← générateur : textes des pages, en-tête, pied de page, sitemap, robots.txt, llms.txt
  conseils.py             ← ARTICLES : un dict par article (slug, title, short, seo, desc, summary, date, related, body)
  secteurs.py             ← SECTEURS : pages par type de client (restaurant, pharmacie, cabinet-medical, bureaux)
  telegram-worker.js      ← code du Worker Cloudflare (à coller dans Cloudflare, pas exécuté ici)
  CONTEXTE.md             ← ce fichier
assets/
  style.css, main.js      ← style et script
  fonts/                  ← Inter et Space Grotesk (woff2)
  logo/                   ← logos, icône, logo de la signature e-mail
  og-image.png, favicons  ← partage sur les réseaux, icônes
  marques/                ← anciens logos de marques (plus utilisés)
  print/qr-belaconnect.png
*.html                    ← pages GÉNÉRÉES : ne pas les modifier à la main
conseils/*.html           ← articles générés + conseils/index.html
sitemap.xml, robots.txt, llms.txt   ← générés
signature.html            ← signature Gmail (noindex), écrite à la main
packs.html                ← ancienne adresse, redirige vers /videosurveillance
.github/workflows/notif-article.yml ← notification Telegram à chaque nouvel article
```

**Pages** : accueil, `/videosurveillance`, `/alarme`, `/informatique`, `/copropriete`, `/maintenance`, `/restaurant`, `/pharmacie`, `/cabinet-medical`, `/bureaux`, `/reglementation`, `/a-propos`, `/contact`, `/mentions-legales`, `/conseils/` (avec 23 articles au 7 novembre 2026).

Les adresses n'ont **pas de `.html`**. C'est `clean_urls()` dans `build.py` qui s'en charge, à l'aide de la liste `CLEAN_PAGES`. **Toute nouvelle page doit être ajoutée à `CLEAN_PAGES`.**

---

## 5. Décisions prises

**Design**
- **Design actuel, « nuit et laser »**, mis en ligne le 6 novembre 2026 :
  - thème sombre partout ;
  - scène de nuit dessinée en SVG en fond de chaque haut de page : rue, vitrine éclairée, rideau baissé, caméra, rayons laser rouges (constante `WAVES` dans `build.py`) ;
  - accents **rouge laser `#FF2B3A`** : trait sous les titres, rayon entre les sections, bord des cartes principales ;
  - boutons **cyan `#2BC0DC`**, la couleur du logo ;
  - menu et barre mobile en verre dépoli léger.
- Maquette de référence sur un canevas Claude Design : https://claude.ai/artifact/NPkW9QMMNoQBTRtG98Pfbo (privé).
- Version « liquid glass » complète essayée puis **abandonnée**, parce qu'elle faisait trop « IA ». Le verre est réservé au menu, à la barre mobile et aux notifications de l'accueil.
- Méthode **unslop** appliquée (skill de Damir Sokolovsky, CC BY 4.0) : aucune animation en boucle ni rebond, pas de lueurs, titres en graisse 500 à 600, pas d'emoji, pas de majuscules espacées.
- Arrondis prononcés, boutons en pilule (choix de Yanisse).

**Contenu**
- Titre de l'accueil : **« Vos locaux sous les yeux, même rideau baissé »**.
- Bandeau des logos de marques retiré ; les marques ne sont citées que dans les articles.
- Pages par type de client ajoutées : restaurant, pharmacie, cabinet médical, bureaux.

**Technique**
- Polices hébergées sur le site, pour le RGPD (Barlow abandonnée au profit d'Inter et Space Grotesk).
- Cookies : bandeau générique, Google Ads et Clarity chargés uniquement après accord (stocké 6 mois dans `localStorage`, clé `bc-consent`).
- Téléphone du formulaire validé (format 0X + 8 chiffres, +33 ou international).
- Référencement : `robots.txt` ouvert aux robots des IA, `llms.txt`, données structurées (LocalBusiness avec 3 départements desservis, FAQPage, Article, BreadcrumbList).

**Google Ads**
- Campagne « vidéosurveillance » sur le **Réseau de recherche uniquement** : Display et partenaires décochés.
- Mots-clés en **expression exacte**, avec exclusions des marques et des recherches de particuliers.
- **Ne pas exclure** marseille, aix, toulon, var : ces zones sont desservies.
- Zone : Alpes-Maritimes + Var, option « Présence ». Bouches-du-Rhône volontairement non ciblées en Ads.

**Sécurité**
- Le jeton du robot Telegram n'est **jamais** dans le dépôt : il est uniquement dans les secrets du Worker Cloudflare (`TG_TOKEN`, `TG_CHAT`).

---

## 6. Ce qui est fait

- Site complet, en ligne, avec le nouveau design, des adresses sans `.html`, la version mobile (barre Appeler / WhatsApp / Devis) et le formulaire de devis en 3 étapes.
- Notifications Telegram pour chaque demande de devis, chaque clic Appeler / WhatsApp et chaque nouvel article.
- Blog : 23 articles, **un nouvel article publié automatiquement chaque jour à 7 h 59** (heure de Paris).
- Search Console validée, sitemap envoyé, indexation des pages clés demandée.
- Google Ads nettoyé : Display coupé, expression exacte, exclusions.
- Microsoft Clarity installé.
- Signature Gmail avec logo et lien WhatsApp (`/signature`).
- Prospection des syndics : premier envoi de 32 e-mails depuis belaconnect06@gmail.com.
- Fiche Apple Business : domaine validé par un enregistrement TXT dans Hostinger, description fournie.
- Fiche Google Business créée : catégories, description et lien WhatsApp fournis.

---

## 7. Ce qui reste à faire

**Priorité haute (pour décrocher des chantiers)**
- [ ] **Fiche Google Business** : vérifier la validation, ajouter 5 à 10 photos réelles, obtenir les premiers avis.
- [ ] **Google Ads** :
  - mettre en pause les derniers mots-clés en « Requête large » et ajouter les exclusions de marques ;
  - ajouter le Var à la zone ;
  - vérifier qu'il n'y a pas de date de fin ;
  - analyser l'export de la période du 29 octobre au 4 novembre, puis un export par semaine.
- [ ] **Apple Business** : terminer la 2e validation (avis de situation SIRENE).
- [ ] **Prospection** : relancer les 32 syndics, écrire à un 2e lot, appeler les syndics sans e-mail, faire du porte-à-porte chez les commerçants (flyer à préparer).

**Ensuite**
- [ ] Créer la conversion Google Ads « Clic appel / WhatsApp » et renseigner `ADS_CONV_APPEL` dans `build.py` (vide pour l'instant).
- [ ] Inscription dans les annuaires, toujours avec le même nom, téléphone et site : Bing Places, PagesJaunes, page Facebook, page LinkedIn, CCI ou Chambre des métiers.
- [ ] Bing Webmaster Tools (import depuis Search Console).
- [ ] Favicon dans les résultats Google : attendre que Google repasse (il a bien vu le logo).
- [ ] Surveiller Search Console 2 à 3 semaines après le changement de titre de l'accueil.
- [ ] Éventuellement d'autres pages par type de client : commerces, boulangeries, coiffeurs, hôtels, entrepôts.
- [ ] Ménage : le code `brands()`, `BRAND_FILES` et `BRAND_LOGO` dans `build.py`, et le dossier `assets/marques/` ne servent plus.
- [ ] La PR n°1 du dépôt existe mais ne doit pas être fusionnée : le site est publié depuis la branche `claude/beautiful-volta-qfuhcb`.

---

## 8. Commandes utiles

```bash
# Régénérer tout le site après une modification de _src/ ou des textes
python3 _src/build.py

# Prévisualiser en local (adresses sans .html non gérées : ajouter .html à la main)
python3 -m http.server 8000      # puis http://localhost:8000

# Publier (mise en ligne en 1 à 2 minutes)
git pull origin claude/beautiful-volta-qfuhcb
python3 _src/build.py
git add -A
git reset _src/__pycache__        # ne jamais commiter le cache Python
git commit -m "…"
git push origin claude/beautiful-volta-qfuhcb

# Compter les mots du dernier article
python3 -c "import re,sys;sys.path.insert(0,'_src');import conseils as c;print(len(re.sub('<[^>]+>',' ',c.ARTICLES[-1]['body']).split()))"

# Vérifier qu'un nouvel article est bien partout, sans lien .html
grep -c <slug> conseils/index.html sitemap.xml llms.txt
grep -c '<slug>\.html' conseils/index.html sitemap.xml llms.txt   # doit donner 0
```

**Ajouter un article** : ajouter un `dict(...)` à la fin de `ARTICLES` dans `_src/conseils.py` (600 à 1000 mots, 2 slugs existants dans `related`), puis lancer `build.py`, commiter et pousser. La notification Telegram part toute seule.

**Ajouter une page par type de client** : ajouter une entrée à `SECTEURS` dans `_src/secteurs.py`, ajouter le nom de la page à `CLEAN_PAGES` dans `build.py`, puis lancer `build.py`.

**Relancer la notification du dernier article** : GitHub > Actions > « Notification nouvel article » > Run workflow.

**Mettre à jour le relais Telegram** : copier `_src/telegram-worker.js` dans Cloudflare (Workers > belaconnect-telegram > Modifier le code > Déployer).
