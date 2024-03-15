# antibiotic resistance prediction
This vanilla version is trained on X test results (table 1) from ICU patients in the MIMIC-IV dataset.
The sample must be taken at least 48 hours after ICU admission

**table 1**
Sample types

|Sample type|Frequency|microbiologyevents.spec_type_desc|
|---|---|---|
|Urine|1,037,970|"URINE"|
|Blood|   |"BLOOD CULTURE",|
|CSF|34,976|"CSF;SPINAL FLUID"|

SEROLOGY/BLOOD
BLOOD
IMMUNOLOGY
Blood (EBV)
Blood (CMV AB)
Immunology (CMV)

**table 2**
CSV files used

|CSV name|module|columns used|variable extracted|
|---|---|---|---|
|[microbiologyevents](https://mimic.mit.edu/docs/iv/modules/hosp/microbiologyevents/)|hosp|'subject_id', 'hadm_id', 'micro_specimen_id', 'chartdate', 'spec_type_desc', 'test_name','org_name', 'ab_name', 'comments','interpretation', 'dilution_text', 'dilution_comparison', 'dilution_value'|"antibiotic"|
|labevents|hosp|||
|d_labitems|hosp|||
|patients|hosp|||
|admissions|hosp|||
|omr|hosp|||
|||||

hosp \n
[transfers]()
[emar]()
[emar_details]()
[pharmacy]()
[prescriptions]()

icu \n
[icustays]() : subject_id hadm_id stay_id first_careunit last_careunit intime outtime los
[d_items]()
[chartevents](https://mimic.mit.edu/docs/iv/modules/icu/chartevents/)
[datetimeevents]()
[Ingredientevents]()
[Inputevents]()
[outputevents](https://mimic.mit.edu/docs/iv/modules/icu/outputevents/)
[procedureevents](https://mimic.mit.edu/docs/iv/modules/icu/procedureevents/)

**table 3**
variables

|variable type|variable name|csv used|
|---|---|---|
|target|antibiotic|microbiologyevents|
|labevents|||
|patients|||
|admissions|||
|omr|||
||||



