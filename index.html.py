# Your first line of Python code
portfolio-agent/
├── index.html
├── style.css
├── script.js
├── agent-core.js
└── README.md
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agente de IA - Portfolio</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="logo">
                <i class="fas fa-robot"></i>
                <h1>Portfolio<span class="ai-text">AI</span></h1>
            </div>
            <div class="theme-toggle">
                <button id="themeToggle">
                    <i class="fas fa-moon"></i>
                </button>
            </div>
        </header>

        <main class="main-content">
            <section class="agent-section">
                <div class="agent-header">
                    <div class="agent-avatar">
                        <div class="avatar-circle">
                            <i class="fas fa-brain"></i>
                            <div class="pulse"></div>
                        </div>
                        <div class="agent-status">
                            <span class="status-dot"></span>
                            <span class="status-text">Online</span>
                        </div>
                    </div>
                    <div class="agent-info">
                        <h2>Assistente de Portfolio</h2>
                        <p class="agent-subtitle">Agente de IA que apresenta projetos e habilidades</p>
                        <div class="agent-tags">
                            <span class="tag">Machine Learning</span>
                            <span class="tag">Web Dev</span>
                            <span class="tag">NLP</span>
                            <span class="tag">React</span>
                        </div>
                    </div>
                </div>

                <div class="chat-container">
                    <div class="chat-header">
                        <h3><i class="fas fa-comments"></i> Diálogo Interativo</h3>
                        <button id="clearChat" class="btn-small">
                            <i class="fas fa-trash-alt"></i> Limpar
                        </button>
                    </div>
                    
                    <div class="chat-messages" id="chatMessages">
                        <div class="message agent-message">
                            <div class="message-avatar">
                                <i class="fas fa-robot"></i>
                            </div>
                            <div class="message-content">
                                <p>Olá! Sou seu Agente de IA para portfolio. Posso apresentar seus projetos, habilidades e experiência. Como posso ajudá-lo hoje?</p>
                                <div class="message-time">Agora</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="quick-actions">
                        <button class="quick-btn" data-query="Projetos">
                            <i class="fas fa-project-diagram"></i> Ver Projetos
                        </button>
                        <button class="quick-btn" data-query="Habilidades">
                            <i class="fas fa-code"></i> Minhas Habilidades
                        </button>
                        <button class="quick-btn" data-query="Experiência">
                            <i class="fas fa-briefcase"></i> Experiência
                        </button>
                        <button class="quick-btn" data-query="Contato">
                            <i class="fas fa-envelope"></i> Informações de Contato
                        </button>
                    </div>
                    
                    <div class="chat-input-container">
                        <input type="text" id="chatInput" placeholder="Pergunte sobre projetos, habilidades, experiência..." autocomplete="off">
                        <button id="sendMessage" class="send-btn">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </div>
                </div>
            </section>

            <section class="projects-section">
                <h3><i class="fas fa-star"></i> Projetos em Destaque</h3>
                <div class="projects-grid">
                    <div class="project-card">
                        <div class="project-icon">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <h4>Sistema de Recomendação</h4>
                        <p>Sistema de recomendação baseado em ML para e-commerce usando collaborative filtering.</p>
                        <div class="project-tech">
                            <span>Python</span>
                            <span>TensorFlow</span>
                            <span>Flask</span>
                        </div>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-icon">
                            <i class="fas fa-language"></i>
                        </div>
                        <h4>Analisador de Sentimentos</h4>
                        <p>Modelo de NLP para análise de sentimentos em português com 92% de precisão.</p>
                        <div class="project-tech">
                            <span>Python</span>
                            <span>BERT</span>
                            <span>FastAPI</span>
                        </div>
                    </div>
                    
                    <div class="project-card">
                        <div class="project-icon">
                            <i class="fas fa-mobile-alt"></i>
                        </div>
                        <h4>App de Tarefas com IA</h4>
                        <p>Aplicativo mobile com assistente de IA para gerenciamento inteligente de tarefas.</p>
                        <div class="project-tech">
                            <span>React Native</span>
                            <span>Node.js</span>
                            <span>OpenAI API</span>
                        </div>
                    </div>
                </div>
            </section>
        </main>

        <footer class="footer">
            <p>Agente de IA para Portfolio • Desenvolvido com HTML, CSS e JavaScript</p>
            <div class="footer-links">
                <a href="#"><i class="fab fa-github"></i> GitHub</a>
                <a href="#"><i class="fab fa-linkedin"></i> LinkedIn</a>
                <a href="#"><i class="fas fa-file-pdf"></i> Currículo</a>
            </div>
        </footer>
    </div>

    <script src="script.js"></script>
    <script src="agent-core.js"></script>
