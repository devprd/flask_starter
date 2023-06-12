import re 

log_entry = '127.0.0.1 - -"GET /image//Tibetan_Mastiff.jpg HTTP/1.1" 404 -' 

# Regular expression pattern to extract relevant information pattern = r'^(\S+) (\S+) (\S+) \[(.*?)\] "(.*?)" (\d+) (\S+)$' # Extracting information using regex matches = re.match(pattern, log_entry) if matches: ip_address = matches.group(1) timestamp = matches.group(4) request_method = matches.group(5) status_code = matches.group(6) print(f'IP Address: {ip_address}') print(f'Timestamp: {timestamp}') print(f'Request Method: {request_method}') print(f'Status Code: {status_code}') else: print("Log entry does not match the expected pattern.")

