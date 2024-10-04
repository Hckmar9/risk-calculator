from flask import Flask, render_template, request, send_file
from models import db, Risk
from routes import init_routes
from excel_utils import generate_excel
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///risks.db'
db.init_app(app)

def init_db():
    with app.app_context():
        db.create_all()

init_routes(app)

@app.route('/download_excel')
def download_excel():
    risks = Risk.query.all()
    excel_file = generate_excel(risks)
    current_datetime = datetime.now().strftime("%Y%m%d")
    filename = f'risks-file_{current_datetime}.xlsx'
    return send_file(excel_file, 
                        download_name=filename,
                        as_attachment=True)

if __name__ == '__main__':
    init_db()
    app.run(debug=True,port=5001)