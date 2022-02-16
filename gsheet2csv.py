#!/usr/bin/env python3
#
# @name: gsheet2csv.py
# @description: extracts a Google sheet tab content, transform it into CSV and loads it into the stdin
# @author: Nestor Urquiza
# @created: 20220215
#

import argparse
import csv
import gspread
import Path from pathlib
import sys
import ServiceAccountCredentials from oauth2client.service_account

def gsheet2csv(credentials: Path, sheet_url: str, tab_name: str):

    scope = ['https://spreadsheets.google.com/feeds']
    sa_credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    gs = gspread.authorize(sa_credentials)

    sheet = gs.open_by_url(sheet_url)
    tab = sheet.worksheet(tab_name)

    list_of_list = tab.get_values();
    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(list_of_list)
    #list(map(lambda x: print(*x, sep=','), tab.get_values()))

def hello_world():
    print("Hello world!")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--credentials', default=None, help='service account credentials file', required=True)
    ap.add_argument('--sheet_url', default=None, help='sheet url', required=True)
    ap.add_argument('--tab_name', default=None, help="tab name", required=True)
    args = ap.parse_args()

    credentials = args.credentials
    sheet_url = args.sheet_url
    tab_name = args.tab_name

    gsheet2csv(credentials, sheet_url, tab_name) 
