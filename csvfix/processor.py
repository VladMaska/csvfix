import csv
from statistics import mean

def filter_rows(input_file, output_file, column, op, value):
    ops = {
        'eq': lambda a, b: a == b,
        'ne': lambda a, b: a != b,
        'gt': lambda a, b: float(a) > float(b),
        'lt': lambda a, b: float(a) < float(b),
        'ge': lambda a, b: float(a) >= float(b),
        'le': lambda a, b: float(a) <= float(b),
    }
    if op not in ops:
        raise ValueError(f"Unsupported operation: {op}")
    comp = ops[op]

    with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if comp(row[column], value):
                writer.writerow(row)

def select_columns(input_file, output_file, columns):
    with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=columns)
        writer.writeheader()
        for row in reader:
            filtered = {col: row[col] for col in columns}
            writer.writerow(filtered)

def sort_rows(input_file, output_file, column):
    with open(input_file, newline='') as infile:
        reader = list(csv.DictReader(infile))
    reader.sort(key=lambda x: x[column])
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader[0].keys())
        writer.writeheader()
        writer.writerows(reader)

def column_stats(input_file, column):
    values = []
    with open(input_file, newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            try:
                values.append(float(row[column]))
            except ValueError:
                continue
    if not values:
        return None
    return {
        'count': len(values),
        'mean': mean(values),
        'max': max(values),
        'min': min(values)
    }
