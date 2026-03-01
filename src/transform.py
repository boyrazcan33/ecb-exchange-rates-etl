from typing import List, Dict
from statistics import mean, StatisticsError


def filter_currencies(data: List[Dict[str, str]], currencies: List[str]) -> List[Dict[str, str]]:
    """Filter data to include only specified currencies."""
    if not data:
        print("Warning: No data to filter")
        return []
    
    filtered = []
    for row in data:
        filtered_row = {'Date': row.get('Date', '')}
        for currency in currencies:
            key = f' {currency}' if f' {currency}' in row else currency
            if key in row:
                filtered_row[currency] = row[key].strip()
        filtered.append(filtered_row)
    
    return filtered


def calculate_mean_rates(historical_data: List[Dict[str, str]], currencies: List[str]) -> Dict[str, float]:
    """
    Calculate arithmetic mean for each currency, skipping N/A values.
    Returns 0.0 for currencies with no valid data.
    """
    if not historical_data:
        print("Warning: No historical data available for mean calculation")
        return {currency: 0.0 for currency in currencies}
    
    means = {}
    
    for currency in currencies:
        values = []
        for row in historical_data:
            key = f' {currency}' if f' {currency}' in row else currency
            if key in row and row[key] and row[key].strip() and row[key].strip() != 'N/A':
                try:
                    values.append(float(row[key].strip()))
                except ValueError:
                    continue
        
        if values:
            try:
                means[currency] = mean(values)
            except StatisticsError:
                print(f"Warning: Could not calculate mean for {currency}")
                means[currency] = 0.0
        else:
            print(f"Warning: No valid data found for {currency}")
            means[currency] = 0.0
    
    return means