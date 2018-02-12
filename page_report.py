import sys
from urllib.parse import urlparse
from collections import Counter
import operator
import re

pattern = re.compile(r'\d{2}\.\d\.\d{3}\.\d{3}\s[[]\d{2}[/][A-Z][a-z]{2}[/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}\s[+]\d{4}[]]\s["][A-Z]{3}\s(https?://[a-z./?=&]+)\s[A-Z]{4}[/]\d\.\d["]\s\d{3}\s\d{4}')
logs_list = []
urls_list = []

# read file using context manager
with open(sys.argv[1], 'r') as file:
    for num, line in enumerate(file, 1):
        if pattern.match(line):
            logs_list.append(line)
        else:
            sys.stderr.write("Invalid log lines: " + str(num) + '\n')

# parse url from log
for log in logs_list:

    # get first group from regex pattern
    whole_url = pattern.sub(r'\1', log).rstrip('\n')        

    parser = urlparse(whole_url)
    url = parser.netloc + parser.path
    url = url.rstrip('/')

    urls_list.append(url)

# count the number of occurrences of each url in urls_list
num_of_url = Counter(urls_list)

# print sorted output
for k, v in sorted(num_of_url.items(), key=operator.itemgetter(1), reverse=True):
    print("\"" + k + "\"," + str(v))
