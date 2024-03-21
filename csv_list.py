csv_files = {
'microbiologyevents':['subject_id', 'hadm_id', 'micro_specimen_id', 'chartdate', 'spec_type_desc', 'test_name', 'org_name', 'ab_name', 'interpretation', 'comments'],
'labevents':['subject_id', 'hadm_id', 'specimen_id', 'itemid', 'charttime', 'value', 'valuenum', 'valueuom', 'comments'],
'emar':['subject_id', 'hadm_id', 'emar_id','pharmacy_id', 'charttime', 'medication', 'event_txt'],
'emar_detail':['subject_id', 'emar_id', 'administration_type', 'pharmacy_id', 'dose_given', 'dose_given_unit', 'product_amount_given', 'product_unit', 'product_code', 'product_description', 'product_description_other', 'infusion_rate', 'infusion_rate_unit', 'route'],
'chartevents':['subject_id', 'hadm_id', 'stay_id', 'charttime', 'itemid', 'value', 'valueuom'],
'prescriptions':['subject_id', 'hadm_id', 'pharmacy_id','starttime', 'stoptime', 'drug', 'gsn', 'ndc', 'prod_strength', 'form_rx', 'dose_val_rx', 'dose_unit_rx', 'route'],
'pharmacy':['subject_id', 'hadm_id', 'pharmacy_id','starttime', 'stoptime', 'medication', 'route', 'frequency', 'basal_rate', 'duration', 'duration_interval'],
'patients':['subject_id', 'gender', 'anchor_age'],
'datetimeevents':['subject_id', 'hadm_id', 'stay_id', 'charttime', 'itemid', 'value'],
'admissions':['subject_id', 'hadm_id', 'admittime', 'dischtime', 'admission_type','admission_location', 'discharge_location', 'marital_status', 'race', 'hospital_expire_flag'],
'omr':['subject_id', 'chartdate', 'result_name', 'result_value'],
'icustays':['subject_id', 'hadm_id', 'stay_id', 'intime', 'outtime', 'los'],
'd_labitems':['itemid', 'label', 'fluid'],
'd_items':['itemid', 'label', 'linksto', 'category', 'unitname'],
'ingredientevents':['subject_id', 'hadm_id', 'stay_id', 'starttime', 'endtime', 'itemid', 'amount', 'amountuom', 'rate', 'rateuom'],
'procedureevents':['subject_id', 'hadm_id', 'stay_id', 'starttime', 'endtime', 'itemid', 'value', 'valueuom', 'patientweight'],
'transfers':['subject_id', 'hadm_id', 'transfer_id', 'eventtype', 'careunit', 'intime', 'outtime']
}


comments = {
'blood_negative':[
    'GRAM NEGATIVE ROD(S).',
    'GRAM POSITIVE COCCI IN CLUSTERS.',
    'GRAM POSITIVE COCCI IN PAIRS AND CHAINS.',
    'GRAM POSITIVE COCCI IN PAIRS AND CLUSTERS.',
    'GRAM POSITIVE COCCI IN CHAINS.',
    'GRAM POSITIVE COCCI. IN PAIRS AND CLUSTERS.',
    'BUDDING YEAST.',
    'GRAM POSITIVE COCCI. IN PAIRS AND CHAINS.',
    'GRAM POSITIVE ROD(S).',
    'TEST CANCELLED, PATIENT CREDITED.',
    'HBV DNA detected, less than 40 IU/mL. Performed using the ___ HBV Test. Linear range of quantification: 40 IU/mL - 110million IU/mL. Limit of detection: 10 IU/mL.'],

'urine_negative':[
    'MIXED BACTERIAL FLORA ( >= 3 COLONY TYPES), CONSISTENT WITH SKIN AND/OR GENITAL CONTAMINATION.',
    'MIXED BACTERIAL FLORA ( >= 3 COLONY TYPES), CONSISTENT WITH FECAL CONTAMINATION.',
    'Culture workup discontinued. Further incubation showed contamination with mixed skin/genital flora. Clinical significance of isolate(s) uncertain. Interpret with caution.',
    'Culture workup discontinued. Further incubation showed contamination with mixed fecal flora. Clinical significance of isolate(s) uncertain. Interpret with caution.',
    'Due to mixed bacterial types ( >= 3 colony types) an abbreviated workup is performed (including a screen for Pseudomonas aeruginosa, Staphylococcus aureus and beta streptococcus).',
    'TEST CANCELLED, PATIENT CREDITED.',
    'Due to mixed bacterial types (>=3) an abbreviated workup is performed; P.aeruginosa, S.aureus and beta strep. are reported if present. Susceptibility will be performed on P.aeruginosa and S.aureus if sparse growth or greater.',
    'MIXED BACTERIAL FLORA ( >= 3 COLONY TYPES), CONSISTENT WITH SKIN AND/OR GENITAL CONTAMINATION. INTERPRET RESULTS WITH CAUTION.',
    'BUDDING YEAST.',
    'Test cancelled by laboratory. PATIENT CREDITED. if pulmonary Histoplasmosis, Coccidioidomycosis, Blastomycosis, Aspergillosis or Mucormycosis is strongly suspected, contact the Microbiology Laboratory (___).',
    'UNABLE TO R/O OTHER PATHOGENS DUE TO OVERGROWTH OF SWARMING PROTEUS SPP.'],

'urine_positive':
    ['Culture workup discontinued. Further incubation showed contamination with mixed skin/genital flora. Clinical significance of isolate(s) uncertain. Interpret with caution.',
    'MIXED BACTERIAL FLORA ( >= 3 COLONY TYPES), CONSISTENT WITH SKIN AND/OR GENITAL CONTAMINATION.',
    'Culture workup discontinued. Further incubation showed contamination with mixed fecal flora. Clinical significance of isolate(s) uncertain. Interpret with caution.',
    'MIXED BACTERIAL FLORA ( >= 3 COLONY TYPES), CONSISTENT WITH FECAL CONTAMINATION.',
    'MIXED BACTERIAL FLORA ( >= 3 COLONY TYPES), CONSISTENT WITH SKIN AND/OR GENITAL CONTAMINATION. INTERPRET RESULTS WITH CAUTION.',
    '<10,000 organisms/ml.']}
