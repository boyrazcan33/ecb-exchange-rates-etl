from typing import List, Dict
import requests
import zipfile
import io
import csv


def extract_daily_rates() -> List[Dict[str, str]]:
    url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
    response = requests.get(url)
    
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        csv_filename = z.namelist()[0]
        with z.open(csv_filename) as f:
            content = f.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(content))
            return list(reader)


def extract_historical_rates() -> List[Dict[str, str]]:
    url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"
    response = requests.get(url)
    
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        csv_filename = z.namelist()[0]
        with z.open(csv_filename) as f:
            content = f.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(content))
            return list(reader)