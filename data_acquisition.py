# Perquisites
import pandas as pd
import gc
from csv_list import csv_files, comments

# Find microbiology results
microbiology = pd.read_csv('microbiologyevents.csv.gz', compression='gzip', dtype=str,
                           usecols=csv_files['microbiologyevents'])

# Specify test type
microbiology = microbiology[((microbiology.spec_type_desc=='URINE')|
                             (microbiology.spec_type_desc=='BLOOD CULTURE'))
                             &
                             ((microbiology.test_name=='URINE CULTURE')|
                              (microbiology.test_name=='Blood Culture, Routine')|
                              (microbiology.test_name=='AEROBIC BOTTLE')|
                              (microbiology.test_name=='FLUID CULTURE')|
                              (microbiology.test_name=='ANAEROBIC BOTTLE')|
                              (microbiology.test_name=='ANAEROBIC CULTURE'))]

urine = microbiology[microbiology.spec_type_desc=='URINE'].drop(['test_name', 'spec_type_desc'], axis=1)
blood = microbiology[microbiology.spec_type_desc=='BLOOD CULTURE'].drop(['test_name', 'spec_type_desc'], axis=1)

# Categorize test results (+/-)
blood_positive = blood[blood.ab_name.notnull()]
blood_negative = blood[(blood.ab_name.isnull()) & (blood.org_name.isnull())]
urine_positive = urine[urine.ab_name.notnull()]
urine_negative = urine[(urine.ab_name.isnull()) & (urine.org_name.isnull())]

# Comment exclusions
urine_positive = urine_positive[~urine_positive['comments'].apply(lambda x: any(str(comment) in x for comment in comments['urine_positive']) if pd.notnull(x) else False)]
urine_negative = urine_negative[~urine_negative['comments'].apply(lambda x: any(str(comment) in x for comment in comments['urine_negative']) if pd.notnull(x) else False)]
blood_negative = blood_negative[~blood_negative['comments'].apply(lambda x: any(str(comment) in x for comment in comments['blood_negative']) if pd.notnull(x) else False)]

# Drop unnecessary columns
blood_positive = blood_positive.drop(['comments', 'org_name', 'ab_name', 'interpretation'], axis=1)
blood_negative = blood_negative.drop(['comments', 'org_name', 'ab_name', 'interpretation'], axis=1)
urine_positive = urine_positive.drop(['comments', 'org_name', 'ab_name', 'interpretation'], axis=1)
urine_negative = urine_negative.drop(['comments', 'org_name', 'ab_name', 'interpretation'], axis=1)

# Categorize test results (S/R)
urine_sensitive = urine_positive[urine_positive.interpretation=='S']
urine_resistant = urine_positive[urine_positive.interpretation=='R']
blood_sensitive = blood_positive[blood_positive.interpretation=='S']
blood_resistant = blood_positive[blood_positive.interpretation=='R']

# Check length 
print(f"blood_negative: {len(blood_negative)}")
print(f"blood_sensitive: {len(blood_sensitive)}")
print(f"blood_resistant: {len(blood_resistant)}")
print(f"urine_negative: {len(urine_negative)}")
print(f"urine_sensitive: {len(urine_sensitive)}")
print(f"urine_resistant: {len(urine_resistant)}")

# Create subject_id filter
filter = pd.concat([blood_negative, blood_sensitive, blood_resistant,urine_negative,
                    urine_sensitive, urine_resistant]).subject_id.drop_duplicates()

# Filter large CSV files
large_csv = ['labevents', 'emar', 'emar_detail', 'chartevents', 'prescriptions', 'pharmacy', 'ingredientevents']
c = {}
for item in large_csv:
    for chunk in pd.read_csv(f'{item}.csv.gz', compression='gzip', dtype=str,
                                usecols=csv_files[item], chunksize=10 ** 6):
        c[item] = chunk.merge(filter, how='inner', on=['subject_id'])
        del chunk
        gc.collect()
    c[item].to_csv(f'{item}.csv',index=False)
# del c

# Load CSVs
## load (filtered) large csvs as is
labevents = pd.read_csv('labevents.csv', dtype=str)
emar = pd.read_csv('emar.csv', dtype=str)
emar_detail = pd.read_csv('emar_detail.csv', dtype=str)
chartevents = pd.read_csv('chartevents.csv', dtype=str)
prescriptions = pd.read_csv('prescriptions.csv', dtype=str)
pharmacy = pd.read_csv('pharmacy.csv', dtype=str)
ingredientevents = pd.read_csv('ingredientevents.csv', dtype=str)

## load csvs without subject_id without filtering
d_labitems = pd.read_csv('d_labitems.csv.gz', compression='gzip', usecols=csv_files['d_labitems'], dtype=str)
d_items = pd.read_csv('d_items.csv.gz', compression='gzip', usecols=csv_files['d_items'], dtype=str)

## load others with filtering
patients = pd.read_csv('patients.csv.gz', compression='gzip', usecols=csv_files['patients'], dtype=str)
patients = patients.merge(filter, how='inner', on=['subject_id'])

datetimeevents = pd.read_csv('datetimeevents.csv.gz', compression='gzip', usecols=csv_files['datetimeevents'], dtype=str)
datetimeevents = datetimeevents.merge(filter, how='inner', on=['subject_id'])

admissions = pd.read_csv('admissions.csv.gz', compression='gzip', usecols=csv_files['admissions'], dtype=str)
admissions = admissions.merge(filter, how='inner', on=['subject_id'])

omr = pd.read_csv('omr.csv.gz', compression='gzip', usecols=csv_files['omr'], dtype=str)
omr = omr.merge(filter, how='inner', on=['subject_id'])

icustays = pd.read_csv('icustays.csv.gz', compression='gzip', usecols=csv_files['icustays'], dtype=str)
icustays = icustays.merge(filter, how='inner', on=['subject_id'])

procedureevents = pd.read_csv('procedureevents.csv.gz', compression='gzip', usecols=csv_files['procedureevents'], dtype=str)
procedureevents = procedureevents.merge(filter, how='inner', on=['subject_id'])

transfers = pd.read_csv('transfers.csv.gz', compression='gzip', usecols=csv_files['transfers'], dtype=str)
transfers = transfers.merge(filter, how='inner', on=['subject_id'])