#!/usr/bin/env python3
#
# @name: csv2gsheet.py
# @description: extracts CSV content from stdout, transforms it into a Google sheet body request and loads it into a Google sheet tab
# @author: Nestor Urquiza
# @created: 20220215
#

import argparse
import gspread
from pathlib import Path
import sys
from oauth2client.service_account import ServiceAccountCredentials

def csv2gsheet(credentials: Path, sheet_url: str, tab_name: str):

    scope = ['https://spreadsheets.google.com/feeds']
    sa_credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    gs = gspread.authorize(sa_credentials)

    sheet = gs.open_by_url(sheet_url)
    tab = sheet.worksheet(tab_name)
    (firstRow, firstColumn) = gspread.utils.a1_to_rowcol('A1')

    raw_data = sys.stdin.read()
    body1 = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": tab.id,
                    "rowIndex": 0,
                    "columnIndex": 0,
                },
                "data": raw_data,
                "type": 'PASTE_NORMAL',
                "delimiter": ',' 
            }
        }]
    }
    body = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": tab.id,
                    "rowIndex": firstRow - 1,
                    "columnIndex": firstColumn - 1,
                },
                "data": raw_data,
                "type": 'PASTE_NORMAL',
                "delimiter": ',' 
            }
        }]
    }
    tab.clear()
    return sheet.batch_update(body)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--credentials', default=None, help='service account credentials file', required=True)
    ap.add_argument('--sheet_url', default=None, help='sheet url', required=True)
    ap.add_argument('--tab_name', default=None, help="tab name", required=True)
    args = ap.parse_args()

    credentials = args.credentials
    sheet_url = args.sheet_url
    tab_name = args.tab_name

    csv2gsheet(credentials, sheet_url, tab_name) 
