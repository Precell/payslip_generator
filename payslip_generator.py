import os
import pandas as pd
from fpdf import FPDF
import yagmail

# Load environment variables
EMAIL_USER = os.getenv("")
EMAIL_PASS = os.getenv("")

# Load employee data
df = pd.read_excel("employees.xlsx")

# # Create output directory if it doesn't exist
os.makedirs("payslips", exist_ok=True)

# Initialize email client


def generate_payslip(emp):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    emp_id = emp["ID"]
    name = emp["Name"]
    basic = emp["Basic Salary"]
    allow = emp["Allowances"]
    deduct = emp["Deductions"]
    net = basic + allow - deduct

    lines = [
        f"Payslip for {name} (ID: {emp_id})",
        "",
        f"Basic Salary: ${basic:.2f}",
        f"Allowances: ${allow:.2f}",
        f"Deductions: ${deduct:.2f}",
        f"Net Salary: ${net:.2f}",
    ]

    for line in lines:
        pdf.cell(200, 10, txt=line, ln=True)

    file_path = f"payslips/{emp_id}.pdf"
    pdf.output(file_path)
    return file_path

def send_email(emp, file_path):
    subject = "Your Payslip for This Month"
    body = f"Dear {emp['Name']},\n\nPlease find attached your payslip for this month.\n\nBest regards,\nHR Department"
    yag.send(to=emp["Email"], subject=subject, contents=body, attachments=file_path)

# Process each employee
for _, row in df.iterrows():
    try:
        pdf_path = generate_payslip(row)
        send_email(row, pdf_path)
        print(f"Payslip sent to {row['Name']} ({row['Email']})")
    except Exception as e:
        print(f"Failed for {row['Name']}: {e}")
