def longestconsecutive(array, k):

    if (len(array) == 0 or k < 0 or k > len(array)):
        return ""

    else:
        longeststring = ""
        for i in range(len(array)):
            strings = ""
