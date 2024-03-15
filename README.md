# antibiotic resistance prediction
This vanilla version is trained on X test results (table 1) from ICU patients in the MIMIC-IV dataset.
The sample must be taken at least 48 hours after ICU admission

### table 1
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

### table 2
CSV files used

|CSV name|columns used|variable extracted|
|---|---|---|
|[microbiologyevents](https://mimic.mit.edu/docs/iv/modules/hosp/microbiologyevents)|'subject_id', 'hadm_id', 'micro_specimen_id', 'chartdate', 'spec_type_desc', 'test_name', 'org_name', 'ab_name', 'interpretation', 'comments'|"antibiotic"|
|[labevents](https://mimic.mit.edu/docs/iv/modules/hosp/labevents)|||
|[d_labitems](https://mimic.mit.edu/docs/iv/modules/hosp/d_labitems)|||
|[patients](https://mimic.mit.edu/docs/iv/modules/hosp/patients)|||
|[admissions](https://mimic.mit.edu/docs/iv/modules/hosp/admissions)|||
|[omr](https://mimic.mit.edu/docs/iv/modules/hosp/omr)|||
||||

hosp <br />
[transfers](https://mimic.mit.edu/docs/iv/modules/hosp/omr)
[emar](https://mimic.mit.edu/docs/iv/modules/hosp/omr)
[emar_details](https://mimic.mit.edu/docs/iv/modules/hosp/omr)
[pharmacy](https://mimic.mit.edu/docs/iv/modules/hosp/omr)
[prescriptions](https://mimic.mit.edu/docs/iv/modules/hosp/omr)

icu <br />
[icustays](https://mimic.mit.edu/docs/iv/modules/icu/icustays) : subject_id hadm_id stay_id first_careunit last_careunit intime outtime los
[d_items](https://mimic.mit.edu/docs/iv/modules/icu/d_items)
[chartevents](https://mimic.mit.edu/docs/iv/modules/icu/chartevents)
[datetimeevents](https://mimic.mit.edu/docs/iv/modules/icu/datetimeevents)
[Ingredientevents](https://mimic.mit.edu/docs/iv/modules/icu/Ingredientevents)
[Inputevents](https://mimic.mit.edu/docs/iv/modules/icu/Inputevents)
[outputevents](https://mimic.mit.edu/docs/iv/modules/icu/outputevents)
[procedureevents](https://mimic.mit.edu/docs/iv/modules/icu/procedureevents)

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

