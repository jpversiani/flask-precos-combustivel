from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///precos_gasolina.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de dados
class PrecoGasolina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posto = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    tipo_combustivel = db.Column(db.String(50), nullable=False, default='Gasolina Comum')
    data_atualizacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<PrecoGasolina {self.posto}: R$ {self.preco}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'posto': self.posto,
            'endereco': self.endereco,
            'preco': self.preco,
            'tipo_combustivel': self.tipo_combustivel,
            'data_atualizacao': self.data_atualizacao.strftime('%d/%m/%Y %H:%M')
        }

# Rotas
@app.route('/')
def index():
    precos = PrecoGasolina.query.order_by(PrecoGasolina.preco.asc()).all()
    return render_template('index.html', precos=precos)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_preco():
    if request.method == 'POST':
        posto = request.form['posto']
        endereco = request.form['endereco']
        preco = float(request.form['preco'])
        tipo_combustivel = request.form['tipo_combustivel']
        
        novo_preco = PrecoGasolina(
            posto=posto,
            endereco=endereco,
            preco=preco,
            tipo_combustivel=tipo_combustivel
        )
        
        try:
            db.session.add(novo_preco)
            db.session.commit()
            flash('Preço adicionado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash('Erro ao adicionar preço. Tente novamente.', 'error')
            db.session.rollback()
    
    return render_template('adicionar.html')

@app.route('/tabela')
def tabela():
    precos = PrecoGasolina.query.order_by(PrecoGasolina.preco.asc()).all()
    return render_template('tabela.html', precos=precos)

@app.route('/api-docs')
def api_docs():
    return render_template('api_docs.html')

@app.route('/estatisticas')
def estatisticas():
    precos = PrecoGasolina.query.all()
    
    # Estatísticas por tipo de combustível
    stats_por_tipo = {}
    for tipo in ['Gasolina Comum', 'Gasolina Aditivada', 'Etanol', 'Diesel', 'Diesel S-10']:
        precos_tipo = [p for p in precos if p.tipo_combustivel == tipo]
        if precos_tipo:
            precos_valores = [float(p.preco) for p in precos_tipo]
            stats_por_tipo[tipo] = {
                'count': len(precos_valores),
                'min': min(precos_valores),
                'max': max(precos_valores),
                'avg': sum(precos_valores) / len(precos_valores),
                'postos': list(set([p.posto for p in precos_tipo]))
            }
    
    # Estatísticas gerais
    total_precos = len(precos)
    total_postos = len(set([p.posto for p in precos]))
    
    return render_template('estatisticas.html', 
                         stats_por_tipo=stats_por_tipo,
                         total_precos=total_precos,
                         total_postos=total_postos)

@app.route('/api/precos')
def api_precos():
    precos = PrecoGasolina.query.order_by(PrecoGasolina.preco.asc()).all()
    return jsonify([
        {
            'id': preco.id,
            'posto': preco.posto,
            'endereco': preco.endereco,
            'preco': float(preco.preco),
            'tipo_combustivel': preco.tipo_combustivel,
            'data_atualizacao': preco.data_atualizacao.isoformat()
        } for preco in precos
    ])

@app.route('/api/precos/<int:preco_id>')
def api_preco_detalhes(preco_id):
    preco = PrecoGasolina.query.get_or_404(preco_id)
    return jsonify({
        'id': preco.id,
        'posto': preco.posto,
        'endereco': preco.endereco,
        'preco': float(preco.preco),
        'tipo_combustivel': preco.tipo_combustivel,
        'data_atualizacao': preco.data_atualizacao.isoformat()
    })

@app.route('/api/precos/tipo/<tipo_combustivel>')
def api_precos_por_tipo(tipo_combustivel):
    precos = PrecoGasolina.query.filter_by(tipo_combustivel=tipo_combustivel).order_by(PrecoGasolina.preco.asc()).all()
    return jsonify([
        {
            'id': preco.id,
            'posto': preco.posto,
            'endereco': preco.endereco,
            'preco': float(preco.preco),
            'tipo_combustivel': preco.tipo_combustivel,
            'data_atualizacao': preco.data_atualizacao.isoformat()
        } for preco in precos
    ])

@app.route('/api/estatisticas')
def api_estatisticas():
    precos = PrecoGasolina.query.all()
    
    stats_por_tipo = {}
    for tipo in ['Gasolina Comum', 'Gasolina Aditivada', 'Etanol', 'Diesel', 'Diesel S-10']:
        precos_tipo = [p for p in precos if p.tipo_combustivel == tipo]
        if precos_tipo:
            precos_valores = [float(p.preco) for p in precos_tipo]
            stats_por_tipo[tipo] = {
                'count': len(precos_valores),
                'min': min(precos_valores),
                'max': max(precos_valores),
                'avg': round(sum(precos_valores) / len(precos_valores), 2)
            }
    
    return jsonify({
        'total_precos': len(precos),
        'total_postos': len(set([p.posto for p in precos])),
        'estatisticas_por_tipo': stats_por_tipo
    })

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_preco(id):
    preco = PrecoGasolina.query.get_or_404(id)
    
    if request.method == 'POST':
        preco.posto = request.form['posto']
        preco.endereco = request.form['endereco']
        preco.preco = float(request.form['preco'])
        preco.tipo_combustivel = request.form['tipo_combustivel']
        preco.data_atualizacao = datetime.utcnow()
        
        try:
            db.session.commit()
            flash('Preço atualizado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash('Erro ao atualizar preço. Tente novamente.', 'error')
            db.session.rollback()
    
    return render_template('editar.html', preco=preco)

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_preco(id):
    preco = PrecoGasolina.query.get_or_404(id)
    
    try:
        db.session.delete(preco)
        db.session.commit()
        flash('Preço removido com sucesso!', 'success')
    except Exception as e:
        flash('Erro ao remover preço. Tente novamente.', 'error')
        db.session.rollback()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)