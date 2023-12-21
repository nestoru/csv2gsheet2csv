[![](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=58F9TDDRBND4L)

# CSV to GSheet to CSV
CSV and GSheet ETL through Unix pipes. Pipe CSV into Google Sheets. Pipe/redirect from Google Sheets into CSV.

## Preconditions
* python3
* python-dev
* python-venv
* pip3
```
# install python3 and make it the default
sudo apt-get install -y python3
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
python --version
# install python3 dev and venv packages to use pip effectively in virtual environments
sudo apt-get install -y libpython3-dev python3-venv
# install pip3
sudo apt install -y python3-pip
```
* service account in GCP
* a json key for the service account in GCP
* read/write access (for the GCP service account) to the GDrive Google sheet

## Ubuntu Install example
```
mkdir -p ~/workspace
cd ~/workspace
git clone https://github.com/nestoru/csv2gsheet2csv.git
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
