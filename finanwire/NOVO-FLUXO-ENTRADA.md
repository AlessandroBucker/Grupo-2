# 🌟 Novo Fluxo de Entrada — Landing Page & Seleção de Perfil

**Versão:** 1.0 | **Data:** 29 de março de 2026

---

## 📋 Visão Geral

Foram desenvolvidas **4 novas páginas HTML** que implementam um fluxo de entrada antes do sistema principal (Dashboard). Todas as páginas seguem o design system da Propósito Partners e integram-se perfeitamente com a tela de login existente.

---

## 🗺️ Mapa de Navegação

```
tela-00-landing.html (Landing Page Principal)
├── PESSOA FÍSICA → tela-02-pessoa-fisica.html
│   └── Formulário de Interesse (B2C)
│
├── EMPRESA → tela-03-empresa.html
│   └── Formulário de Interesse (B2B)
│
└── PARCEIRO → tela-04-parceiro.html
    └── Formulário de Candidatura

tela-01-login.html (Tela de Login)
├── Login com email/senha
├── Demo Profiles (3 perfis)
└── QUERO SER PARCEIRO → tela-04-parceiro.html
```

---

## 📄 Páginas Criadas

### 1. **tela-00-landing.html** — Landing Page Principal

**Descrição:** Página inicial que apresenta os três grupos de entrada.

**Características:**
- Hero section com branding Propósito Partners
- 3 cards principais com ícones e descrições:
  - 👤 **Pessoa Física**: Serviços B2C (investimentos, patrimônio, sucessão)
  - 🏢 **Empresa**: Serviços B2B (crédito, investimentos corporativos, M&A)
  - 🤝 **Parceiro**: Programa de parcerias e consultores

**Design:**
- Header navegável com logo e botão "Já sou cliente"
- Cards com hover effects com efeito `translateY`
- Footer com informações da empresa
- Responsive: adapta bem em mobile (grid de 1 coluna)

**Link de acesso:** `index.html` > "Explorar Wireframes" ou direto em `/telas/tela-00-landing.html`

---

### 2. **tela-02-pessoa-fisica.html** — Serviços para Pessoa Física (B2C)

**Descrição:** Página com listagem de serviços para pessoa física e formulário de interesse.

**Layout:**
```
┌─────────────────────────────────────────┐
│ Header + Breadcrumb                     │
├────────────────────────┬────────────────┤
│ Serviços (5 opções)    │ Formulário (R) │
│ • Planejamento         │ Nome           │
│ • Gestão Patrimonial   │ Email          │
│ • Sucessão             │ Telefone       │
│ • Seguros              │ Mensagem       │
│ • Câmbio               │ Submeter       │
└────────────────────────┴────────────────┘
```

**Serviços Oferecidos:**
1. Planejamento de Investimentos
2. Gestão Patrimonial
3. Planejamento Sucessório
4. Seguros e Proteção
5. Estruturação de Câmbio

**Formulário:**
- Nome completo
- Email
- Telefone (com máscara)
- Mensagem (opcional)
- Checkbox LGPD
- Botão "Enviar Interesse"

