# Still need to work on the file structure, looks ugly
from openpyxl import Workbook
from io import BytesIO

def generate_excel(risks):
    wb = Workbook()
    ws = wb.active
    ws.title = "Risks"
    
    # Here goes the headers
    headers = ["ID", "Name", "Description"]
    ws.append(headers)
    
    # Here goes the data
    for risk in risks:
        ws.append([risk.id, risk.name, risk.description])
    
    # Save to a BytesIO object to use the file after being generated
    excel_file = BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)
    
    return excel_file