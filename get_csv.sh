#!/bin/bash
url="https://physionet.org/files/mimiciv/2.2"
csvs=(hosp/admissions icu/chartevents icu/d_items icu/datatimeevents
hosp/d_labitems hosp/emar hosp/emar_detail icu/icustays
icu/ingredientevents hosp/labevents hosp/microbiologyevents hosp/omr
hosp/patients hosp/prescriptions icu/procedureevents hosp/transfers)
for csv in ${csvs[@]}; do wget -c -np --user $1 --password $2 $url/$csv.csv.gz; done