</body>
</html>
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --secondary: #10b981;
    --dark: #1f2937;
    --light: #f9fafb;
    --gray: #6b7280;
    --gray-light: #e5e7eb;
    --border-radius: 12px;
    --shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    --transition: all 0.3s ease;
}

[data-theme="dark"] {
    --primary: #818cf8;
    --primary-dark: #6366f1;
    --secondary: #34d399;
    --dark: #f9fafb;
    --light: #111827;
    --gray: #9ca3af;
    --gray-light: #374151;
    --shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.2);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: var(--light);
    color: var(--dark);
    line-height: 1.6;
    transition: var(--transition);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Header */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
    margin-bottom: 30px;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 1.5rem;
    font-weight: 700;
}

.logo i {
    color: var(--primary);
    font-size: 2rem;
}

.ai-text {
    color: var(--primary);
    font-weight: 800;
}

.theme-toggle button {
    background: var(--gray-light);
    border: none;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    color: var(--dark);
    transition: var(--transition);
}

.theme-toggle button:hover {
    background: var(--primary);
    color: white;
    transform: rotate(30deg);
}

/* Agent Section */
.agent-section {
    background: var(--light);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow);
    padding: 30px;
    margin-bottom: 40px;
    border: 1px solid var(--gray-light);
}

.agent-header {
    display: flex;
    align-items: center;
    gap: 25px;
    margin-bottom: 30px;
}

.agent-avatar {
    position: relative;
}

.avatar-circle {
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
    color: white;
    position: relative;
}

.pulse {
    position: absolute;
    width: 120px;
    height: 120px;
    border: 2px solid var(--primary);
    border-radius: 50%;
    top: -10px;
    left: -10px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(0.95); opacity: 0.8; }
    70% { transform: scale(1.05); opacity: 0.4; }
    100% { transform: scale(0.95); opacity: 0.8; }
}

.agent-status {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 10px;
    gap: 8px;
}

.status-dot {
    width: 10px;
    height: 10px;
    background-color: var(--secondary);
    border-radius: 50%;
    animation: blink 2s infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

.status-text {
    font-size: 0.9rem;
    color: var(--gray);
    font-weight: 500;
}

.agent-info h2 {
    font-size: 1.8rem;
    margin-bottom: 5px;
}

.agent-subtitle {
    color: var(--gray);
    margin-bottom: 15px;
}

.agent-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.tag {
    background-color: var(--gray-light);
    color: var(--dark);
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
}

/* Chat Container */
.chat-container {
    border: 1px solid var(--gray-light);
    border-radius: var(--border-radius);
    overflow: hidden;
}

.chat-header {
    background-color: var(--gray-light);
    padding: 15px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.chat-header h3 {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.2rem;
}

.btn-small {
    background-color: var(--primary);
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: var(--transition);
}

.btn-small:hover {
    background-color: var(--primary-dark);
    transform: translateY(-2px);
}

.chat-messages {
    height: 350px;
    overflow-y: auto;
    padding: 20px;
    background-color: var(--light);
}

.message {
    display: flex;
    margin-bottom: 20px;
    animation: fadeIn 0.5s;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.user-message {
    flex-direction: row-reverse;
}

.message-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: var(--primary);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 10px;
    flex-shrink: 0;
}

.user-message .message-avatar {
    background-color: var(--secondary);
}

.message-content {
    max-width: 70%;
    background-color: var(--gray-light);
    padding: 15px;
    border-radius: 18px;
    border-top-left-radius: 0;
    position: relative;
}

.user-message .message-content {
    background-color: var(--primary);
    color: white;
    border-top-left-radius: 18px;
    border-top-right-radius: 0;
}

.message-time {
    font-size: 0.75rem;
    color: var(--gray);
    margin-top: 8px;
    text-align: right;
}

.user-message .message-time {
    color: rgba(255, 255, 255, 0.8);
}

.quick-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 15px 20px;
    background-color: var(--gray-light);
    border-top: 1px solid var(--gray-light);
}

.quick-btn {
    background-color: var(--light);
    color: var(--dark);
    border: 1px solid var(--gray-light);
    padding: 10px 15px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: var(--transition);
}

.quick-btn:hover {
    background-color: var(--primary);
    color: white;
    border-color: var(--primary);
    transform: translateY(-3px);
}

.chat-input-container {
    display: flex;
    padding: 20px;
    background-color: var(--light);
    border-top: 1px solid var(--gray-light);
}

#chatInput {
    flex: 1;
    padding: 15px;
    border: 1px solid var(--gray-light);
    border-radius: 8px;
    font-size: 1rem;
    background-color: var(--light);
    color: var(--dark);
    transition: var(--transition);
}

#chatInput:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
}

