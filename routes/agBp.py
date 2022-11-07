from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from model.agModel import Agenda

#Instancia o Blueprint
agBp = Blueprint('agBp', __name__)

'''
@agBp.route('/banco')
def agenda_list():
    db.create_all()
'''

@agBp.route('/agenda')
def lista_agenda():
    agenda_query = Agenda.query.all()
    return render_template('ag_lista.html', agenda = agenda_query)

@agBp.route('/agenda/create')
def cria_agenda():
    return render_template('ag_cria.html')

@agBp.route('/agenda/add', methods=['POST'])
def adiciona_agenda():
    
    agendaNome = request.form["nome"]
    agendaEmpresa = request.form["empresa"]
    agendaTelefone = request.form["telefone"]
    agendaEmail = request.form["email"]

    agenda = Agenda(nome = agendaNome, empresa = agendaEmpresa, telefone = agendaTelefone, email = agendaEmail)
    db.session.add(agenda)
    db.session.commit()

    return redirect(url_for('agBp.lista_agenda'))

@agBp.route('/agenda/update/<agenda_id>')
def atualiza_agenda(agenda_id = 0):
    agenda_query = Agenda.query.filter_by(id = agenda_id).first()
    return render_template('ag_atualiza.html', agenda = agenda_query)

@agBp.route('/agenda/upd', methods=['POST'])
def agenda_upd():

    agendaId = request.form['id']
    agendaNome = request.form['nome']
    agendaEmpresa = request.form['empresa']
    agendaTelefone = request.form['telefone']
    agendaEmail = request.form['email']

    agenda = Agenda.query.filter_by(id = agendaId).first()
    agenda.nome = agendaNome
    agenda.empresa = agendaEmpresa
    agenda.telefone = agendaTelefone
    agenda.email = agendaEmail
    db.session.add(agenda)
    db.session.commit()

    return redirect(url_for('agBp.lista_agenda'))

@agBp.route('/agenda/delete/<agenda_id>')
def agenda_deleta(agenda_id = 0):
    agenda_query = Agenda.query.filter_by(id = agenda_id).first()
    return render_template('ag_deleta.html', agenda = agenda_query)

@agBp.route('/agenda/dlt', methods=['POST'])
def agenda_dlt():

    agendaId = request.form['id']
    agenda = Agenda.query.filter_by(id = agendaId).first()
    db.session.delete(agenda)
    db.session.commit()

    return redirect(url_for('agBp.lista_agenda'))
