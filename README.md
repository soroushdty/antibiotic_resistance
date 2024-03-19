# Antibiotic Resistance Prediction
This model is trained on X test results (table 1) from ICU patients in the MIMIC-IV dataset.

The sample must be taken at least 48 hours after ICU admission
 

### Table 1: Sample Types

|Type|spec_type_desc|test_name|
|---|---|---|
|Urine|URINE|"URINE CULTURE", "FLUID CULTURE"|
|Blood|BLOOD CULTURE|"Blood Culture, Routine", "AEROBIC BOTTLE", "ANAEROBIC BOTTLE", "ANAEROBIC CULTURE"|

### Table 2: CSV Files

|CSV|columns|class|attributes|
|---|---|---|---|
|[microbiologyevents](https://mimic.mit.edu/docs/iv/modules/hosp/microbiologyevents)|subject_id, hadm_id, micro_specimen_id, chartdate, spec_type_desc, test_name, org_name, ab_name, interpretation, comments|culture|subject, hadm, sampleid, date, fluid, positive, organism, antibiotic, resistant|
|[labevents](https://mimic.mit.edu/docs/iv/modules/hosp/labevents)|subject_id, hadm_id, specimen_id, itemid, charttime, value, valuenum, valueuom, comments||
|[d_labitems](https://mimic.mit.edu/docs/iv/modules/hosp/d_labitems)|itemid, label, fluid|||
|[patients](https://mimic.mit.edu/docs/iv/modules/hosp/patients)|subject_id, gender, anchor_age|||
|[admissions](https://mimic.mit.edu/docs/iv/modules/hosp/admissions)|subject_id, hadm_id, admittime, dischtime, admission_type, admission_location, discharge_location, marital_status, race, hospital_expire_flag||mortality|
|[omr](https://mimic.mit.edu/docs/iv/modules/hosp/omr)|subject_id, chartdate, result_name, result_value|BMI, BP||
|[icustays](https://mimic.mit.edu/docs/iv/modules/icu/icustays)|subject_id, hadm_id, stay_id, intime, outtime, los|*||
|[transfers](https://mimic.mit.edu/docs/iv/modules/hosp/transfers)|subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime|*||
|[chartevents](https://mimic.mit.edu/docs/iv/modules/icu/chartevents)|subject_id, hadm_id, stay_id, charttime, itemid, value, valueuom, lownormalvalue, highnormalvalue|*||
|[d_items](https://mimic.mit.edu/docs/iv/modules/icu/d_items)|itemid, label, linksto, category, unitname|||
|[datetimesevents](https://mimic.mit.edu/docs/iv/modules/icu/datetimesevents)|subject_id, hadm_id, stay_id, charttime, itemid, value|*||
|[ingredientevents](https://mimic.mit.edu/docs/iv/modules/icu/ingredientevents)|subject_id, hadm_id, stay_id, starttime, endtime, itemid, amount, amountuom, rate, rateuom|*||
|[procedureevents](https://mimic.mit.edu/docs/iv/modules/icu/procedureevents)|subject_id, hadm_id, stay_id, starttime, endtime, itemid, value, valueuom, patientweight|*||
|[emar](https://mimic.mit.edu/docs/iv/modules/hosp/emar)|subject_id, hadm_id, emar_id, pharmacy_id, charttime, medication, event_txt|**||
|[emar_detail](https://mimic.mit.edu/docs/iv/modules/hosp/emar_detail)|subject_id, emar_id, administration_type, pharmacy_id, dose_given, dose_given_unit, product_amount_given, product_unit, product_code, product_description, product_description_other, infusion_rate, infusion_rate_unit, route|**||
|[pharmacy](https://mimic.mit.edu/docs/iv/modules/hosp/pharmacy)|subject_id, hadm_id, pharmacy_id, starttime, stoptime, medication, route, frequency, basal_rate, duration, duration_interval|**||
|[prescriptions](https://mimic.mit.edu/docs/iv/modules/hosp/prescriptions)|subject_id, hadm_id, pharmacy_id, starttime, stoptime, drug, gsn, ndc, prod_strength, form_rx, dose_val_rx, dose_unit_rx, route|**||



### Table 3: Variables

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

