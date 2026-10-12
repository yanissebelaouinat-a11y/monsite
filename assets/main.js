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
    window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  });
})();
