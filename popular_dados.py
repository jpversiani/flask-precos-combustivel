from app import app, db, PrecoGasolina
from datetime import datetime, timedelta
import random

# Dados fictícios de postos de gasolina de Montes Claros
postos_montes_claros = [
    {
        "posto": "Posto Ipiranga Centro",
        "endereco": "Av. Coronel Prates, 123 - Centro, Montes Claros - MG"
    },
    {
        "posto": "Shell Select Major Lopes",
        "endereco": "Av. Major Lopes, 456 - Major Lopes, Montes Claros - MG"
    },
    {
        "posto": "BR Petrobras Ibituruna",
        "endereco": "Av. Ibituruna, 789 - Ibituruna, Montes Claros - MG"
    },
    {
        "posto": "Ale Combustíveis",
        "endereco": "Rua Urbino Viana, 321 - Centro, Montes Claros - MG"
    },
    {
        "posto": "Posto Bandeira Branca",
        "endereco": "Av. Cula Mangabeira, 654 - Santo Expedito, Montes Claros - MG"
    },
    {
        "posto": "Texaco Vila Mauricéia",
        "endereco": "Rua Coronel Celestino, 987 - Vila Mauricéia, Montes Claros - MG"
    },
    {
        "posto": "Posto do Zé - São Geraldo",
        "endereco": "Av. São Geraldo, 147 - São Geraldo, Montes Claros - MG"
    },
    {
        "posto": "Auto Posto Eldorado",
        "endereco": "Av. Dulce Sarmento, 258 - Eldorado, Montes Claros - MG"
    },
    {
        "posto": "Posto Universitário",
        "endereco": "Av. Rui Braga, 369 - Vila Universitária, Montes Claros - MG"
    },
    {
        "posto": "Ipiranga Todos os Santos",
        "endereco": "Rua Todos os Santos, 741 - Todos os Santos, Montes Claros - MG"
    },
    {
        "posto": "Shell Morrinhos",
        "endereco": "Av. dos Morrinhos, 852 - Morrinhos, Montes Claros - MG"
    },
    {
        "posto": "BR Distribuidora Planalto",
        "endereco": "Rua do Planalto, 963 - Planalto, Montes Claros - MG"
    },
    {
        "posto": "Posto Cidade Nova",
        "endereco": "Av. Cidade Nova, 159 - Cidade Nova, Montes Claros - MG"
    },
    {
        "posto": "Auto Posto JK",
        "endereco": "Av. Juscelino Kubitschek, 357 - JK, Montes Claros - MG"
    },
    {
        "posto": "Petrobras Vila Atlântida",
        "endereco": "Rua Vila Atlântida, 486 - Vila Atlântida, Montes Claros - MG"
    }
]

# Tipos de combustível disponíveis
tipos_combustivel = [
    "Gasolina Comum",
    "Gasolina Aditivada", 
    "Etanol",
    "Diesel",
    "Diesel S-10"
]

def gerar_preco_realista(tipo_combustivel):
    """Gera preços realistas baseados no tipo de combustível"""
    base_prices = {
        "Gasolina Comum": (5.20, 5.80),
        "Gasolina Aditivada": (5.40, 6.00),
        "Etanol": (3.80, 4.40),
        "Diesel": (5.80, 6.40),
        "Diesel S-10": (6.00, 6.60)
    }
    
    min_price, max_price = base_prices.get(tipo_combustivel, (5.00, 6.00))
    return round(random.uniform(min_price, max_price), 2)

def gerar_data_aleatoria():
    """Gera uma data aleatória nos últimos 30 dias"""
    dias_atras = random.randint(0, 30)
    horas_atras = random.randint(0, 23)
    minutos_atras = random.randint(0, 59)
    
    return datetime.now() - timedelta(days=dias_atras, hours=horas_atras, minutes=minutos_atras)

def popular_banco_dados():
    """Popula o banco de dados com dados fictícios"""
    with app.app_context():
        # Cria as tabelas se não existirem
        print("Criando tabelas do banco de dados...")
        db.create_all()
        print("Tabelas criadas com sucesso!")
        
        # Limpa dados existentes (opcional)
        print("Verificando dados existentes...")
        count_existing = PrecoGasolina.query.count()
        print(f"Encontrados {count_existing} registros existentes.")
        
        if count_existing > 0:
            print(f"Removendo {count_existing} registros existentes...")
            PrecoGasolina.query.delete()
            db.session.commit()
            print("Dados existentes removidos.")
        
        print("\nPopulando banco de dados com exemplos de Montes Claros...")
        
        registros_criados = 0
        
        # Para cada posto, cria registros para diferentes tipos de combustível
        for posto_info in postos_montes_claros:
            # Cada posto terá de 2 a 4 tipos de combustível
            num_combustiveis = random.randint(2, 4)
            combustiveis_posto = random.sample(tipos_combustivel, num_combustiveis)
            
            for tipo_combustivel in combustiveis_posto:
                preco = gerar_preco_realista(tipo_combustivel)
                data_atualizacao = gerar_data_aleatoria()
                
                novo_registro = PrecoGasolina(
                    posto=posto_info["posto"],
                    endereco=posto_info["endereco"],
                    preco=preco,
                    tipo_combustivel=tipo_combustivel,
                    data_atualizacao=data_atualizacao
                )
                
                db.session.add(novo_registro)
                registros_criados += 1
                
                print(f"✓ {posto_info['posto']} - {tipo_combustivel}: R$ {preco:.2f}")
        
        # Salva todas as alterações
        db.session.commit()
        
        print(f"\n🎉 Banco de dados populado com sucesso!")
        print(f"📊 Total de registros criados: {registros_criados}")
        print(f"🏪 Total de postos: {len(postos_montes_claros)}")
        print(f"⛽ Tipos de combustível: {', '.join(tipos_combustivel)}")
        
        # Mostra estatísticas
        print("\n📈 Estatísticas dos preços gerados:")
        for tipo in tipos_combustivel:
            precos_tipo = [p.preco for p in PrecoGasolina.query.filter_by(tipo_combustivel=tipo).all()]
            if precos_tipo:
                print(f"  {tipo}:")
                print(f"    Menor: R$ {min(precos_tipo):.2f}")
                print(f"    Maior: R$ {max(precos_tipo):.2f}")
                print(f"    Média: R$ {sum(precos_tipo)/len(precos_tipo):.2f}")
                print(f"    Registros: {len(precos_tipo)}")

if __name__ == "__main__":
    print("🚗 Populador de Dados - Sistema de Preços de Gasolina")
    print("📍 Cidade: Montes Claros - MG")
    print("="*60)
    
    try:
        popular_banco_dados()
        print("\n✅ Processo concluído com sucesso!")
        print("🌐 Acesse http://localhost:5000 para ver os dados")
    except Exception as e:
        print(f"\n❌ Erro ao popular banco de dados: {e}")
        print("Certifique-se de que a aplicação Flask está configurada corretamente.")