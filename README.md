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

Output will be saved to `exchange_rates.html`

## Project Structure
```
ecb-etl-project/
├── src/
│   ├── extract.py      # Data extraction from ECB APIs
│   ├── transform.py    # Data transformation and calculations
│   └── load.py         # HTML generation and file output
├── main.py             # Main orchestration
├── requirements.txt
└── README.md
```

## Features

- Extracts daily and historical EUR exchange rates from ECB
- Filters USD, SEK, GBP, and JPY currencies
- Calculates historical mean rates
- Generates styled HTML table