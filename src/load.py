from typing import Dict


def create_html_table(daily_data: Dict[str, str], mean_rates: Dict[str, float]) -> str:
    html = """<!DOCTYPE html>
<html>
<head>
    <title>ECB Exchange Rates</title>
    <style>
        table {
            border-collapse: collapse;
            width: 60%;
            margin: 50px auto;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #0033a0;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #e6f2ff;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>Currency Code</th>
            <th>Rate</th>
            <th>Mean Historical Rate</th>
        </tr>
"""
    
    for currency in daily_data.keys():
        if currency != 'Date':
            rate = daily_data.get(currency, 'N/A')
            mean_rate = mean_rates.get(currency, 0.0)
            html += f"""        <tr>
            <td>{currency}</td>
            <td>{rate}</td>
            <td>{mean_rate:.4f}</td>
        </tr>
"""
    
    html += """    </table>
</body>
</html>"""
    
    return html


def save_to_file(content: str, filename: str) -> bool:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error saving file: {e}")
        return False