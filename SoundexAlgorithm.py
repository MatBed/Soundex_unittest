import SoundexData
import itertools
import string

class SoundexAlgorithm():

    def Encode(self, word = ""):
        invalidChars = set(string.punctuation)

        if word == "":
            return "0000"
        if word is None:
            return "0000"
        if any(char in invalidChars for char in word):
            return "0000"


        lowerCaseWord = word.lower()
        encodedWord = SoundexAlgorithm.EncodeWord(SoundexAlgorithm, lowerCaseWord)
        trimWord = SoundexAlgorithm.TrimString(SoundexAlgorithm, encodedWord)

        return trimWord

    def TrimString(self, word):
        if len(word) > 4:
            word = word[0:4]
        elif len(word) < 4:
            while len(word) < 4:
                word += "0"
        return word

    def EncodeWord(self, word):
        i = 0
        encodedWord = ""
        encodedWord += word[0]

        for char in word:
            if i == 0:
                i += 1
                continue

            if (i > 1 and (word[i-1] == "w" or word[i-1] == "h") and SoundexAlgorithm.AreTwoCharsWithTheSameNumber(SoundexAlgorithm, word[i-2], word[i])):
                i += 1
                continue

            elif char in SoundexData.charToNumber.keys():
                encodedWord += SoundexData.charToNumber.get(char)
                if(SoundexAlgorithm.AreTwoCharsWithTheSameNumber(SoundexAlgorithm, word[i], word[i-1]) and i > 1):
                    encodedWord = SoundexAlgorithm.RemoveDuplicatedChars(SoundexAlgorithm, encodedWord)

            elif (SoundexAlgorithm.AreTwoCharsWithTheSameNumber(SoundexAlgorithm, word[i - 1], word[i + 1]) and (word[i] == "w" or word[i] == "h")) or SoundexAlgorithm.AreTwoCharsWithTheSameNumber(SoundexAlgorithm, word[i], word[i + 1]) and i > word.Length - 1:
                encodedWord = SoundexAlgorithm.RemoveDuplicatedChars(SoundexAlgorithm, encodedWord)


            i += 1

        return encodedWord

    def RemoveDuplicatedChars(self, word):
        withoutDuplicated = ''.join(ch for ch, _ in itertools.groupby(word))
        return withoutDuplicated


    def AreTwoCharsWithTheSameNumber(self, firstChar, secondChar):
        if firstChar in SoundexData.charToNumber.keys() and secondChar in SoundexData.charToNumber.keys():
            valueOfFirstChar = SoundexData.charToNumber.get(firstChar)
            valueOfSecondChar = SoundexData.charToNumber.get(secondChar)

            if valueOfFirstChar == valueOfSecondChar:
                return True

        return False
