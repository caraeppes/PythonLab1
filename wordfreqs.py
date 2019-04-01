
def long_text_to_list():
    string = open('longtext.txt').read()
    return string.split()


def word_frequency_dict(wordList):
    wordDict = {}
    for word in wordList:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
    return wordDict


def print_250_most_common_words(wordDict):
    sortedDict = sorted(wordDict.items(), key=lambda item: (item[1], item[0]))
    top250 = 0
    print("250 most common words and number of occurrences:")
    while (top250 <= 250):
        print(sortedDict.pop())
        top250 += 1


print_250_most_common_words(word_frequency_dict(long_text_to_list()))
