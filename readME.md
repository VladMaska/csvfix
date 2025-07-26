# csvfix

📊 **csvfix** is a lightweight Python CLI utility for quick processing of CSV files

---

## Features

- Filter rows by column value with operators (eq, ne, gt, lt, ge, le)  
- Select and reorder columns  
- Sort rows by column  
- Compute basic statistics (count, mean, max, min) on numeric columns  

---

## Installation

```bash
git clone https://github.com/your-username/csvfix.git
cd csvfix
```

---

## Usage

```bash
# Filter rows where 'age' > 30
python main.py filter --file data.csv --column age --op gt --value 30 --out filtered.csv

# Select columns 'name' and 'email'
python main.py select --file data.csv --columns name,email --out selected.csv

# Sort rows by 'date'
python main.py sort --file data.csv --column date --out sorted.csv

# Show stats for 'salary'
python main.py stats --file data.csv --column salary
```

---

## Project Structure

```bash
csvfix/
├── main.py
├── cli.py
├── csvfix/
│   ├── __init__.py
│   └── processor.py
├── README.md
└── LICENSE

```