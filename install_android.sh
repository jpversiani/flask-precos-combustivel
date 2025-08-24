#!/bin/bash

# Script de Instalação Automática para Android (Termux)
# Sistema Flask de Preços de Combustível
# Autor: João Paulo Versiani

echo "🚀 Instalando Sistema Flask de Preços de Combustível no Android..."
echo "================================================="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCESSO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[AVISO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERRO]${NC} $1"
}

# Verificar se está rodando no Termux
if [ ! -d "/data/data/com.termux" ]; then
    print_error "Este script deve ser executado no Termux!"
    print_warning "Instale o Termux da F-Droid ou Google Play Store"
    exit 1
fi

print_status "Verificando Termux... ✓"

# Atualizar pacotes do Termux
print_status "Atualizando pacotes do Termux..."
pkg update -y && pkg upgrade -y

# Instalar dependências necessárias
print_status "Instalando dependências..."
pkg install -y python git wget curl

# Verificar se pip está disponível
if ! command -v pip &> /dev/null; then
    print_status "Instalando pip..."
    pkg install -y python-pip
fi

# Criar diretório de projetos
cd $HOME
if [ ! -d "projetos" ]; then
    mkdir projetos
    print_status "Diretório 'projetos' criado"
fi

cd projetos

# Remover instalação anterior se existir
if [ -d "flask-precos-combustivel" ]; then
    print_warning "Removendo instalação anterior..."
    rm -rf flask-precos-combustivel
fi

# Clonar repositório do GitHub
print_status "Baixando projeto do GitHub..."
if git clone https://github.com/jpversiani/flask-precos-combustivel.git; then
    print_success "Projeto baixado com sucesso!"
else
    print_error "Falha ao baixar o projeto do GitHub"
    exit 1
fi

cd flask-precos-combustivel

# Instalar dependências Python
print_status "Instalando dependências Python..."
if pip install -r requirements.txt; then
    print_success "Dependências instaladas com sucesso!"
else
    print_error "Falha ao instalar dependências"
    exit 1
fi

# Criar dados de exemplo
print_status "Criando dados de exemplo..."
echo "📊 Populando banco de dados com dados de exemplo..."
echo "Criando tabelas e inserindo dados de exemplo..."
if python popular_dados.py; then
    print_success "Dados de exemplo criados!"
else
    print_warning "Falha ao criar dados de exemplo (continuando...)"
fi

# Criar script de inicialização
print_status "Criando script de inicialização..."
cat > start_server.sh << 'EOF'
#!/bin/bash
echo "🚀 Iniciando Servidor Flask..."
echo "================================"
echo "📱 Acesse: http://localhost:5000"
echo "🌐 Para acesso externo, configure ngrok"
echo "⏹️  Para parar: Ctrl+C"
echo ""
python app.py
EOF

chmod +x start_server.sh

# Criar script para ngrok (opcional)
print_status "Criando script para ngrok..."
cat > setup_ngrok.sh << 'EOF'
#!/bin/bash
echo "🌐 Configurando Ngrok para acesso externo..."
echo "==========================================="

# Verificar se ngrok está instalado
if ! command -v ngrok &> /dev/null; then
    echo "📥 Baixando ngrok..."
    wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
    tar -xzf ngrok-v3-stable-linux-arm64.tgz
    chmod +x ngrok
    echo "✓ Ngrok instalado!"
    echo "⚠️  Configure sua auth token: ./ngrok config add-authtoken SEU_TOKEN"
    echo "📖 Obtenha seu token em: https://dashboard.ngrok.com/get-started/your-authtoken"
else
    echo "✓ Ngrok já está instalado!"
fi

echo ""
echo "🚀 Para expor o servidor:"
echo "1. Execute: ./start_server.sh (em um terminal)"
echo "2. Execute: ./ngrok http 5000 (em outro terminal)"
echo "3. Use a URL fornecida pelo ngrok para acesso externo"
EOF

chmod +x setup_ngrok.sh

# Criar arquivo de informações
cat > INSTALACAO_ANDROID.md << 'EOF'
# 📱 Sistema Flask no Android - Instalado com Sucesso!

## 🚀 Como usar:

### Iniciar o servidor:
```bash
./start_server.sh
```

### Acessar localmente:
- Abra o navegador e vá para: `http://localhost:5000`

### Configurar acesso externo (opcional):
```bash
./setup_ngrok.sh
```

## 📁 Estrutura do projeto:
- `app.py` - Aplicação Flask principal
- `templates/` - Templates HTML
- `instance/precos_gasolina.db` - Banco de dados SQLite
- `requirements.txt` - Dependências Python

## 🔧 Comandos úteis:

### Atualizar projeto:
```bash
git pull origin master
pip install -r requirements.txt
```

### Resetar banco de dados:
```bash
rm -f instance/precos_gasolina.db
python popular_dados.py
```

### Parar servidor:
- Pressione `Ctrl+C` no terminal onde o servidor está rodando

## 📞 Suporte:
- GitHub: https://github.com/jpversiani/flask-precos-combustivel
- Documentação completa no README.md
EOF

print_success "Instalação concluída com sucesso!"
echo ""
echo "================================================="
echo "🎉 Sistema Flask de Preços de Combustível instalado!"
echo "================================================="
echo ""
echo "📍 Localização: $HOME/projetos/flask-precos-combustivel"
echo ""
echo "🚀 Para iniciar o servidor:"
echo "   cd $HOME/projetos/flask-precos-combustivel"
echo "   ./start_server.sh"
echo ""
echo "📱 Acesse: http://localhost:5000"
echo ""
echo "🌐 Para acesso externo:"
echo "   ./setup_ngrok.sh"
echo ""
echo "📖 Leia: INSTALACAO_ANDROID.md para mais informações"
echo ""
print_success "Instalação finalizada! Aproveite! 🎯"