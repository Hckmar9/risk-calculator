from flask import render_template, request
from models import Risk
from risk_operations import add_risk, update_risk, delete_risk

def init_routes(app):
    @app.route('/')
    def index():
        risks = Risk.query.all()
        return render_template('index.html', risks=risks)

    @app.route('/add_risk', endpoint='route_add_risk', methods=['POST'])
    def route_add_risk():
        return add_risk(request.form)

    @app.route('/update_risk/<int:id>', endpoint='route_update_risk', methods=['POST'])
    def route_update_risk(id):
        return update_risk(id, request.form)

    @app.route('/delete_risk/<int:id>', endpoint='route_delete_risk')
    def route_delete_risk(id):
        return delete_risk(id)

    @app.route('/dashboard')
    def dashboard():
        risks = Risk.query.all()
        dashboard_data = prepare_dashboard_data(risks)
        return render_template('dashboard.html', dashboard_data=dashboard_data)

def prepare_dashboard_data(risks):
    prioritized_risks = sorted(risks, key=lambda r: r.score, reverse=True)
    
    return {
        'priority_chart_data': prepare_priority_chart_data(prioritized_risks[:5]),
        'category_chart_data': prepare_category_chart_data(risks),
        'risk_matrix_data': prepare_risk_matrix_data(risks)
    }

def categorize_risks(risks):
    return {
        'High': [r for r in risks if r.score > 15],
        'Medium': [r for r in risks if 9 <= r.score <= 15],
        'Low': [r for r in risks if r.score < 9]
    }

def prepare_risk_matrix_data(risks):
    risk_matrix = {}
    for risk in risks:
        key = f"{risk.impact}-{risk.probability}"
        if key not in risk_matrix:
            risk_matrix[key] = []
        risk_matrix[key].append(risk.name)
    return risk_matrix

def prepare_priority_chart_data(top_risks):
    return {
        'labels': [risk.name for risk in top_risks],
        'datasets': [{
            'label': 'Risk Score',
            'data': [risk.score for risk in top_risks],
            'backgroundColor': 'rgba(75, 192, 192, 0.6)',
            'borderColor': 'rgba(75, 192, 192, 1)',
            'borderWidth': 1
        }]
    }

def prepare_category_chart_data(risks):
    categorized = categorize_risks(risks)
    return {
        'labels': ['High', 'Medium', 'Low'],
        'datasets': [{
            'label': 'Number of Risks',
            'data': [len(categorized['High']), len(categorized['Medium']), len(categorized['Low'])]
        }]
    }