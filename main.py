from src.extract import extract_daily_rates, extract_historical_rates
from src.transform import filter_currencies, calculate_mean_rates
from src.load import create_html_table, save_to_file


def main() -> None:
    currencies = ['USD', 'SEK', 'GBP', 'JPY']
    
    daily_rates = extract_daily_rates()
    historical_rates = extract_historical_rates()
    
    filtered_daily = filter_currencies(daily_rates, currencies)
    filtered_historical = filter_currencies(historical_rates, currencies)
    
    mean_rates = calculate_mean_rates(filtered_historical, currencies)
    
    latest_daily = filtered_daily[0]
    
    html_content = create_html_table(latest_daily, mean_rates)
    save_to_file(html_content, 'exchange_rates.html')
    
    print("ETL process completed. Output saved to exchange_rates.html")


if __name__ == "__main__":
    main()