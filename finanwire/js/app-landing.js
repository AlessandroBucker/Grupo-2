/**
 * app-landing.js
 * Gerencia a navegação e interações das páginas de entrada da Propósito Partners
 * Inclui: Landing page, Pessoa Física, Empresa, Parceiro
 */

// ============================================================================
// CONFIGURAÇÕES GLOBAIS
// ============================================================================

// Armazenar dados de interesse localmente (para fins de demonstração)
const storeInterest = (data) => {
  const interests = JSON.parse(localStorage.getItem('proposito_interests') || '[]');
  interests.push({
    ...data,
    timestamp: new Date().toISOString()
  });
  localStorage.setItem('proposito_interests', JSON.stringify(interests));
};

// Verificar se há dados armazenados (para analytics)
const getStoredInterests = () => {
  return JSON.parse(localStorage.getItem('proposito_interests') || '[]');
};

// ============================================================================
// ANIMAÇÕES DE ENTRADA
// ============================================================================

const setupEntryAnimations = () => {
  // Animar cards na landing page
  const entryCards = document.querySelectorAll('.entry-card');
  entryCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    
    setTimeout(() => {
      card.style.transition = 'all 0.5s ease-out';
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    }, index * 100);
  });
};

// ============================================================================
// GERENCIAMENTO DE FORMULÁRIOS
// ============================================================================

const setupFormHandlers = () => {
  // Pessoa Física
  const pessoaForm = document.getElementById('interesseForm');
  if (pessoaForm && pessoaForm.dataset.page === 'pessoa-fisica') {
    pessoaForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handlePessoaFisicaSubmit();
    });
  }

  // Empresa
  const empresaForm = document.getElementById('interesseForm');
  if (empresaForm && pessoaForm.dataset.page === 'empresa') {
    empresaForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handleEmpresaSubmit();
    });
  }

  // Parceiro
  const parceiroForm = document.getElementById('parceiroForm');
  if (parceiroForm) {
    parceiroForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handleParceiroSubmit();
    });
  }
};

const handlePessoaFisicaSubmit = () => {
  const form = document.getElementById('interesseForm');
  const formData = new FormData(form);
  const service = document.querySelector('input[name="service"]:checked')?.value || 'não especificado';

  const data = {
    tipo: 'pessoa_fisica',
    servico: service,
    nome: formData.get('nome'),
    email: formData.get('email'),
    telefone: formData.get('telefone'),
    mensagem: formData.get('mensagem')
  };

  // Armazenar interesse
  storeInterest(data);

  // Enviar para servidor (quando integrado)
  console.log('Interesse de Pessoa Física registrado:', data);

  // Feedback ao usuário
  showSuccessMessage(form);
  form.reset();
};

const handleEmpresaSubmit = () => {
  const form = document.getElementById('interesseForm');
  const formData = new FormData(form);
  const service = document.querySelector('input[name="service"]:checked')?.value || 'não especificado';

  const data = {
    tipo: 'empresa',
    servico: service,
    empresa: formData.get('empresa'),
    nome: formData.get('nome'),
    email: formData.get('email'),
    telefone: formData.get('telefone'),
    ramo: formData.get('ramo'),
    mensagem: formData.get('mensagem')
  };

  // Armazenar interesse
  storeInterest(data);

  // Enviar para servidor (quando integrado)
  console.log('Interesse de Empresa registrado:', data);

  // Feedback ao usuário
  showSuccessMessage(form);
  form.reset();
};

const handleParceiroSubmit = () => {
  const form = document.getElementById('parceiroForm');
  const formData = new FormData(form);

  const data = {
    tipo: 'parceiro',
    nome: formData.get('nome'),
    email: formData.get('email'),
    telefone: formData.get('telefone'),
    cpf: formData.get('cpf'),
    ramo: formData.get('ramo'),
    profissao: formData.get('profissao'),
    experiencia: formData.get('experiencia'),
    motivacao: formData.get('motivacao')
  };

  // Armazenar interesse
  storeInterest(data);

  // Enviar para servidor (quando integrado)
  console.log('Candidatura de Parceiro registrada:', data);

  // Feedback ao usuário
  showSuccessMessage(form);
  form.reset();
};

