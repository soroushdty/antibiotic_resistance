import pandas as pd

# Load CSVs
labevents = pd.read_csv('labevents.csv', dtype=str)
emar = pd.read_csv('emar.csv', dtype=str)
emar_detail = pd.read_csv('emar_detail.csv', dtype=str)
chartevents = pd.read_csv('chartevents.csv', dtype=str)
prescriptions = pd.read_csv('prescriptions.csv', dtype=str)
pharmacy = pd.read_csv('pharmacy.csv', dtype=str)
ingredientevents = pd.read_csv('ingredientevents.csv', dtype=str)
patients = pd.read_csv('patients.csv', dtype=str)
datetimeevents = pd.read_csv('datetimeevents.csv', dtype=str)
admissions = pd.read_csv('admissions.csv', dtype=str)
omr = pd.read_csv('omr.csv', dtype=str)
icustays = pd.read_csv('icustays.csv', dtype=str)
procedureevents = pd.read_csv('procedureevents.csv', dtype=str)
transfers = pd.read_csv('transfers.csv', dtype=str)
d_labitems = pd.read_csv('d_labitems.csv', dtype=str)
d_items = pd.read_csv('d_items.csv', dtype=str)