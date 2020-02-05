import sys
import matplotlib.pyplot as plt

# get text
if len(sys.argv) < 2:
    # when no file given as argument
    with open(input('Enter file location: '), 'r', encoding='utf8') as file:
        text = file.read()

else:
    with open(sys.argv[1], 'r', encoding='utf8') as file:
        text = file.read()

# removing useless characters and converting to lowercase
text = ''.join([i for i in text if i.isalpha() or i == " "]).lower()
# replacing line breaks
text = text.replace("\n", " ")
# splitting at word breaks
words_raw = text.split()

words = []

# adding every word only once to new list
for word in words_raw:
    if word not in words:
        words.append(word)

# counting amount of every word
words_count = []
for word in words:
    words_count.append([word, words_raw.count(word)])

# create graph
y_pos = range(0, len(words_count))
bars = []
height = []

for word in sorted(words_count, key=lambda l: l[1], reverse=True):
    bars.append(word[0])
    height.append(word[1])

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
# plt.xticks(y_pos, bars, size=7)

# rotate labels by 90°
plt.xticks(rotation='vertical')

for idx, bar in enumerate(bars):
    if idx >= 10:
        break
    print("{}. {}".format(idx + 1, bar))

# Show graphic
plt.show()
