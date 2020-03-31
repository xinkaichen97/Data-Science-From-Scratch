import re
import sys
from collections import Counter

regex = sys.argv[1]  # type test.txt | python 9-sysstd.py "[0-9]"
line_count = 0

try:
    num_words = int(sys.argv[2])
except ValueError:
    print('Usage: python 9-sysstd.py num_words')
    sys.exit(1)

words = []
for line in sys.stdin:
    line_count += 1
    if re.search(regex, line):
        sys.stdout.write(line)
    for word in line.strip().split():
        if word:
            words.append(word.lower())
print('Lines:', line_count)  # same as sys.stdout
counter = Counter(words)
sys.stdout.write('Most common words:\n')
for word, count in counter.most_common(num_words):
    sys.stdout.write(word + '\t' + str(count) + '\n')

