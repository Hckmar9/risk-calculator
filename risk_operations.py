from flask import redirect, url_for
from models import db, Risk

def add_risk(form_data):
    new_risk = Risk(
        name=form_data['name'],
        description=form_data['description'],
        probability=int(form_data['probability']),
        impact=int(form_data['impact']),
        score=int(form_data['probability']) * int(form_data['impact']),
        mitigation_strategy=form_data['mitigation_strategy'],
        status=form_data['status']
    )
    db.session.add(new_risk)
    db.session.commit()
    return redirect(url_for('index'))

def update_risk(id, form_data):
    risk = Risk.query.get_or_404(id)
    risk.name = form_data['name']
    risk.description = form_data['description']
    risk.probability = int(form_data['probability'])
    risk.impact = int(form_data['impact'])
    risk.score = risk.probability * risk.impact
    risk.mitigation_strategy = form_data['mitigation_strategy']
    risk.status = form_data['status']
    db.session.commit()
    return redirect(url_for('index'))

def delete_risk(id):
    risk = Risk.query.get_or_404(id)
    db.session.delete(risk)
    db.session.commit()
    return redirect(url_for('index'))