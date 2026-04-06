/* =====================================================
   app.js — FinanceIA shared scripts
   ===================================================== */

// ── Sidebar mobile toggle ──────────────────────────────
(function() {
  const sidebar   = document.getElementById('sidebar');
  const overlay   = document.getElementById('sidebar-overlay');
  const menuBtn   = document.getElementById('mobile-menu-btn');
  const closeBtn  = document.getElementById('sidebar-close');

  function open()  { sidebar?.classList.add('open'); overlay?.classList.add('open'); }
  function close() { sidebar?.classList.remove('open'); overlay?.classList.remove('open'); }

  menuBtn?.addEventListener('click', open);
  closeBtn?.addEventListener('click', close);
  overlay?.addEventListener('click', close);
})();

// ── Dropdowns ─────────────────────────────────────────
document.addEventListener('click', function(e) {
  const btn = e.target.closest('[data-dropdown]');
  if (btn) {
    e.stopPropagation();
    const id   = btn.dataset.dropdown;
    const menu = document.getElementById(id);
    const open = menu.classList.contains('open');
    // close all
    document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
    if (!open) menu.classList.add('open');
    return;
  }
  // close all on outside click
  document.querySelectorAll('.dropdown-menu.open').forEach(m => m.classList.remove('open'));
});

// ── Tabs ──────────────────────────────────────────────
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const group = this.dataset.group;
    const target = this.dataset.tab;

    document.querySelectorAll(`.tab-btn[data-group="${group}"]`).forEach(b => b.classList.remove('active'));
    document.querySelectorAll(`.tab-content[data-group="${group}"]`).forEach(c => c.classList.remove('active'));

    this.classList.add('active');
    document.getElementById(target)?.classList.add('active');
  });
});

// ── Active nav link ───────────────────────────────────
(function() {
  const path = window.location.pathname.replace(/\/[^/]*$/, m => m);
  document.querySelectorAll('.nav-item a').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (window.location.href.endsWith(href) || window.location.pathname === href)) {
      link.closest('.nav-item')?.classList.add('active');
    }
  });
})();

// ── Logout ────────────────────────────────────────────
document.querySelectorAll('.logout-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    window.location.href = '../tela-01-login.html';
  });
});
document.querySelectorAll('.logout-btn-root').forEach(btn => {
  btn.addEventListener('click', () => {
    window.location.href = 'telas/tela-01-login.html';
  });
});
