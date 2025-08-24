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
git clone https://github.com/seu-usuario/flask-precos-combustivel.git
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

## 📱 Execução no Android (Termux)

### 1. Instalar Termux
- Baixe o Termux da F-Droid ou Google Play Store

### 2. Configurar Ambiente
```bash
# Atualizar pacotes
pkg update && pkg upgrade

# Instalar Python e Git
pkg install python git
pkg install python-pip
```

### 3. Clonar e Executar
```bash
# Clonar repositório
git clone https://github.com/seu-usuario/flask-precos-combustivel.git
cd flask-precos-combustivel

# Instalar dependências
pip install -r requirements.txt

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
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Email: seu.email@exemplo.com

## 🙏 Agradecimentos

- Flask Framework
- Bootstrap para UI
- Font Awesome para ícones
- Ngrok para exposição online

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**