# Run this once after downloading all csv.gz files
# To create necessary csv files

# Perquisites
import pandas as pd
import gc
import json
from csv_list import csv_files, comments
print('modules imported successfully')

# Find microbiology results
microbiology = pd.read_csv('microbiologyevents.csv.gz', compression='gzip', dtype=str,
                           usecols=csv_files['microbiologyevents'])
print('micrbiologyevents.csv.gz loaded')

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
blood_positive = blood_positive.drop(['comments'], axis=1)
urine_positive = urine_positive.drop(['comments'], axis=1)
blood_negative = blood_negative.drop(['comments', 'org_name', 'ab_name','interpretation'], axis=1)
urine_negative = urine_negative.drop(['comments', 'org_name', 'ab_name','interpretation'], axis=1)

# Categorize test results (S/R)
urine_sensitive = urine_positive[urine_positive.interpretation=='S'].drop(['interpretation'], axis=1)
urine_resistant = urine_positive[urine_positive.interpretation=='R'].drop(['interpretation'], axis=1)
blood_sensitive = blood_positive[blood_positive.interpretation=='S'].drop(['interpretation'], axis=1)
blood_resistant = blood_positive[blood_positive.interpretation=='R'].drop(['interpretation'], axis=1)
print('test result filtering completed')

# Save to csv
blood_negative.to_csv('blood_negative.csv',index=False)
print('blood_negative.csv saved successfully')
blood_sensitive.to_csv('blood_sensitive.csv',index=False)
print('blood_sensitive.csv saved successfully')
blood_resistant.to_csv('blood_resistant.csv',index=False)
print('blood_resistant.csv saved successfully')
urine_negative.to_csv('urine_negative.csv',index=False)
print('urine_negative.csv saved successfully')
urine_sensitive.to_csv('urine_sensitive.csv',index=False)
print('urine_sensitive.csv saved successfully')
urine_resistant.to_csv('urine_resistant.csv',index=False)
print('urine_resistant.csv saved successfully')

# Create subject_id filter
filter = pd.concat([blood_negative, blood_sensitive, blood_resistant,urine_negative,
                    urine_sensitive, urine_resistant]).subject_id.drop_duplicates()
filter.to_csv('filter.csv',index=False)
print('filter.csv created successfully')

# Filter large CSV files
c = {}  # WHY AM I USING A DICT HERE??
chunksize = 10 ** 6

with open('nrows.json', 'r') as f:
    nrows = json.load(f)

for k,v in nrows.items():
    head = 0
    print(f'Processing {k}:')
    for chunk in pd.read_csv(f'{k}.csv.gz', compression='gzip', dtype=str,
                                usecols=csv_files[k], chunksize=chunksize):
        c[k] = chunk.merge(filter, how='inner', on=['subject_id'])
        head += len(chunk)
        print(f'Part {head//chunksize} out of {(int(v)//chunksize)+1}...')  # WHY THIS DOESNT PRINT LAST CHUNK??
        del chunk
        gc.collect()
    c[k].to_csv(f'{k}.csv',index=False)
    print(f'{k}.csv created.')

# Filter smaller CSV files
patients = pd.read_csv('patients.csv.gz', compression='gzip', usecols=csv_files['patients'], dtype=str)
patients = patients.merge(filter, how='inner', on=['subject_id'])
patients.to_csv('patients.csv', index=False)
print('patients.csv created.')

datetimeevents = pd.read_csv('datetimeevents.csv.gz', compression='gzip', usecols=csv_files['datetimeevents'], dtype=str)
datetimeevents = datetimeevents.merge(filter, how='inner', on=['subject_id'])
datetimeevents.to_csv('datetimeevents.csv', index=False)
print('datetimeevents.csv created.')

admissions = pd.read_csv('admissions.csv.gz', compression='gzip', usecols=csv_files['admissions'], dtype=str)
admissions = admissions.merge(filter, how='inner', on=['subject_id'])
admissions.to_csv('admissions.csv', index=False)
print('admissions.csv created.')

omr = pd.read_csv('omr.csv.gz', compression='gzip', usecols=csv_files['omr'], dtype=str)
omr = omr.merge(filter, how='inner', on=['subject_id'])
omr.to_csv('omr.csv', index=False)
print('omr.csv created.')

icustays = pd.read_csv('icustays.csv.gz', compression='gzip', usecols=csv_files['icustays'], dtype=str)
icustays = icustays.merge(filter, how='inner', on=['subject_id'])
icustays.to_csv('icustays.csv', index=False)
print('icustays.csv created.')

procedureevents = pd.read_csv('procedureevents.csv.gz', compression='gzip', usecols=csv_files['procedureevents'], dtype=str)
procedureevents = procedureevents.merge(filter, how='inner', on=['subject_id'])
procedureevents.to_csv('procedureevents.csv', index=False)
print('procedureevents.csv created.')

d_labitems = pd.read_csv('d_labitems.csv.gz', compression='gzip', usecols=csv_files['d_labitems'], dtype=str)
d_labitems.to_csv('d_labitems.csv', index=False)
print('d_labitems.csv created.')

d_items = pd.read_csv('d_items.csv.gz', compression='gzip', usecols=csv_files['d_items'], dtype=str)
d_items.to_csv('d_items.csv', index=False)
print('d_items.csv created.')