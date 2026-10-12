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

  // Apparition au défilement
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
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
