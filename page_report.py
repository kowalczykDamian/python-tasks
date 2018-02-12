import sys
from urllib.parse import urlparse
from collections import Counter
import operator

# open file using context manager
with open(sys.argv[1], 'r') as file:
    logs_list = file.readlines()

urls_list = []

# parse url from log
for i in range(0, len(logs_list)):

    split_log = logs_list[i].split('"')
    whole_http_request = split_log[1]

    split_request = whole_http_request.split(' ')
    whole_url = split_request[1]

    parser = urlparse(whole_url)
    url = parser.netloc + parser.path
    url = url.rstrip('/')

    urls_list.append(url)

# count the number of occurrences of each url in urls_list
num_of_url = Counter(urls_list)

# print sorted output
for k, v in sorted(num_of_url.items(), key=operator.itemgetter(1), reverse=True):
    print("\""+k+"\","+str(v))
