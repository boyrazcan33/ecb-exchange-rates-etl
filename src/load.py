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
            html += f"""        <tr>
            <td>{currency}</td>
            <td>{daily_data[currency]}</td>
            <td>{mean_rates[currency]:.4f}</td>
        </tr>
"""
    
    html += """    </table>
</body>
</html>"""
    
    return html


def save_to_file(content: str, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)