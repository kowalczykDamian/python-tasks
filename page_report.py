import sys
from urllib.parse import urlparse
from collections import Counter
import operator
import re

REGEX = '\d{2}\.\d\.\d{3}\.\d{3}\s[[]\d{2}[/][A-Z][a-z]{2}[/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}\s[+]\d{4}[]]\s["][A-Z]{3}\s(?P<url>https?://[a-z./?=&]+)\s[A-Z]{4}[/]\d\.\d["]\s\d{3}\s\d{4}'

def main():
    logs_list = []

    # read file using context manager
    with open(sys.argv[1], 'r') as file:
        for num, line in enumerate(file, 1):
            if re.search(REGEX, line):
                logs_list.append(line)
            else:
                sys.stderr.write("Invalid log lines: " + str(num) + '\n')

    # parse url from log string
    urls_list = [parse_url(log) for log in logs_list]        

    # count the number of occurrences of each url in urls_list
    num_of_occur = Counter(urls_list)

    # print sorted output
    for k, v in sorted(num_of_occur.items(), key=operator.itemgetter(1), reverse=True):
        print("\"{}\",{}".format(k, v))

def parse_url(log):
    
    # retrieve url using regex group name
    match = re.search(REGEX, log)
    whole_url = match.group('url')

    # clean up url
    parser = urlparse(whole_url)
    url = parser.netloc + parser.path.rstrip('/')

    return url

if __name__ == "__main__":
    main()
