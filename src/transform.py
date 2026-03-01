from typing import List, Dict
from statistics import mean


def filter_currencies(data: List[Dict[str, str]], currencies: List[str]) -> List[Dict[str, str]]:
    filtered = []
    for row in data:
        filtered_row = {'Date': row['Date']}
        for currency in currencies:
            # Handle both with and without leading space
            key = f' {currency}' if f' {currency}' in row else currency
            if key in row:
                filtered_row[currency] = row[key].strip()
        filtered.append(filtered_row)
    return filtered


def calculate_mean_rates(historical_data: List[Dict[str, str]], currencies: List[str]) -> Dict[str, float]:
    means = {}
    
    for currency in currencies:
        values = []
        for row in historical_data:
            # Handle both with and without leading space
            key = f' {currency}' if f' {currency}' in row else currency
            if key in row and row[key] and row[key].strip() and row[key].strip() != 'N/A':
                values.append(float(row[key].strip()))
        if values:
            means[currency] = mean(values)
    
    return means