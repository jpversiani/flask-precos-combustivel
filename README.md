# 🚗 Sistema de Preços de Combustível

Um sistema web completo desenvolvido em Flask para monitoramento e comparação de preços de combustível em postos de gasolina.

## 📋 Funcionalidades

- ✅ **Cadastro de Preços**: Adicione preços de diferentes tipos de combustível
- 📊 **Estatísticas Detalhadas**: Visualize análises por tipo de combustível
- 🔍 **Filtros Avançados**: Busque e filtre dados na tabela interativa
- 📱 **Design Responsivo**: Interface moderna e adaptável
- 🌐 **API REST**: Endpoints para integração com outras aplicações
- 📖 **Documentação da API**: Interface completa para desenvolvedores

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: SQLite com SQLAlchemy
- **Frontend**: Bootstrap 5, Font Awesome, JavaScript
- **Deployment**: Ngrok para exposição online

## 📁 Estrutura do Projeto

```
flask-precos-combustivel/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── popular_dados.py       # Script para popular dados de exemplo
├── README.md             # Documentação do projeto
├── instance/
│   └── precos_gasolina.db # Banco de dados SQLite
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── index.html        # Página inicial
│   ├── adicionar.html    # Formulário de cadastro
│   ├── editar.html       # Formulário de edição
│   ├── tabela.html       # Tabela de dados com filtros
│   ├── estatisticas.html # Página de estatísticas
│   └── api_docs.html     # Documentação da API
└── __pycache__/          # Cache Python (ignorado no Git)
```

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes Python)

### 1. Clone o Repositório
```bash
git clone https://github.com/jpversiani/flask-precos-combustivel.git
cd flask-precos-combustivel
```

### 2. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3. Execute a Aplicação
```bash
python app.py
```

### 4. Acesse o Sistema
Abra seu navegador e acesse: `http://localhost:5000`

## 📱 Executar no Android (Termux)

### 🚀 Instalação Automática (Recomendado)

**Método 1: Instalação em uma linha**
```bash
curl -fsSL https://raw.githubusercontent.com/jpversiani/flask-precos-combustivel/master/install_android.sh | bash
```

**Método 2: Download e execução manual**
```bash
# Baixar script de instalação
wget https://raw.githubusercontent.com/jpversiani/flask-precos-combustivel/master/install_android.sh
chmod +x install_android.sh
./install_android.sh
```

### 📋 Pré-requisitos
1. **Instalar Termux:**
   - Baixe da [F-Droid](https://f-droid.org/packages/com.termux/) (recomendado)
   - Ou da Google Play Store

2. **Executar a instalação automática** (script faz tudo automaticamente):
   - ✅ Atualiza pacotes do Termux
   - ✅ Instala Python, Git, Pip
   - ✅ Clona o repositório do GitHub
   - ✅ Instala dependências Python
   - ✅ Cria dados de exemplo
   - ✅ Configura scripts de inicialização

### 🎯 Após a Instalação
```bash
# Navegar para o projeto
cd ~/projetos/flask-precos-combustivel

# Iniciar servidor
./start_server.sh

# Acessar no navegador
# http://localhost:5000
```

### 🌐 Configurar Acesso Externo
```bash
# Configurar ngrok (opcional)
./setup_ngrok.sh
```

### 🔧 Instalação Manual (se preferir)
```bash
# Atualizar pacotes
pkg update && pkg upgrade

# Instalar dependências
pkg install python git python-pip

# Clonar repositório
git clone https://github.com/jpversiani/flask-precos-combustivel.git
cd flask-precos-combustivel

# Instalar dependências Python
pip install -r requirements.txt

# Criar dados de exemplo
python popular_dados.py

# Executar aplicação
python app.py
```

## 🌐 Exposição Online com Ngrok

### 1. Instalar Ngrok
```bash
# Windows
winget install ngrok

# Linux/Android (Termux)
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
tar -xzf ngrok-v3-stable-linux-arm64.tgz
mv ngrok $PREFIX/bin/
```

### 2. Configurar Authtoken
```bash
ngrok config add-authtoken SEU_AUTHTOKEN_AQUI
```

### 3. Expor Aplicação
```bash
ngrok http 5000
```

## 📊 API Endpoints

### Preços
- `GET /api/precos` - Lista todos os preços
- `GET /api/precos/{id}` - Detalhes de um preço específico
- `GET /api/precos/tipo/{tipo}` - Preços por tipo de combustível

### Estatísticas
- `GET /api/estatisticas` - Estatísticas gerais e por tipo

### Exemplo de Resposta
```json
{
  "id": 1,
  "posto": "Posto Shell",
  "endereco": "Rua das Flores, 123",
  "preco": 5.89,
  "tipo_combustivel": "Gasolina Comum",
  "data_atualizacao": "23/08/2025 15:30"
}
```

## 🎨 Páginas Disponíveis

- **/** - Página inicial com lista de preços
- **/adicionar** - Formulário para adicionar novos preços
- **/tabela** - Tabela completa com filtros avançados
- **/estatisticas** - Análises e gráficos detalhados
- **/api-docs** - Documentação completa da API
- **/editar/{id}** - Editar preço específico

## 🔧 Configuração

### Variáveis de Ambiente
```python
# app.py
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///precos_gasolina.db'
```

### Tipos de Combustível Suportados
- Gasolina Comum
- Gasolina Aditivada
- Etanol
- Diesel
- Diesel S-10

## 📝 Populando Dados de Exemplo

```bash
python popular_dados.py
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Seu Nome**
- GitHub: [@jpversiani](https://github.com/jpversiani)
- Email: jpversiani@outlook.com

## 🙏 Agradecimentos

- Flask Framework
- Bootstrap para UI
- Font Awesome para ícones
- Ngrok para exposição online

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**
