#!/usr/bin/python3
import sys
from collections import Counter

total_size = 0
status_counts = Counter()
line_count = 0


def print_stats():
    global total_size, status_counts
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")


try:
    for line in sys.stdin:
        line_count += 1
        # Split line based on spaces
        fields = line.strip().split()

        # Check format: IP, date (optional), method, path, protocol, status, size
        if len(fields) >= 7 and fields[2] == 'GET' and fields[4] == 'HTTP/1.1':
            try:
                status_code = int(fields[5])
                file_size = int(fields[6])
                total_size += file_size
                status_counts[status_code] += 1
            except ValueError:
                pass  # Skip lines with invalid status or size

        # Print after 10 lines or keyboard interrupt
        if line_count % 10 == 0 or line_count == 1:
            print_stats()
            status_counts = Counter()  # Reset counts for next block

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