.send-btn {
    background-color: var(--primary);
    color: white;
    border: none;
    width: 55px;
    margin-left: 10px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.2rem;
    transition: var(--transition);
}

.send-btn:hover {
    background-color: var(--primary-dark);
    transform: translateY(-2px);
}

/* Projects Section */
.projects-section {
    margin-bottom: 40px;
}

.projects-section h3 {
    font-size: 1.5rem;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 25px;
}

.project-card {
    background-color: var(--light);
    border-radius: var(--border-radius);
    padding: 25px;
    box-shadow: var(--shadow);
    border: 1px solid var(--gray-light);
    transition: var(--transition);
    position: relative;
    overflow: hidden;
}

.project-card:hover {
    transform: translateY(-10px);
    border-color: var(--primary);
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
}

.project-icon {
    font-size: 2rem;
    color: var(--primary);
    margin-bottom: 15px;
}

.project-card h4 {
    font-size: 1.3rem;
    margin-bottom: 10px;
}

.project-card p {
    color: var(--gray);
    margin-bottom: 20px;
    font-size: 0.95rem;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.project-tech span {
    background-color: var(--gray-light);
    color: var(--dark);
    padding: 5px 10px;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 500;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px 0;
    color: var(--gray);
    border-top: 1px solid var(--gray-light);
    margin-top: 40px;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 15px;
}

.footer-links a {
    color: var(--gray);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: var(--transition);
}

.footer-links a:hover {
    color: var(--primary);
}

/* Responsividade */
@media (max-width: 768px) {
    .agent-header {
        flex-direction: column;
        text-align: center;
        gap: 15px;
    }
    
    .agent-tags {
        justify-content: center;
    }
    
    .projects-grid {
        grid-template-columns: 1fr;
    }
    
    .message-content {
        max-width: 85%;
    }
    
    .quick-actions {
        justify-content: center;
    }
}
document.addEventListener('DOMContentLoaded', function() {
    // Elementos DOM
    const chatInput = document.getElementById('chatInput');
    const sendButton = document.getElementById('sendMessage');
    const chatMessages = document.getElementById('chatMessages');
    const clearButton = document.getElementById('clearChat');
    const themeToggle = document.getElementById('themeToggle');
    const quickButtons = document.querySelectorAll('.quick-btn');
    
    // Inicializar agente
    const agent = new PortfolioAgent();
    
    // Tema escuro/claro
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);
    
    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });
    
    function updateThemeIcon(theme) {
        const icon = themeToggle.querySelector('i');
        icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
    }
    
    // Enviar mensagem
    function sendMessage() {
        const messageText = chatInput.value.trim();
        
        if (messageText === '') return;
        
        // Adicionar mensagem do usuário
        addMessage(messageText, 'user');
        
        // Limpar input
        chatInput.value = '';
        
        // Simular processamento
        setTimeout(() => {
            const response = agent.getResponse(messageText);
            addMessage(response, 'agent');
        }, 500);
    }
    
    // Adicionar mensagem ao chat
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const avatarIcon = sender === 'user' ? 'fas fa-user' : 'fas fa-robot';
        
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="${avatarIcon}"></i>
            </div>
            <div class="message-content">
                <p>${text}</p>
                <div class="message-time">Agora</div>
            </div>
        `;
        
        chatMessages.appendChild(messageDiv);
        
        // Scroll para a última mensagem
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Event Listeners
    sendButton.addEventListener('click', sendMessage);
    
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    clearButton.addEventListener('click', () => {
        chatMessages.innerHTML = '';
        
        // Adicionar mensagem inicial do agente
        addMessage('Olá! Sou seu Agente de IA para portfolio. Posso apresentar seus projetos, habilidades e experiência. Como posso ajudá-lo hoje?', 'agent');
    });
    
    // Botões rápidos
    quickButtons.forEach(button => {
        button.addEventListener('click', () => {
            const query = button.getAttribute('data-query');
            chatInput.value = query;
            sendMessage();
        });
    });
    
    // Efeito de digitação para a primeira mensagem
    const initialMessage = document.querySelector('.agent-message .message-content p');
    const originalText = initialMessage.textContent;
    initialMessage.textContent = '';
    
    let i = 0;
    function typeWriter() {
        if (i < originalText.length) {
            initialMessage.textContent += originalText.charAt(i);
            i++;
            setTimeout(typeWriter, 30);
        }
    }
    
    setTimeout(typeWriter, 1000);
});
class PortfolioAgent {
    constructor() {
        this.responses = {
            "projetos": {
                title: "Meus Principais Projetos",
                content: "Tenho desenvolvido diversos projetos nas áreas de Machine Learning, Desenvolvimento Web e Aplicativos Mobile:<br><br>" +
                         "<strong>1. Sistema de Recomendação</strong><br>" +
                         "Sistema baseado em Machine Learning para recomendações personalizadas em e-commerce, implementado com Python, TensorFlow e Flask.<br><br>" +
                         "<strong>2. Analisador de Sentimentos</strong><br>" +
                         "Modelo de NLP para análise de sentimentos em português com 92% de precisão, utilizando BERT e FastAPI.<br><br>" +
                         "<strong>3. App de Tarefas com IA</strong><br>" +
                         "Aplicativo mobile com assistente de IA para gerenciamento inteligente de tarefas, desenvolvido com React Native e Node.js."
            },
            "habilidades": {
                title: "Minhas Habilidades Técnicas",
                content: "<strong>Linguagens de Programação:</strong> Python, JavaScript, Java, SQL<br>" +
                         "<strong>Machine Learning:</strong> TensorFlow, PyTorch, Scikit-learn, NLP, Visão Computacional<br>" +
                         "<strong>Desenvolvimento Web:</strong> React, Node.js, HTML/CSS, TypeScript, REST APIs<br>" +
                         "<strong>Ferramentas & DevOps:</strong> Git, Docker, AWS, CI/CD, Linux<br>" +
                         "<strong>Bancos de Dados:</strong> PostgreSQL, MongoDB, Redis"
            },
            "experiência": {
                title: "Minha Experiência Profissional",
                content: "<strong>Desenvolvedor de IA Sênior</strong> - Tech Solutions Inc. (2022-Presente)<br>" +
                         "Lidero a equipe de desenvolvimento de modelos de Machine Learning para processamento de linguagem natural e visão computacional.<br><br>" +
                         "<strong>Engenheiro de Software</strong> - Inovação Digital Ltda. (2020-2022)<br>" +
                         "Desenvolvimento de aplicações web escaláveis e APIs RESTful para clientes corporativos.<br><br>" +
                         "<strong>Estagiário em Ciência de Dados</strong> - Data Insights Corp. (2019-2020)<br>" +
                         "Implementação de pipelines de dados e modelos preditivos para análise de mercado."
            },
            "contato": {
                title: "Informações de Contato",
                content: "<strong>Email:</strong> seu.email@portfolio.com<br>" +
                         "<strong>LinkedIn:</strong> linkedin.com/in/seuperfil<br>" +
                         "<strong>GitHub:</strong> github.com/seuusuario<br>" +
                         "<strong>Portfolio Online:</strong> seunome.dev<br><br>" +
                         "Estou sempre aberto a novas oportunidades e colaborações!"
            },
            "oi": {
                title: "Olá!",
                content: "Sou seu Agente de IA para portfolio. Posso apresentar seus projetos, habilidades, experiência profissional e informações de contato. Como posso ajudá-lo?"
            },
            "olá": {
                title: "Olá!",
                content: "Sou seu Agente de IA para portfolio. Posso apresentar seus projetos, habilidades, experiência profissional e informações de contato. Como posso ajudá-lo?"
            },
            "oi tudo bem": {
                title: "Tudo ótimo!",
                content: "Estou aqui para ajudar a mostrar suas habilidades e projetos. Em que posso ser útil?"
            }
        };
        
        this.defaultResponse = "Desculpe, não entendi sua pergunta. Você pode perguntar sobre meus <strong>projetos</strong>, <strong>habilidades</strong>, <strong>experiência</strong> ou <strong>contato</strong>.";
    }
    
    getResponse(userInput) {
        const input = userInput.toLowerCase().trim();
        
        // Verificar correspondências
        for (const [key, value] of Object.entries(this.responses)) {
            if (input.includes(key)) {
                return `<strong>${value.title}</strong><br><br>${value.content}`;
            }
        }
        
        // Resposta padrão
        return this.defaultResponse;
    }
    
    // Método para adicionar novas respostas
    addResponse(key, title, content) {
        this.responses[key] = { title, content };
    }
}
# Agente de IA para Portfolio

Um assistente virtual interativo para demonstração em portfolio, desenvolvido com HTML, CSS e JavaScript puro.

## Funcionalidades

- **Chat interativo** com respostas pré-programadas
- **Apresentação de projetos** com cards destacados
- **Informações sobre habilidades** e experiência profissional
- **Tema claro/escuro** com persistência local
- **Interface responsiva** para todos os dispositivos
- **Botões de ação rápida** para consultas comuns

## Tecnologias Utilizadas

- HTML5 semântico
- CSS3 com variáveis CSS e Flexbox/Grid
- JavaScript ES6+ (sem bibliotecas externas)
- Font Awesome para ícones
- Google Fonts (Inter e JetBrains Mono)