const showSuccessMessage = (form) => {
  const title = form.closest('.form-sidebar') ? 'Seu interesse foi registrado com sucesso!' : 'Sua candidatura foi recebida!';
  const message = form.closest('.form-sidebar') 
    ? 'Um especialista entrará em contato em até 24 horas.'
    : 'Analisaremos seus dados em até 3 dias úteis.';

  alert(`${title}\n\n${message}`);
};

// ============================================================================
// SELEÇÃO DE SERVIÇOS COM EFEITO VISUAL
// ============================================================================

const setupServiceSelection = () => {
  const serviceRadios = document.querySelectorAll('input[name="service"]');
  
  serviceRadios.forEach(radio => {
    radio.addEventListener('change', (e) => {
      // Remover selected de todos
      document.querySelectorAll('.service-item').forEach(item => {
        item.classList.remove('selected');
      });

      // Adicionar selected ao pai do radio selecionado
      e.target.closest('.service-item').classList.add('selected');

      // Animar
      const serviceItem = e.target.closest('.service-item');
      serviceItem.style.transition = 'all 0.2s ease-out';
      serviceItem.style.transform = 'scale(1.02)';
      setTimeout(() => {
        serviceItem.style.transform = 'scale(1)';
      }, 200);
    });
  });
};

// ============================================================================
// VALIDAÇÃO E MÁSCARA DE ENTRADA
// ============================================================================

const setupInputMasks = () => {
  // Máscara de telefone
  const phoneInputs = document.querySelectorAll('input[type="tel"]');
  phoneInputs.forEach(input => {
    input.addEventListener('input', (e) => {
      let value = e.target.value.replace(/\D/g, '');
      
      if (value.length > 0) {
        if (value.length <= 2) {
          value = `(${value}`;
        } else if (value.length <= 7) {
          value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
        } else {
          value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7, 11)}`;
        }
      }

      e.target.value = value;
    });
  });

  // Máscara de CPF
  const cpfInputs = document.querySelectorAll('input[name="cpf"]');
  cpfInputs.forEach(input => {
    input.addEventListener('input', (e) => {
      let value = e.target.value.replace(/\D/g, '');
      
      if (value.length > 0) {
        if (value.length <= 3) {
          value = value;
        } else if (value.length <= 6) {
          value = `${value.slice(0, 3)}.${value.slice(3)}`;
        } else if (value.length <= 9) {
          value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(6)}`;
        } else {
          value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(6, 9)}-${value.slice(9, 11)}`;
        }
      }

      e.target.value = value;
    });
  });
};

// ============================================================================
// TRANSIÇÃO ENTRE PÁGINAS SUAVE
// ============================================================================

const setupPageTransitions = () => {
  document.addEventListener('click', (e) => {
    const link = e.target.closest('a[href*=".html"]');
    
    if (link && !e.ctrlKey && !e.shiftKey && !e.metaKey) {
      // Opcional: adicionar efeito de fade out
      const href = link.getAttribute('href');
      
      // Se for um link interno do site, podemos adicionar fade
      if (href.includes('tela-')) {
        document.body.style.opacity = '1';
        document.body.style.transition = 'opacity 0.3s ease-out';
        document.body.style.opacity = '0';
      }
    }
  });
};

// ============================================================================
// INICIALIZAÇÃO
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
  // Executar todas as inicializações
  setupEntryAnimations();
  setupFormHandlers();
  setupServiceSelection();
  setupInputMasks();
  setupPageTransitions();

  // Log de debug (removar em produção)
  console.log('✅ App Landing inicializado com sucesso');
  console.log(`📊 Interesses armazenados: ${getStoredInterests().length}`);
});

// ============================================================================
// FUNÇÃO DE UTILIDADE PARA ANALYTICS (OPCIONAL)
// ============================================================================

const trackEvent = (eventName, eventData) => {
  console.log(`📈 Evento: ${eventName}`, eventData);
  
  // Aqui você pode enviar para Google Analytics, Mixpanel, etc.
  // gtag('event', eventName, eventData);
  // mixpanel.track(eventName, eventData);
};

// Registrar visualização de página
const pageType = document.body.dataset.page || 'desconhecida';
trackEvent('page_view', {
  page_type: pageType,
  timestamp: new Date().toISOString()
});
