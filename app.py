import re
import csv

# Regular expression to match log file entries
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'

def parse_log_file(filename, output_filename):
    """
    Parses a log file and writes the extracted data to a CSV file.

    Args:
        filename (str): The name of the log file.
        output_filename (str): The name of the output CSV file.
    """

    with open(filename, 'r') as log_file, open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['remote_addr', 'remote_user', 'time_local', 'request', 'status', 'body_bytes_sent', 'http_referer', 'http_user_agent'])

        for line in log_file:
            match = re.match(log_pattern, line)
            if match:
                data = match.groups()
                writer.writerow(data)

# Example usage:
parse_log_file("your_log_file.txt", "output.csv")