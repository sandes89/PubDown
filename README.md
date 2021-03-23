# PubDown
Download compounds structure from PubChem based on Names

Requirements
pubchempy >= 1.04
pandas

How to Use the script

> Download the script and create the list of compound names in a csv file and save it as compounds.csv 
> Place the input compound list and script in same folder
> Run the script with command
python retrieve_structures.py

> The compounds with valid names would result in downloaded .sdf files and the ones with invalid names would be dequed and saved in a file.
