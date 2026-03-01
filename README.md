# ECB Exchange Rates ETL

A simple ETL pipeline that extracts Euro foreign exchange rates from the European Central Bank, transforms the data, and outputs an HTML table.

## Requirements

- Python 3.12+
- See requirements.txt for dependencies

## ⚡ Quick Start
```bash
# Clone the repository
git clone https://github.com/boyrazcan33/ecb-exchange-rates-etl.git
cd ecb-exchange-rates-etl

# Install dependencies
pip install -r requirements.txt

# Run the ETL pipeline
python main.py
```

**➡️ Output file:** `exchange_rates.html` (generated in project root)

## Running Tests
```bash
pytest tests/ -v
```

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

## Sample Output

The program generates an HTML table with the following format:

| Currency Code | Rate    | Mean Historical Rate |
|---------------|---------|---------------------|
| USD           | 1.1805  | 1.1823              |
| SEK           | 10.6643 | 9.6907              |
| GBP           | 0.87630 | 0.7849              |
| JPY           | 184.13  | 131.6950            |

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