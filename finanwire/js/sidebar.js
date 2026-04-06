/* =====================================================
   sidebar.js — injects sidebar + topbar HTML
   Call: renderLayout({ page, title, breadcrumbs })
   ===================================================== */

const ICONS = {
  chart:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>`,
  building: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>`,
  upload:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 16 12 12 8 16"/><line x1="12" y1="12" x2="12" y2="21"/><path d="M20.39 18.39A5 5 0 0018 9h-1.26A8 8 0 103 16.3"/></svg>`,
  bar:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>`,
  users:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>`,
  settings: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z"/></svg>`,
  bell:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/></svg>`,
  logout:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>`,
  chevdown: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>`,
  menu:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>`,
};

const NAV = [
  { label: 'Dashboard',            icon: 'chart',    href: 'tela-02-dashboard.html' },
  { label: 'Empresas / Clientes',  icon: 'building', href: 'tela-04-listagem.html'  },
  { label: 'Upload de Documentos', icon: 'upload',   href: 'tela-05-upload-ocr.html', badge: '3' },
  { label: 'Relatórios',           icon: 'bar',      href: 'tela-04-listagem.html'  },
  { label: 'Usuários',             icon: 'users',    href: 'tela-04-listagem.html'  },
  { label: 'Configurações',        icon: 'settings', href: 'tela-02-dashboard.html' },
];

function renderLayout({ page, title, breadcrumbs = [], user = { name:'Tessália Santos', role:'ANALISTA' } }) {
  const crumbsHTML = [
    { label:'Dashboard', href:'tela-02-dashboard.html' },
    ...breadcrumbs
  ].map((c, i, arr) => {
    if (i === arr.length - 1) return `<span class="current">${c.label}</span>`;
    return `<a href="${c.href}">${c.label}</a><span class="sep">/</span>`;
  }).join('');

  const navHTML = NAV.map(item => {
    const active = item.href === page ? 'active' : '';
    return `
    <li class="nav-item ${active}">
      <a href="${item.href}">
        <span class="nav-icon">${ICONS[item.icon]}</span>
        <span>${item.label}</span>
        ${item.badge ? `<span class="nav-badge">${item.badge}</span>` : ''}
      </a>
    </li>`;
  }).join('');

  const roleClass = { ADM:'badge-adm', ANALISTA:'badge-analyst', CONTADOR:'badge-accountant' }[user.role] || 'badge-analyst';
  const initial = user.name.charAt(0);
  const firstName = user.name.split(' ')[0];

  document.getElementById('app').innerHTML = `
    <div class="sidebar-overlay" id="sidebar-overlay"></div>
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-logo">
        <div class="logo-icon">${ICONS.chart}</div>
        <div>
          <div class="logo-name">FinanceIA</div>
          <div class="logo-partner">Propósito Partners</div>
        </div>
      </div>
      <nav>
        <ul class="sidebar-nav">
          <li><span class="section-label">Menu Principal</span></li>
          ${navHTML}
        </ul>
      </nav>
      <div class="sidebar-user">
        <div class="user-row logout-btn">
          <div class="user-avatar">${initial}</div>
          <div style="flex:1;min-width:0">
            <div class="user-name">${user.name}</div>
            <div class="user-role">${user.role}</div>
          </div>
          <span class="logout-icon">${ICONS.logout}</span>
        </div>
      </div>
    </aside>

    <div class="main-wrap">
      <header class="topbar">
        <button class="mobile-menu-btn" id="mobile-menu-btn">${ICONS.menu}</button>
        <nav class="breadcrumbs">${crumbsHTML}</nav>
        <div class="topbar-actions">
          <button class="bell-btn">
            ${ICONS.bell}
            <span class="bell-dot"></span>
          </button>
          <div class="topbar-user">
            <div class="user-avatar" style="width:28px;height:28px;font-size:12px">${initial}</div>
            <span class="topbar-user-name hide-md">${firstName}</span>
            <span class="badge ${roleClass} hide-md">${user.role}</span>
            <span class="topbar-chevron">${ICONS.chevdown}</span>
          </div>
        </div>
      </header>

      <main class="page-content" id="page-content">
        <h1 class="page-title">${title}</h1>
        <div id="page-body"></div>
      </main>
    </div>
  `;

  // re-run scripts after inject
  const script = document.createElement('script');
  script.src = '../js/app.js';
  document.body.appendChild(script);
}
