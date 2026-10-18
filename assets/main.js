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

  // Année du pied de page
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

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
  var camNeeded = function () { return /video|pack|copro/.test(val('besoin')); };
  var show = function (n) {
    current = n;
    form.classList.add('js-steps');
    panels.forEach(function (p) { p.classList.toggle('active', +p.getAttribute('data-step') === n); });
    marks.forEach(function (m, k) { m.classList.toggle('on', k < n); });
    form.querySelector('.only-cam').hidden = !camNeeded();
    var copro = /copro/.test(val('besoin'));
    form.querySelector('.only-copro').hidden = !copro;
    form.querySelector('.not-copro').hidden = copro;
    form.querySelector('.not-copro-2').hidden = copro;
    var lg = form.querySelector('[data-step="2"] legend');
    if (lg) lg.textContent = copro ? 'Parlez-nous de la résidence' : 'Parlez-nous de vos locaux';
    if (n > 1) form.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };
  show(1);

  // Pré-sélection depuis l'URL (ex. contact.html?besoin=pack-4)
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
    var subject = 'Demande de devis — ' + besoinTxt + (entreprise ? ' — ' + entreprise : '') + ' — ' + form.ville.value.trim();
    var lines = [
      'BESOIN : ' + besoinTxt,
    ];
    if (/copro/.test(val('besoin'))) {
      lines.push('Profil : ' + (label('profil') || '—'));
      lines.push('Zones à surveiller : ' + (label('zones') || '—'));
      lines.push('Taille : ' + (label('lots') || '—'));
      lines.push('Avancement : ' + (label('ag') || '—'));
    } else {
      lines.push('Locaux : ' + (label('locaux') || '—'));
    }
    if (camNeeded()) {
      lines.push('Caméras : ' + (label('cameras') || '—'));
      if (!/copro/.test(val('besoin'))) lines.push('Emplacement : ' + (label('emplacement') || '—'));
    }
    lines.push('Installation existante : ' + (label('existant') || '—'));
    lines.push('Délai : ' + (label('delai') || '—'));
    lines.push('', 'CONTACT',
      'Entreprise : ' + (entreprise || '—'),
      'Nom : ' + form.nom.value.trim(),
      'Téléphone : ' + form.tel.value.trim(),
      'Email : ' + (form.email.value.trim() || '—'),
      'Ville : ' + form.ville.value.trim(),
      'Rappel : ' + form.rappel.value,
      '', 'PRÉCISIONS', form.message.value.trim() || '—');
    var body = lines.join('\n');
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
