import sys
from src.extract import extract_daily_rates, extract_historical_rates
from src.transform import filter_currencies, calculate_mean_rates
from src.load import create_html_table, save_to_file


def main() -> None:
    """Execute ETL pipeline for ECB exchange rates."""
    try:
        currencies = ['USD', 'SEK', 'GBP', 'JPY']
        
        print("Fetching exchange rates from ECB...")
        daily_rates = extract_daily_rates()
        historical_rates = extract_historical_rates()
        
        if not daily_rates:
            print("Error: Unable to fetch daily rates. Exiting.")
            sys.exit(1)
        
        print("Processing data...")
        filtered_daily = filter_currencies(daily_rates, currencies)
        filtered_historical = filter_currencies(historical_rates, currencies)
        
        mean_rates = calculate_mean_rates(filtered_historical, currencies)
        
        if not filtered_daily:
            print("Error: No data available after filtering. Exiting.")
            sys.exit(1)
        
        latest_daily = filtered_daily[0]
        
        print("Generating HTML output...")
        html_content = create_html_table(latest_daily, mean_rates)
        
        if save_to_file(html_content, 'exchange_rates.html'):
            print("ETL process completed successfully.")
            print("Output saved to exchange_rates.html")
        else:
            print("Error: Failed to save output file.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Critical error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()