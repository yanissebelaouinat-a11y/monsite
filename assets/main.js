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

  // Pré-sélection du besoin depuis l'URL (ex. contact.html?besoin=pack-4)
  var form = document.getElementById('devis');
  if (!form) return;
  var besoin = new URLSearchParams(window.location.search).get('besoin');
  if (besoin && form.besoin) {
    var opt = form.besoin.querySelector('option[value="' + besoin + '"]');
    if (opt) form.besoin.value = besoin;
  }

  // Formulaire : ouvre l'email pré-rempli
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
    var besoinTxt = form.besoin.options[form.besoin.selectedIndex].text;
    var entreprise = form.entreprise.value.trim();
    var subject = 'Demande de devis — ' + besoinTxt + (entreprise ? ' — ' + entreprise : '');
    var body = [
      'Entreprise : ' + (entreprise || '—'),
      'Nom : ' + form.nom.value.trim(),
      'Téléphone : ' + form.tel.value.trim(),
      'Email : ' + (form.email.value.trim() || '—'),
      'Ville : ' + form.ville.value.trim(),
      'Besoin : ' + besoinTxt,
      '',
      form.message.value.trim()
    ].join('\n');
    var mailto = function () {
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    };
    if (!key) { mailto(); return; }

    // Envoi direct (Web3Forms) ; en cas d'échec, on retombe sur l'email
    var ok = document.getElementById('form-ok');
    var btn = form.querySelector('button[type="submit"]');
    btn.disabled = true;
    var label = btn.innerHTML;
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
    }).then(function (r) { return r.json(); }).then(function (res) {
      if (!res.success) throw new Error(res.message);
      form.reset();
      ok.textContent = 'Merci, votre demande a bien été envoyée. Nous vous rappelons rapidement.';
      ok.classList.add('show');
    }).catch(function () {
      mailto();
    }).then(function () {
      btn.disabled = false;
      btn.innerHTML = label;
    });
  });
})();
