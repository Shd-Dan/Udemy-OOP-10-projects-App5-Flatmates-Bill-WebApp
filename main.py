from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

# The inputs
amount = float(input("Enter total bill amount: "))
period = input("Enter period (months year): ")

name_1 = input("Please enter name: ")
days_in_period_1 = int(input(f"How many days did {name_1} stay in house? "))

name_2 = input("Please enter other name: ")
days_in_period_2 = int(input(f"How many days did {name_2} stay in house? "))

the_bill = Bill(amount, period)
flatmate_1 = Flatmate(name=name_1, days_in_house=days_in_period_1)
flatmate_2 = Flatmate(name=name_2, days_in_house=days_in_period_2)

print(f"{flatmate_1.name} pays:", round(flatmate_1.pays(bill=the_bill, flatmate2=flatmate_2), 2))
print(f"{flatmate_2.name} pays:", round(flatmate_2.pays(bill=the_bill, flatmate2=flatmate_1), 2))

pdf_report = PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1=flatmate_1, flatmate2=flatmate_2, bill=the_bill)

file_sharer = FileSharer(pdf_report.filename)
print(file_sharer.share())
