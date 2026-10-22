// BelaConnect — scripts communs
(function () {
  // Menu mobile
  var burger = document.querySelector('.burger');
  var menu = document.getElementById('menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
    });
  }

  // Ombre de l'en-tête au défilement
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Adresses propres : belaconnect.fr/ et belaconnect.fr/alarme au lieu de /index.html et /alarme.html
  if (/\.html$/.test(location.pathname) && location.protocol !== 'file:' && history.replaceState) {
    history.replaceState(null, '', location.pathname.replace(/index\.html$/, '').replace(/\.html$/, '') + location.search + location.hash);
  }

  // Année du pied de page
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // Notifications Telegram (via le relais Cloudflare) : demandes de devis et clics Appeler / WhatsApp
  var relay = document.body.getAttribute('data-tg');
  window.bcNotify = function (payload) {
    if (!relay || !window.fetch) return;
    try {
      fetch(relay, { method: 'POST', keepalive: true, headers: { 'Content-Type': 'text/plain' }, body: JSON.stringify(payload) })
        .catch(function () {});
    } catch (e) {}
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="tel:"], a[href*="wa.me/"]');
    if (a) window.bcNotify({ type: 'clic', what: a.href.indexOf('wa.me') >= 0 ? 'whatsapp' : 'appel', page: location.pathname });
  });

  // Cookies Google Ads : la balise n'est chargée qu'après accord du visiteur (choix gardé 6 mois)
  var consent = document.getElementById('consent');
  if (consent) {
    var KEY = 'bc-consent', SIX_MONTHS = 182 * 24 * 3600 * 1000;
    var read = function () {
      try { var c = JSON.parse(localStorage.getItem(KEY)); return c && Date.now() - c.t < SIX_MONTHS ? c.v : null; }
      catch (e) { return null; }
    };
    var loadAds = function () {
      if (window.gtag) return;
      var id = consent.getAttribute('data-ads');
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { dataLayer.push(arguments); };
      gtag('consent', 'default', { ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted', analytics_storage: 'denied' });
      gtag('js', new Date());
      gtag('config', id);
      var sc = document.createElement('script');
      sc.async = true;
      sc.src = 'https://www.googletagmanager.com/gtag/js?id=' + id;
      document.head.appendChild(sc);
    };
    var choice = read();
    if (choice === 'yes') loadAds();
    else if (choice === null) consent.hidden = false;
    consent.addEventListener('click', function (e) {
      var b = e.target.closest('[data-consent]');
      if (!b) return;
      var v = b.getAttribute('data-consent');
      try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (err) {}
      consent.hidden = true;
      if (v === 'yes') loadAds();
      else if (window.gtag) gtag('consent', 'update', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });
    });
    // Conversions Google Ads (envoyées seulement si la balise est chargée, donc après accord)
    window.bcConversion = function (kind) {
      var label = consent.getAttribute('data-conv-' + kind);
      if (label && window.gtag) gtag('event', 'conversion', { send_to: consent.getAttribute('data-ads') + '/' + label });
    };
    document.addEventListener('click', function (e) {
      if (e.target.closest('a[href^="tel:"], a[href*="wa.me/"]')) window.bcConversion('appel');
    });
    document.querySelectorAll('[data-cookies]').forEach(function (b) {
      b.addEventListener('click', function () { consent.hidden = false; });
    });
  }

  // Animations (désactivées si l'utilisateur préfère réduire les mouvements)
  var motionOk = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  if (motionOk && 'IntersectionObserver' in window) {
    document.documentElement.classList.add('anim');

    // Apparition progressive des blocs au défilement, avec un léger décalage entre voisins
    var targets = '.section-head, .split > *, .grid-2 > *, .grid-3 > *, .grid-4 > *, .compare > *, ' +
      '.plain-list li, .faq details, .cta-band, .note, .brands img, .brands strong, .contact-info .ci, form.quote, .aside-note';
    var items = document.querySelectorAll(targets);
    items.forEach(function (el) {
      if (el.closest('.hero')) return;
      var i = Array.prototype.indexOf.call(el.parentNode.children, el);
      el.classList.add('reveal');
      el.style.transitionDelay = (i % 6) * 90 + 'ms';
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
        // Une fois apparu, on retire le délai pour que les effets au survol restent instantanés
        setTimeout(function () { e.target.style.transitionDelay = ''; }, 1200);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

    // Compteurs de la bande « Pourquoi choisir BelaConnect »
    var counters = document.querySelectorAll('.why-grid b');
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        co.unobserve(e.target);
        var el = e.target, text = el.textContent, m = text.match(/^(\d+)(.*)$/);
        if (!m) return;
        var end = parseInt(m[1], 10), pad = m[1].length, rest = m[2], t0 = null, dur = 1200;
        var step = function (t) {
          if (!t0) t0 = t;
          var k = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - k, 3)));
          el.textContent = String(v).padStart(pad, '0') + rest;
          if (k < 1) requestAnimationFrame(step);
        };
        el.textContent = '0'.padStart(pad, '0') + rest;
        requestAnimationFrame(step);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { co.observe(el); });
  }

  // ===== Formulaire de devis en 3 étapes =====
  var form = document.getElementById('devis');
  if (!form) return;
  var panels = form.querySelectorAll('.step-panel');
  var marks = form.querySelectorAll('.progress li');
  var current = 1;
  var val = function (name) {
    var f = form.querySelectorAll('[name="' + name + '"]:checked');
    return Array.prototype.map.call(f, function (x) { return x.value; }).join(', ');
  };
  var label = function (name) {
    var f = form.querySelectorAll('[name="' + name + '"]:checked');
    return Array.prototype.map.call(f, function (x) { return x.parentNode.textContent.trim(); }).join(', ');
  };
  var CAT = { 'video': 'video', 'video-alarme': 'video', 'alarme': 'alarme', 'copro': 'copro', 'baie': 'baie',
              'info': 'info', 'maintenance': 'maint', 'autre': 'autre' };
  var LEGEND = { video: 'Parlez-nous de vos locaux', alarme: 'Parlez-nous de vos locaux', copro: 'Parlez-nous de la résidence',
                 baie: 'Parlez-nous de votre baie', info: 'Parlez-nous de votre informatique', maint: 'Que faut-il réparer ou entretenir ?',
                 autre: 'Parlez-nous de votre projet' };
  var cats = function () {
    var c = {};
    form.querySelectorAll('[name="besoin"]:checked').forEach(function (r) { c[CAT[r.value] || 'autre'] = 1; });
    if (form.querySelector('[name="besoin"][value="video-alarme"]:checked')) c.alarme = 1;
    return Object.keys(c);
  };
  var groupVisible = function (g) {
    var want = g.getAttribute('data-for').split(' '), have = cats();
    return have.some(function (c) { return want.indexOf(c) >= 0; });
  };
  var show = function (n) {
    current = n;
    form.classList.add('js-steps');
    panels.forEach(function (p) { p.classList.toggle('active', +p.getAttribute('data-step') === n); });
    marks.forEach(function (m, k) { m.classList.toggle('on', k < n); });
    form.querySelectorAll('.q-group').forEach(function (g) { g.hidden = !groupVisible(g); });
    var lg = form.querySelector('[data-step="2"] legend'), c0 = cats()[0];
    if (lg) lg.textContent = LEGEND[c0] || LEGEND.autre;
    if (n > 1) form.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };
  show(1);

  // Pré-sélection depuis l'URL (ex. /contact?besoin=copro)
  var pre = new URLSearchParams(window.location.search).get('besoin');
  if (pre) {
    var r = form.querySelector('[name="besoin"][value="' + pre + '"]');
    if (r) r.checked = true;
  }

  form.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b) return;
    if (b.classList.contains('next')) {
      if (current === 1 && !val('besoin')) {
        panels[0].querySelector('.step-error').classList.add('show');
        return;
      }
      panels[0].querySelector('.step-error').classList.remove('show');
      show(current + 1);
    }
    if (b.classList.contains('prev')) show(current - 1);
  });
  // Un choix à l'étape 1 fait passer directement à la suite
  form.querySelectorAll('[name="besoin"]').forEach(function (r) {
    r.addEventListener('change', function () { setTimeout(function () { show(2); }, 180); });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var err = document.getElementById('form-error');
    var required = ['nom', 'tel', 'ville'];
    for (var i = 0; i < required.length; i++) {
      var field = form[required[i]];
      if (!field.value.trim()) {
        err.classList.add('show');
        field.focus();
        return;
      }
    }
    err.classList.remove('show');
    var to = form.getAttribute('data-to');
    var key = form.getAttribute('data-key');
    var besoinTxt = label('besoin') || 'Non précisé';
    var entreprise = form.entreprise.value.trim();
    var subject = (cats().indexOf('maint') >= 0 ? 'Demande de dépannage — ' : 'Demande de devis — ') + besoinTxt + (entreprise ? ' — ' + entreprise : '') + ' — ' + form.ville.value.trim();
    var lines = ['BESOIN : ' + besoinTxt];
    form.querySelectorAll('.q-group').forEach(function (g) {
      if (!groupVisible(g)) return;
      lines.push(g.getAttribute('data-title') + ' : ' + (label(g.getAttribute('data-name')) || '—'));
    });
    lines.push('', 'CONTACT',
      'Entreprise : ' + (entreprise || '—'),
      'Nom : ' + form.nom.value.trim(),
      'Téléphone : ' + form.tel.value.trim(),
      'Email : ' + (form.email.value.trim() || '—'),
      'Ville : ' + form.ville.value.trim(),
      'Rappel : ' + form.rappel.value,
      '', 'PRÉCISIONS', form.message.value.trim() || '—');
    var body = lines.join('\n');
    window.bcNotify({ type: 'devis', subject: subject, message: body });
    var mailto = function () {
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    };
    if (!key) { mailto(); return; }

    // Envoi direct (Web3Forms)
    var ok = document.getElementById('form-ok');
    var btn = form.querySelector('button[type="submit"]');
    btn.disabled = true;
    var btnLabel = btn.innerHTML;
    btn.textContent = 'Envoi en cours…';
    fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({
        access_key: key,
        subject: subject,
        from_name: 'Site BELACONNECT',
        replyto: form.email.value.trim() || undefined,
        botcheck: form.botcheck.checked,
        message: body
      })
    }).then(function (r) {
      return r.json().catch(function () { throw new Error('réponse ' + r.status); });
    }).then(function (res) {
      if (!res.success) throw new Error(res.message || 'refusé');
      form.classList.add('sent');
      if (window.bcConversion) window.bcConversion('devis');
      ok.className = 'form-ok show';
      ok.innerHTML = '<b>Merci, votre demande a bien été envoyée.</b> Nous vous rappelons rapidement pour convenir d\'une visite gratuite.';
      form.reset();
    }).catch(function (e) {
      ok.className = 'form-ok form-fail show';
      ok.innerHTML = "L'envoi n'a pas abouti" + (e && e.message ? ' (' + e.message.replace(/[<>&]/g, '') + ')' : '') +
        '. Vous pouvez <a href="tel:' + (form.getAttribute('data-tel') || '') + '">nous appeler</a> ou ' +
        '<a href="#" id="form-mail">envoyer votre demande par email</a>.';
      var m = document.getElementById('form-mail');
      if (m) m.addEventListener('click', function (ev) { ev.preventDefault(); mailto(); });
      if (window.console) console.error('Web3Forms', e);
    }).then(function () {
      btn.disabled = false;
      btn.innerHTML = btnLabel;
    });
  });
})();
