import argparse
from csvfix.processor import filter_rows, select_columns, sort_rows, column_stats

def main():
    parser = argparse.ArgumentParser(description="csvfix - CSV file processor")
    subparsers = parser.add_subparsers(dest="command")

    filter_parser = subparsers.add_parser("filter")
    filter_parser.add_argument("--file", required=True)
    filter_parser.add_argument("--column", required=True)
    filter_parser.add_argument("--op", required=True, choices=["eq", "ne", "gt", "lt", "ge", "le"])
    filter_parser.add_argument("--value", required=True)
    filter_parser.add_argument("--out", required=True)

    select_parser = subparsers.add_parser("select")
    select_parser.add_argument("--file", required=True)
    select_parser.add_argument("--columns", required=True, help="Comma-separated columns")
    select_parser.add_argument("--out", required=True)

    sort_parser = subparsers.add_parser("sort")
    sort_parser.add_argument("--file", required=True)
    sort_parser.add_argument("--column", required=True)
    sort_parser.add_argument("--out", required=True)

    stats_parser = subparsers.add_parser("stats")
    stats_parser.add_argument("--file", required=True)
    stats_parser.add_argument("--column", required=True)

    args = parser.parse_args()

    if args.command == "filter":
        filter_rows(args.file, args.out, args.column, args.op, args.value)
        print(f"Filtered rows saved to {args.out}")
    elif args.command == "select":
        cols = [c.strip() for c in args.columns.split(",")]
        select_columns(args.file, args.out, cols)
        print(f"Selected columns saved to {args.out}")
    elif args.command == "sort":
        sort_rows(args.file, args.out, args.column)
        print(f"Sorted rows saved to {args.out}")
    elif args.command == "stats":
        stats = column_stats(args.file, args.column)
        if stats is None:
            print("No numeric data found in the column.")
        else:
            print(f"Stats for column '{args.column}':")
            print(f" Count: {stats['count']}")
            print(f" Mean: {stats['mean']}")
            print(f" Max: {stats['max']}")
            print(f" Min: {stats['min']}")
    else:
        parser.print_help()
