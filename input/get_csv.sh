#!/bin/bash

url="https://physionet.org/files/mimiciv/2.2"

csvs=(hosp/admissions icu/chartevents icu/d_items icu/datetimeevents
hosp/d_labitems hosp/emar hosp/emar_detail icu/icustays hosp/pharmacy
icu/ingredientevents hosp/labevents hosp/microbiologyevents hosp/omr
hosp/patients hosp/prescriptions icu/procedureevents hosp/transfers)

# Save csv.gz files
for csv in ${csvs[@]}; do wget -c -np --user $1 --password $2 $url/$csv.csv.gz; done

# Count rows of large files
declare -A nrows
for i in "labevents" "emar" "emar_detail" "chartevents" "prescriptions" "pharmacy" "ingredientevents"
do echo counting rows in "$i.csv.gz" && nrows["$i"]=$(zgrep -c $ "$i.csv.gz") && echo Done!; done

keys=("${!nrows[@]}")
last_key=${keys[@]:(-1)}

# Export hashtable as JSON
printf "{\n" > nrows.json
for key in "${!nrows[@]}"; do
    printf "\"%s\":\"%s\"" "$key" "${nrows[$key]}" >> nrows.json
    if [[ $key != $last_key ]]; then
        printf ",\n" >> nrows.json
    fi
done
printf "\n}" >> nrows.json
echo "Number of rows exported to JSON"

echo "Executing data_acquisition.py"
python data_acquisition.py

read -p "Do you want to delete all unnecessary files? (y/n): " answer

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    rm *.csv.gz
    rm nrows.json
    echo "Files deleted."
    
elif [[ "$answer" == "n" || "$answer" == "N" ]]; then
    echo "Deletion canceled."
else
    echo "Invalid input. Please enter y for Yes, or n for No."
fi