
---

```markdown
# 🧾 Payslip Generator with Email Automation

This project automates the generation and emailing of employee payslips using Python. It reads data from an Excel spreadsheet, generates a personalized PDF payslip for each employee, and emails the file to their respective addresses.

---

## 📁 Features

- Reads employee salary data from an Excel file using **pandas**
- Generates professional PDF payslips using **fpdf**
- Sends the payslips to each employee using **yagmail**
- Automatically creates and organizes payslip files

---

## 🛠️ Technologies Used

- Python 3.x
- [pandas](https://pypi.org/project/pandas/)
- [fpdf](https://pyfpdf.readthedocs.io/en/latest/)
- [yagmail](https://github.com/kootenpv/yagmail)

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/payslip-generator.git
   cd payslip-generator
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Required Files

- `employees.xlsx` – Excel file containing employee details.
- Columns should include: `Name`, `Email`, `Basic Salary`, `Allowances`, `Deductions`, `Gross Salary`, etc.

---

## 📧 Setup Email Credentials

1. Create a `.env` file and add:
   ```
   EMAIL=youremail@gmail.com
   EMAIL_PASSWORD=yourpassword
   ```

2. Or use app passwords if 2FA is enabled on Gmail.

---

## 🚀 Usage

1. Run the main script:
   ```bash
   python payslip_generator.py
   ```

2. The script will:
   - Read data from `employees.xlsx`
   - Generate a PDF payslip for each employee
   - Send it to their email using `yagmail`
   - Save PDFs in the `payslips/` directory

---

## 📄 Example Payslip

A generated payslip will include:
- Employee Name
- Basic Salary
- Allowances
- Deductions
- Net Pay

---

## 📌 Notes

- Make sure your Gmail allows access from third-party apps or use an App Password.
- Always test with dummy emails first to avoid spamming real inboxes.

---

## 📚 Resources for Students

- Pandas Docs: https://pandas.pydata.org/
- fpdf Docs: https://pyfpdf.readthedocs.io/
- Yagmail Docs: https://github.com/kootenpv/yagmail
- YouTube: Intro to Python Email Automation
- TutorialsPoint: Python for Beginners

---

## 🧑‍💻 Created For

Uncommon.org Bootcamp Final Project – Python Track

```

---

Let me know if you want this saved as a `.md` file or added to the existing project PDF!