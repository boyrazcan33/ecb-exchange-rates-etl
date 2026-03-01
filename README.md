# ECB Exchange Rates ETL

A simple ETL pipeline that extracts Euro foreign exchange rates from the European Central Bank, transforms the data, and outputs an HTML table.

## Requirements

- Python 3.12+
- See requirements.txt for dependencies

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

**Output:** `exchange_rates.html` will be generated in the project root.

## Project Structure
```
ecb-etl-project/
├── src/
│   ├── extract.py      # Data extraction from ECB APIs
│   ├── transform.py    # Data transformation and calculations
│   └── load.py         # HTML generation and file output
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── main.py             # Main orchestration
├── requirements.txt
└── README.md
```

## Features

- Extracts daily and historical EUR exchange rates from ECB
- Filters USD, SEK, GBP, and JPY currencies
- Calculates historical mean rates
- Generates styled HTML table with hover effects
- Comprehensive error handling for API failures
- Unit tests with pytest

## Running Tests
```bash
pytest tests/ -v
```

## Development Notes

### AI Assistance
Unit tests in the `tests/` directory were created with AI assistance (Claude). AI was also used to format and structure this README file.

During development, I encountered an issue where the filtered data was not appearing in the HTML output. With AI guidance, I used the following diagnostic command to inspect the actual CSV structure:
```bash
python -c "from src.extract import extract_daily_rates; data = extract_daily_rates(); print(data[0])"
```

This revealed that ECB's CSV contains leading spaces in currency column names (e.g., `' USD'` instead of `'USD'`). The AI suggested handling both formats in the code:
```python
key = f' {currency}' if f' {currency}' in row else currency
```

This debugging approach and the defensive coding pattern were suggested by AI. The core ETL implementation was developed independently.