import os
from src.load import create_html_table, save_to_file


def test_create_html_table_basic():
    daily_data = {
        'Date': '27 February 2026',
        'USD': '1.1805',
        'SEK': '10.6643'
    }
    mean_rates = {
        'USD': 1.1823,
        'SEK': 9.6907
    }
    
    html = create_html_table(daily_data, mean_rates)
    
    assert '<!DOCTYPE html>' in html
    assert '<table>' in html
    assert 'USD' in html
    assert '1.1805' in html
    assert '1.1823' in html
    assert 'SEK' in html
    assert '10.6643' in html


def test_create_html_table_excludes_date():
    daily_data = {
        'Date': '27 February 2026',
        'USD': '1.1805'
    }
    mean_rates = {'USD': 1.1823}
    
    html = create_html_table(daily_data, mean_rates)
    
    assert '27 February 2026' not in html


def test_save_to_file_success(tmp_path):
    test_file = tmp_path / "test_output.html"
    content = "<html><body>Test</body></html>"
    
    result = save_to_file(content, str(test_file))
    
    assert result is True
    assert test_file.exists()
    assert test_file.read_text(encoding='utf-8') == content


def test_save_to_file_creates_new_file(tmp_path):
    test_file = tmp_path / "new_file.html"
    content = "<html>Test</html>"
    
    result = save_to_file(content, str(test_file))
    
    assert result is True
    assert test_file.exists()


def test_save_to_file_overwrites_existing(tmp_path):
    test_file = tmp_path / "existing.html"
    test_file.write_text("Old content", encoding='utf-8')
    
    new_content = "<html>New content</html>"
    result = save_to_file(new_content, str(test_file))
    
    assert result is True
    assert test_file.read_text(encoding='utf-8') == new_content