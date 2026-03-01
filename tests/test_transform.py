from src.transform import filter_currencies, calculate_mean_rates


def test_filter_currencies_basic():
    data = [
        {'Date': '27 Feb 2026', ' USD': ' 1.1805', ' EUR': ' 1.0', ' SEK': ' 10.66'}
    ]
    currencies = ['USD', 'SEK']
    
    result = filter_currencies(data, currencies)
    
    assert len(result) == 1
    assert 'USD' in result[0]
    assert 'SEK' in result[0]
    assert 'EUR' not in result[0]
    assert result[0]['USD'] == '1.1805'


def test_filter_currencies_with_leading_space():
    data = [
        {'Date': '27 Feb 2026', ' USD': ' 1.1805', ' JPY': ' 184.13'}
    ]
    currencies = ['USD', 'JPY']
    
    result = filter_currencies(data, currencies)
    
    assert result[0]['USD'] == '1.1805'
    assert result[0]['JPY'] == '184.13'


def test_filter_currencies_empty_data():
    result = filter_currencies([], ['USD'])
    
    assert result == []


def test_calculate_mean_rates_basic():
    data = [
        {'Date': '2026-03-01', ' USD': ' 1.20'},
        {'Date': '2026-02-28', ' USD': ' 1.18'},
        {'Date': '2026-02-27', ' USD': ' 1.16'}
    ]
    currencies = ['USD']
    
    result = calculate_mean_rates(data, currencies)
    
    assert 'USD' in result
    assert result['USD'] == (1.20 + 1.18 + 1.16) / 3


def test_calculate_mean_rates_with_na():
    data = [
        {'Date': '2026-03-01', ' USD': ' 1.20'},
        {'Date': '2026-02-28', ' USD': ' N/A'},
        {'Date': '2026-02-27', ' USD': ' 1.16'}
    ]
    currencies = ['USD']
    
    result = calculate_mean_rates(data, currencies)
    
    assert result['USD'] == (1.20 + 1.16) / 2


def test_calculate_mean_rates_empty_data():
    result = calculate_mean_rates([], ['USD'])
    
    assert result == {'USD': 0.0}


def test_calculate_mean_rates_all_na():
    data = [
        {'Date': '2026-03-01', ' USD': ' N/A'},
        {'Date': '2026-02-28', ' USD': ' N/A'}
    ]
    currencies = ['USD']
    
    result = calculate_mean_rates(data, currencies)
    
    assert result['USD'] == 0.0