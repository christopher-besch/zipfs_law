import matplotlib.pyplot as plt


# get index with word: occurrences_of_word
def get_words_dict(text):
    # splitting at word breaks
    words_raw = text.split()

    words = {}
    # adding every wordcount to a dict
    for word in words_raw:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    # sort dict by occurrences of words, most go first
    return {key: value for key, value in sorted(words.items(), key=lambda item: item[1], reverse=True)}


# format a line for a table
def format_spaces(string1, string2, total_chars=40, min_spaces=1):
    num_spaces = total_chars - (len(str(string1)) + min_spaces)
    # add spaces if there are too few
    if num_spaces < min_spaces:
        num_spaces = min_spaces

    return str(string1) + " " * num_spaces + str(string2)


if __name__ == "__main__":
    # get cipher from file if unavailable
    input_text = input("paste the text here: ").replace("\n", " ")
    if input_text == '':
        file_location = input("file location: ")
        with open(file_location, encoding='utf-8') as file:
            input_text = file.read().replace("\n", " ")

    # removing useless characters and converting to lowercase
    input_text = ''.join([char for char in input_text if char.isalpha() or char == " "]).lower()

    words_dict = get_words_dict(input_text)

    # create graph
    y_pos = range(0, len(words_dict))
    bars = []
    height = []

    # print and save values to graph
    print(format_spaces("word", "occurrences"))
    for word_str, word_amount in words_dict.items():
        print(format_spaces(word_str, word_amount))
        bars.append(word_str)
        height.append(word_amount)

    # Create bars
    plt.bar(y_pos, height)

    # Create names on the x-axis
    # plt.xticks(y_pos, bars, size=7)
    # rotate labels by 90°
    plt.xticks(rotation='vertical')

    # Show graphic
    plt.show()
