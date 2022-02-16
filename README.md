# CSV to GSheet to CSV
CSV and GSheet ETL through Unix pipes. Pipe CSV into Google Sheets. Pipe/redirect from Google Sheets into CSV.

## Preconditions
* python3
* pip3
* python-dev
* python-venv
* service account in GCP
* a json key for the service account in GCP
* read/write access (for the GCP service account) to the GDrive Google sheet

## Ubuntu Install example
```
mkdir -p ~/workspace
cd ~/workspace
git clone csv2gsheet2csv
cd csv2gsheet2csv
pip install virtualenv
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Help
```
cd ~/workspace/csv2gsheet2csv
python gsheet2csv.py
python csv2gsheet.py
```

## Running examples
* pipe the content of my_raw_data.csv into csv2gsheet.py
* pass the location of the GCP service account credentials file (json key)
* pass the url to the Google sheet identified gy its ${gsheetId}in GDrive
* pass the name of the tab in the sheet
```
cat my_raw_data.csv | \
  python csv2gsheet.py \
    --credentials gcp-service-account-credentials.json \
    --sheet_url https://docs.google.com/spreadsheets/d/${gsheetId} \
    --tab_name my_raw_data_in_gsheet
```
* redirect the content of the same sheet into a new local csv file
```
python gsheet2csv.py \
  --credentials gcp-service-account-credentials.json \
  --sheet_url https://docs.google.com/spreadsheets/d/${gsheetId} \
  --tab_name my_raw_data_in_gsheet > copy_of_my_raw_data.csv
```
