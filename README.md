# Antibiotic Resistance Prediction
This vanilla version is trained on X test results (table 1) from ICU patients in the MIMIC-IV dataset.

Microorganisms with at least 1000 cultures with at least 100 results for each antibiotic are included.


The sample must be taken at least 48 hours after ICU admission
 

### Table 1: Sample Types

|Type|Frequency|spec_type_desc|test_name|
|---|---|---|---|
|Urine|535,226|URINE|"URINE CULTURE", "FLUID CULTURE"|
|Blood|91,516|BLOOD CULTURE|"Blood Culture, Routine", "AEROBIC BOTTLE", "ANAEROBIC BOTTLE", "ANAEROBIC CULTURE"|

### table 2: CSV Files

|CSV|columns|class|attributes|
|---|---|---|---|
|[microbiologyevents](https://mimic.mit.edu/docs/iv/modules/hosp/microbiologyevents)|subject_id, hadm_id, micro_specimen_id, chartdate, spec_type_desc, test_name, org_name, ab_name, interpretation, comments|culture|subject, hadm, sampleid, date, fluid, positive, organism, antibiotic, resistant|
|[labevents](https://mimic.mit.edu/docs/iv/modules/hosp/labevents)|subject_id, hadm_id, specimen_id, itemid, charttime, value, valuenum, valueuom, comments||
|[d_labitems](https://mimic.mit.edu/docs/iv/modules/hosp/d_labitems)|itemid, label, fluid|||
|[patients](https://mimic.mit.edu/docs/iv/modules/hosp/patients)|subject_id, gender, anchor_age|||
|[admissions](https://mimic.mit.edu/docs/iv/modules/hosp/admissions)|subject_id, hadm_id, admittime, dischtime, admission_type, admission_location, discharge_location, marital_status, race, hospital_expire_flag||mortality|
|[omr](https://mimic.mit.edu/docs/iv/modules/hosp/omr)|subject_id, chartdate, result_name, result_value|BMI, BP||
|[icustays](https://mimic.mit.edu/docs/iv/modules/icu/icustays)|subject_id, hadm_id, stay_id, intime, outtime, los|||
|[transfers](https://mimic.mit.edu/docs/iv/modules/hosp/transfers)|subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime|||
|[chartevents](https://mimic.mit.edu/docs/iv/modules/icu/chartevents)||||
|[d_items](https://mimic.mit.edu/docs/iv/modules/icu/d_items)||||
|[datetimesevents](https://mimic.mit.edu/docs/iv/modules/icu/datetimesevents)|subject_id, hadm_id, stay_id, charttime, itemid, value|||
|||||
|||||


MEDICATION <br />
[emar](https://mimic.mit.edu/docs/iv/modules/hosp/emar)
[emar_details](https://mimic.mit.edu/docs/iv/modules/hosp/emar_details)
[pharmacy](https://mimic.mit.edu/docs/iv/modules/hosp/pharmacy)
[prescriptions](https://mimic.mit.edu/docs/iv/modules/hosp/prescriptions)
[ingredientevents](https://mimic.mit.edu/docs/iv/modules/icu/ingredientevents)
[inputevents](https://mimic.mit.edu/docs/iv/modules/icu/inputevents)

IV FLUIDS
[ingredientevents](https://mimic.mit.edu/docs/iv/modules/icu/ingredientevents)
[inputevents](https://mimic.mit.edu/docs/iv/modules/icu/inputevents)


### table 3
variables

|variable type|variable name|csv used|
|---|---|---|
|target|antibiotic|microbiologyevents|
|labevents|||
|patients|||
|admissions|||
|omr|||
||||


### MIMIC-IV reference
[physionet dataset](https://physionet.org/content/mimiciv/2.2/) <br />
[article](https://www.nature.com/articles/s41597-022-01899-x)

