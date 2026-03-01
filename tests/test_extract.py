from unittest.mock import patch, Mock
import io
import zipfile
from src.extract import extract_daily_rates, extract_historical_rates


def create_mock_zip_response():
    csv_content = "Date, USD, SEK, GBP, JPY\n27 February 2026, 1.1805, 10.6643, 0.8763, 184.13\n"
    
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        zip_file.writestr('eurofxref.csv', csv_content)
    
    zip_buffer.seek(0)
    return zip_buffer.getvalue()


@patch('src.extract.requests.get')
def test_extract_daily_rates_success(mock_get):
    mock_response = Mock()
    mock_response.content = create_mock_zip_response()
    mock_get.return_value = mock_response
    
    result = extract_daily_rates()
    
    assert len(result) == 1
    assert result[0]['Date'] == '27 February 2026'
    assert ' USD' in result[0]


@patch('src.extract.requests.get')
def test_extract_daily_rates_network_error(mock_get):
    mock_get.side_effect = Exception("Network error")
    
    result = extract_daily_rates()
    
    assert result == []


@patch('src.extract.requests.get')
def test_extract_historical_rates_success(mock_get):
    mock_response = Mock()
    mock_response.content = create_mock_zip_response()
    mock_get.return_value = mock_response
    
    result = extract_historical_rates()
    
    assert len(result) == 1
    assert ' USD' in result[0]


@patch('src.extract.requests.get')
def test_extract_bad_zip_file(mock_get):
    mock_response = Mock()
    mock_response.content = b'not a zip file'
    mock_get.return_value = mock_response
    
    result = extract_daily_rates()
    
    assert result == []