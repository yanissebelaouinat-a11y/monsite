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
  // Provenance du visiteur (mémorisée à son arrivée sur le site, pour la session)
  var source = (function () {
    try {
      var known = sessionStorage.getItem('bc-src');
      if (known) return known;
      var q = location.search, ref = document.referrer, src;
      if (/[?&](gclid|gbraid|wbraid)=/.test(q)) src = 'Annonce Google Ads';
      else if (/[?&]utm_source=([^&]+)/.test(q)) src = 'Campagne ' + decodeURIComponent(RegExp.$1);
      else if (/google\./.test(ref)) src = 'Recherche Google';
      else if (/bing\.|duckduckgo\.|qwant\.|yahoo\./.test(ref)) src = 'Moteur de recherche';
      else if (/chatgpt|openai|perplexity|claude\.ai|gemini|copilot/.test(ref)) src = 'Assistant IA';
      else if (/facebook|instagram|linkedin|whatsapp|t\.co\//.test(ref)) src = 'Réseaux sociaux';
      else if (ref && ref.indexOf(location.host) < 0) src = 'Lien depuis ' + ref.split('/')[2];
      else src = 'Accès direct';
      sessionStorage.setItem('bc-src', src);
      return src;
    } catch (e) { return ''; }
  })();
  var when = function () {
    var d = new Date(), z = function (n) { return (n < 10 ? '0' : '') + n; };
    return z(d.getDate()) + '/' + z(d.getMonth() + 1) + ' à ' + z(d.getHours()) + 'h' + z(d.getMinutes());
  };
  var pageName = function () {
    var c = document.querySelector('.crumbs');
    if (c) return c.textContent.split('/').pop().trim();
    return location.pathname === '/' ? 'Accueil' : (document.title.split(' | ')[0] || location.pathname).trim();
  };
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
    if (!a) return;
    var wa = a.href.indexOf('wa.me') >= 0;
    var title = wa ? '💬 CLIC SUR WHATSAPP' : '📞 CLIC SUR APPELER';
    var text = '📄 Page : ' + pageName() + '\n🔗 ' + location.pathname + (source ? '\n🎯 Provenance : ' + source : '') + '\n🕒 ' + when();
    window.bcNotify({ type: 'clic', what: wa ? 'whatsapp' : 'appel', page: location.pathname, v: 2, title: title, text: text });
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

    // Ondes du haut de page : léger effet de profondeur qui suit la souris (ordinateur)
    var waves = document.querySelector('.hero-waves'), hero = waves && waves.closest('.hero');
    if (waves && window.matchMedia('(hover:hover)').matches) {
      var tx = 0, ty = 0, cx = 0, cy = 0, raf = 0;
      var loop = function () {
        cx += (tx - cx) * .08; cy += (ty - cy) * .08;
        waves.style.setProperty('--px', cx.toFixed(1) + 'px');
        waves.style.setProperty('--py', cy.toFixed(1) + 'px');
        raf = Math.abs(tx - cx) + Math.abs(ty - cy) > .2 ? requestAnimationFrame(loop) : 0;
      };
      hero.addEventListener('mousemove', function (e) {
        var r = hero.getBoundingClientRect();
        tx = ((e.clientX - r.left) / r.width - .5) * -28;
        ty = ((e.clientY - r.top) / r.height - .5) * -20;
        if (!raf) raf = requestAnimationFrame(loop);
      });
      hero.addEventListener('mouseleave', function () { tx = ty = 0; if (!raf) raf = requestAnimationFrame(loop); });
    }

    // Halo qui suit la souris sur les cartes
    document.querySelectorAll('a.card.main, a.art-card').forEach(function (c) {
      c.addEventListener('mousemove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        c.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });

    // Barre de progression de lecture (articles)
    var art = document.querySelector('.article');
    if (art) {
      var bar = document.createElement('div');
      bar.className = 'read-progress';
      document.body.appendChild(bar);
      var onRead = function () {
        var r = art.getBoundingClientRect(), total = r.height - innerHeight * .6;
        var k = Math.min(1, Math.max(0, -r.top / (total > 0 ? total : 1)));
        bar.style.transform = 'scaleX(' + k.toFixed(3) + ')';
      };
      window.addEventListener('scroll', onRead, { passive: true });
      onRead();
    }

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

  // Téléphone : uniquement des chiffres (et + au début), mis en forme « 06 12 34 56 78 » pendant la saisie
  var tel = form.tel, telErr = document.getElementById('tel-error');
  var telDigits = function (v) { return v.replace(/[^\d+]/g, '').replace(/(?!^)\+/g, ''); };
  var telValid = function (v) {
    var d = telDigits(v);
    return /^0[1-9]\d{8}$/.test(d) || /^\+33[1-9]\d{8}$/.test(d) || /^\+(?!33)\d{8,14}$/.test(d);
  };
  var telShow = function (bad) {
    tel.classList.toggle('invalid', bad);
    tel.setAttribute('aria-invalid', bad ? 'true' : 'false');
    if (telErr) telErr.classList.toggle('show', bad);
  };
  if (tel) {
    tel.addEventListener('input', function () {
      var d = telDigits(tel.value);
      if (d.charAt(0) === '0') d = d.slice(0, 10).replace(/(\d{2})(?=\d)/g, '$1 ');
      else if (d.indexOf('+33') === 0) d = ('+33 ' + d.slice(3, 12).replace(/^(\d)(?=\d)/, '$1 ').replace(/(\d{2})(?=\d)/g, '$1 ')).replace(/ (\d) /, ' $1 ');
      tel.value = d;
      if (tel.classList.contains('invalid') && telValid(d)) telShow(false);
    });
    tel.addEventListener('blur', function () { if (tel.value.trim()) telShow(!telValid(tel.value)); });
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (tel && !telValid(tel.value)) { telShow(true); tel.focus(); return; }
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
    var EMOJI = { video: '📹', alarme: '🚨', copro: '🏢', baie: '🗄️', info: '💻', maint: '🔧', autre: '💡' };
    var isMaint = cats().indexOf('maint') >= 0;
    var tgTitle = isMaint ? '🛠️ NOUVELLE DEMANDE DE DÉPANNAGE' : '🔔 NOUVELLE DEMANDE DE DEVIS';
    var tg = [cats().map(function (c) { return EMOJI[c] || '💡'; }).join('') + ' ' + besoinTxt, '',
      '👤 Nom : ' + form.nom.value.trim()];
    if (entreprise) tg.push('🏢 Entreprise : ' + entreprise);
    tg.push('📞 Tél : ' + form.tel.value.trim());
    if (form.email.value.trim()) tg.push('✉️ Email : ' + form.email.value.trim());
    tg.push('📍 Ville : ' + form.ville.value.trim(), '🕐 Rappel : ' + form.rappel.value);
    var det = [];
    form.querySelectorAll('.q-group').forEach(function (g) {
      if (!groupVisible(g)) return;
      var v = label(g.getAttribute('data-name'));
      if (v) det.push('▫️ ' + g.getAttribute('data-title') + ' : ' + v);
    });
    if (det.length) tg.push('', '📋 DÉTAILS', det.join('\n'));
    if (form.message.value.trim()) tg.push('', '💬 MESSAGE', form.message.value.trim());
    tg.push('', '🎯 Provenance : ' + (source || '—'), '🕒 ' + when());
    window.bcNotify({ type: 'devis', subject: tgTitle, message: tg.join('\n'), v: 2, title: tgTitle, text: tg.join('\n') });
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
