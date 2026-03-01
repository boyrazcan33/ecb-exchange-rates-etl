from typing import List, Dict
import requests
import zipfile
import io
import csv


def extract_daily_rates() -> List[Dict[str, str]]:
    """Fetch daily rates from ECB. Returns empty list on failure."""
    url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            csv_filename = z.namelist()[0]
            with z.open(csv_filename) as f:
                content = f.read().decode('utf-8')
                reader = csv.DictReader(io.StringIO(content))
                return list(reader)
                
    except requests.RequestException as e:
        print(f"Error fetching daily rates: {e}")
        return []
    except zipfile.BadZipFile:
        print("Error: Invalid ZIP file received")
        return []
    except Exception as e:
        print(f"Unexpected error in extract_daily_rates: {e}")
        return []


def extract_historical_rates() -> List[Dict[str, str]]:
    """Fetch historical rates from ECB. Returns empty list on failure."""
    url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            csv_filename = z.namelist()[0]
            with z.open(csv_filename) as f:
                content = f.read().decode('utf-8')
                reader = csv.DictReader(io.StringIO(content))
                return list(reader)
                
    except requests.RequestException as e:
        print(f"Error fetching historical rates: {e}")
        return []
    except zipfile.BadZipFile:
        print("Error: Invalid ZIP file received")
        return []
    except Exception as e:
        print(f"Unexpected error in extract_historical_rates: {e}")
        return []