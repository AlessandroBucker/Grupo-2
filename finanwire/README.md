# FinanceIA — Wireframes MVP
**"Precision Finance" Design System**
Propósito Partners · Grupo 2 · TIC 55 (Brisa/Fulbra)

---

## Como abrir no VS Code

1. Extraia o `.zip`
2. `File → Open Folder` → selecione a pasta `finanwire`
3. Instale a extensão **Live Server** (Ritwick Dey)
4. Clique com botão direito em `index.html` → **Open with Live Server**

---

## Estrutura

```
finanwire/
├── index.html                   ← Página inicial (Home)
├── css/
│   ├── global.css               ← Design tokens, botões, badges, tabelas
│   └── app-layout.css           ← Sidebar navy, topbar, shell
├── js/
│   ├── app.js                   ← Dropdowns, tabs, navegação
│   └── sidebar.js               ← Renderiza sidebar + topbar dinamicamente
└── telas/
    ├── tela-01-login.html       ← Login split-layout (RF01–RF04, RNF01, RF23)
    ├── tela-02-dashboard.html   ← Dashboard KPIs + charts (RF10, RF20–RF27)
    ├── tela-03-cadastro.html    ← Cadastro multi-step (RF06, RF07, RF11, RF23)
    ├── tela-04-listagem.html    ← Listagem 4 abas (RF05, RF08–RF10, RF18, RF30–RF31)
    └── tela-05-upload-ocr.html  ← Upload + OCR revisão (RF12–RF19)
```

## Design

- **Paleta**: Navy `#0F1C2E` · Cobalt `#1A56DB` · Emerald `#059669` · Coral `#DC2626`
- **Fontes**: IBM Plex Sans (UI) + IBM Plex Mono (valores numéricos)
- **Filosofia**: "Precision Finance" — Corporate Minimalism

## Equipe

| Nome | Função |
|---|---|
| Alessandro Werner Bucker | Frontend / Testes |
| Gabriel Rodrigo M. Duglokinski | Backend / BD |
| Marlon Pires Mendes | Backend / Requisitos |
| Samara Malta de Faria da Silva | Backend / PO / OCR |
| Tessália Pomocena Dos Santos | Frontend / UX/UI |

**Orientadora:** Caroline Pacheco da Rosa · **Período:** Fev–Jul 2026
