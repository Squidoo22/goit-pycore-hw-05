import sys
from pathlib import Path
import re
from typing import List, Dict, Optional


def parse_log_line(line: str) -> Dict[str, str]:
    pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$'
    match = re.match(pattern, line)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    else:
        raise ValueError(f"Invalid log line format: {line}")


def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []
    path = Path(file_path)
    if not path.exists():
        print(f"Error: '{file_path}' - not found")
        return logs

    with path.open('r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    log_entry = parse_log_line(line)
                    logs.append(log_entry)
                except ValueError as e:
                    print(f"Error parsing line '{line}': {str(e)}")
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    log_counts = {}
    for log in logs:
        level = log["level"]
        log_counts[level] = log_counts.get(level, 0) + 1
    return log_counts


def display_log_counts(counts: Dict[str, int], logs: List[Dict[str, str]], detailed_level: Optional[str] = None):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")

    if detailed_level:
        print(f"\nДеталі логів для рівня '{detailed_level}':")
        filtered_logs = filter_logs_by_level(logs, detailed_level)
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <path_to_log_file> [log_level]")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    parsed_logs = load_logs(log_file)
    log_counts = count_logs_by_level(parsed_logs)
    display_log_counts(log_counts, parsed_logs, detailed_level=log_level)

    # to run this script - python 3.py info.log or python 3.py info.log ERROR