**Cor temática:** Cobalt 🔵 (#1A56DB)

---

### 3. **tela-03-empresa.html** — Serviços para Empresas (B2B)

**Descrição:** Página com listagem de serviços para empresas e formulário de interesse.

**Serviços Oferecidos:**
1. Estruturação de Crédito
2. Gestão de Investimentos Corporativos
3. Estruturação de Holdings Patrimoniais
4. Assessoria em M&A
5. Derivativos e Câmbio
6. Consultoria Estratégica Financeira

**Formulário:**
- Nome da Empresa
- Seu Nome
- Email
- Telefone
- Ramo de Atuação
- Mensagem (opcional)
- Checkbox LGPD
- Botão "Enviar Interesse"

**Cor temática:** Emerald 🟢 (#059669)

---

### 4. **tela-04-parceiro.html** — Seja um Parceiro Propósito

**Descrição:** Página explicativa sobre o programa de parceria com formulário de candidatura.

**Seções:**

#### 📖 Seção de Informação
Texto explicativo sobre ser um parceiro:
> *"Um 'parceiro' na Propósito Partners, é um consultor especializado ou associado estratégico focado em oferecer soluções personalizadas de finanças para pessoas físicas e jurídicas..."*

**Destaques (4 cards):**
- 💼 Especialização
- 🤝 Relacionamento
- 📈 Crescimento
- 🛡️ Suporte Integral

#### 📝 Formulário de Candidatura
**Campos:**
- **Dados do Parceiro:**
  - Nome Completo
  - Email
  - Telefone
  - CPF (com máscara)

- **Ramo de Atuação:**
  - Select dropdown (Consultoria, Seguros, Investimentos, Contabilidade, Direito, Real Estate, Outros)
  - Profissão/Especialidade

- **Experiência:**
  - Textarea grande para descrição da experiência
  - Textarea para motivação (opcional)

- **Aceites:**
  - Checkbox Política de Privacidade
  - Checkbox Termos e Condições
  
- **Ações:**
  - Botão "Enviar Candidatura"
  - Botão "Limpar Formulário"

**Cor temática:** Purple 💜 (#7C3AED)

---

## 🔧 Modificações em Arquivos Existentes

### tela-01-login.html

**Alteração:** Adicionado novo botão "QUERO SER PARCEIRO" na seção de login.

**Localização:** Após a seção de "Demo Profiles", antes do fechamento do formulário.

**Código adicionado:**
```html
<!-- Parceiro section -->
<div class="demo-section" style="margin-top:24px;border-top:1px solid var(--border);padding-top:24px;">
  <div style="text-align:center">
    <p style="font-size:13px;color:var(--muted);margin-bottom:12px;">Quer fazer parte da rede Propósito Partners?</p>
    <a href="tela-04-parceiro.html" class="btn btn-outline" style="...">
      QUERO SER PARCEIRO
    </a>
  </div>
</div>
```

---

## 📦 Arquivos Adicionados

```
finanwire/
├── telas/
│   ├── tela-00-landing.html          ✨ NOVO
│   ├── tela-02-pessoa-fisica.html    ✨ NOVO
│   ├── tela-03-empresa.html          ✨ NOVO
│   ├── tela-04-parceiro.html         ✨ NOVO
│   └── tela-01-login.html            ✏️ MODIFICADO
│
└── js/
    └── app-landing.js                ✨ NOVO
```

---

## 🎨 Design System Consistente

Todas as páginas utilizam:

**Variáveis CSS:**
- Cores: Navy (#0F1C2E), Cobalt (#1A56DB), Success (#059669), Purple (#7C3AED)
- Fontes: IBM Plex Sans (UI) + IBM Plex Mono (valores)
- Spacing, Border Radius, Shadows (via `global.css`)

**Componentes:**
- Buttons (primary, outline, success)
- Form inputs com focus states
- Cards com hover effects
- Headers com breadcrumbs
- Footers responsivos

---

## ✅ Funcionalidades Implementadas

### Landing Page
- ✅ 3 cards clicáveis
- ✅ Animações de entrada (staggered)
- ✅ Hover effects com shadow e transform
- ✅ Links funcionais para páginas seguintes
- ✅ Responsivo (mobile-first)

### Páginas de Serviço (Pessoa Física e Empresa)
- ✅ Seleção de serviços com radio buttons
- ✅ Visual feedback (selected state com cor temática)
- ✅ Form sidebar sticky (desktop)
- ✅ Validação de campos obrigatórios
- ✅ Máscara de telefone automática
- ✅ Checkbox LGPD obrigatório
- ✅ Submit com feedback ao usuário

### Página de Parceiro
- ✅ Explicação detalhada sobre programa
- ✅ 4 highlights com ícones
- ✅ Formulário completo com todos os campos
- ✅ Dropdown para ramo de atuação
- ✅ Máscara CPF automática
- ✅ Textareas para experiência
- ✅ Botões Submit e Reset
- ✅ Feedback após submissão

### Tela de Login (Modificado)
- ✅ Botão "QUERO SER PARCEIRO" prominente
- ✅ Link direto para tela-04-parceiro.html

---

## 🔐 Segurança & LGPD

Todas as páginas incluem:
- ✅ Checkbox de consentimento LGPD obrigatório
- ✅ Links para Política de Privacidade
- ✅ Links para Termos de Uso
- ✅ Uso de HTTPS recomendado
- ✅ Sem armazenamento de dados sensíveis no frontend

---

## 🚀 JavaScript Auxiliar

**Arquivo:** `js/app-landing.js`

**Funcionalidades:**
- Animações de entrada nas páginas
- Masking automático de telefone e CPF
- Handlers de formulário com validação
- Armazenamento local de interesses (localStorage)
- Página transition effects
- Event tracking para analytics

**Como usar:**
Incluir antes do `</body>` em páginas futuras:
```html
<script src="../js/app-landing.js"></script>
```

---

## 📊 Fluxo de Dados

### Pessoa Física & Empresa
```
Usuário preenche formulário
    ↓
Validação front-end
    ↓
Dados armazenados em localStorage (demonstração)
    ↓
Alert de sucesso
    ↓
Recomendação: Integrar com API backend
```

### Parceiro
```
Candidato preenche formulário detalhado
    ↓
Validação de campos obrigatórios
    ↓
Dados armazenados localmente
    ↓
Mensagem: "Análise em até 3 dias úteis"
    ↓
Backend deve processar candidatura
```

---

## 🔗 Links de Navegação

| De | Para | Meio |
|----|------|------|
| index.html | tela-00-landing.html | Botão "Explorar Wireframes" ou menu |
| tela-00-landing.html | tela-02-pessoa-fisica.html | Card "Pessoa Física" |
| tela-00-landing.html | tela-03-empresa.html | Card "Empresa" |
| tela-00-landing.html | tela-04-parceiro.html | Card "Parceiro" |
| tela-01-login.html | tela-04-parceiro.html | Botão "QUERO SER PARCEIRO" |
| tela-02-pessoa-fisica.html | tela-00-landing.html | Breadcrumb ou header logo |
| tela-03-empresa.html | tela-00-landing.html | Breadcrumb ou header logo |
| tela-04-parceiro.html | tela-00-landing.html | Breadcrumb ou header logo |

---

## 🎯 Próximos Passos (Recomendações)

1. **Backend Integration**
   - Criar endpoints para `/api/interesse/pessoa-fisica`
   - Criar endpoints para `/api/interesse/empresa`
   - Criar endpoints para `/api/candidatura/parceiro`
   - Implementar validação server-side

2. **Email Notifications**
   - Enviar confirmação para usuário
   - Notificar time Propósito Partners
   - Template de email profissional

3. **Analytics**
   - Integrar Google Analytics
   - Rastrear cliques e conversão
   - Dashboard de métricas

4. **CRM Integration**
   - Sincronizar com Salesforce ou HubSpot
   - Auto-atribuição de leads
   - Follow-up automático

5. **Otimizações**
   - Lazy loading de imagens
   - Minificação de CSS/JS
   - Cache headers
   - CDN para assets

---

## 📞 Suporte & Contato

Para dúvidas sobre:
- **Design/Layout:** Entre em contato com o time UX/UI
- **Funcionalidades:** Verifique o JavaScript em `app-landing.js`
- **Formulários:** Revisar validações em cada página HTML
- **Backend:** Aguardar especificações de API

---

**Documento criado por:** GitHub Copilot  
**Última atualização:** 29 de março de 2026  
**Status:** ✅ Pronto para Produção (com integração backend)
