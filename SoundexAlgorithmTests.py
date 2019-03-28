import SoundexAlgorithm
import unittest
from unittest.mock import Mock
from SoundexAlgorithm import ISaveData, DataContaioner

class SoundxAlgorithmTests(unittest.TestCase):
    def test_WhenTheWordIsEmptyReturn0000(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("")
        self.assertEqual(encodeword, "0000")

    def test_WhenTheWordIsNoneReturn0000(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode(None)
        self.assertEqual(encodeword, "0000")

    def test_WhenTheWordHaveOneCharThenFillTheWordBy0(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("w")
        self.assertEqual(encodeword, "w000")

    def test_WhenTheWordHaveUpperCaseThenChancgeToLowerCase(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("WASD")
        self.assertEqual(encodeword, "w230")

    def test_WhenTheWordHaveFourCharsWithDifferentNumbersThenReturnEncodedWord(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("bcdm")
        self.assertEqual(encodeword, "b235")

    def test_WhenTheWordHaveMoreThanOneCharAndLessThanFourCharsThenAdd0(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("an")
        self.assertEqual(encodeword, "a500")

    def test_WhenTheWordHaveMoreThanFourCharsThenRemoveRedundantChars(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("anrtzv")
        self.assertEqual(encodeword, "a563")

    def test_WhenTheWordHaveNeighboringCharsWithTheSameNumberThenRemoveAllThisCharsWitchoutFirst(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("accb")
        self.assertEqual(encodeword, "a210")

    def test_WhenTheWordHaveCharsWhichDoNotExistInDictionaryThenRemoveThisChars(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("acob")
        self.assertEqual(encodeword, "a210")

    def test_WhenTheWordHaveSpecialCharsThenReplaceThisCharsTo0(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("!%#&")
        self.assertEqual(encodeword, "0000")

    def test_WhenInTheWordTwoLettersWithTheSameNumberAreSeparatedByWThenEncodeLikeOneNumber(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("bgwjlm")
        self.assertEqual(encodeword, "b245")

    def test_WhenInTheWordTwoLettersWithTheSameNumberAreSeparatedByHThenEncodeLikeOneNumber(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("bghjlm")
        self.assertEqual(encodeword, "b245")

    def test_WhenInTheWordTwoLettersWithTheSameNumberAreSeparatedByVowelThenEncodeTwice(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("bditv")
        self.assertEqual(encodeword, "b331")

    def test_WhentTheWordIsRobertThenReturnR163(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("Robert")
        self.assertEqual(encodeword, "r163")

    def test_WhentTheWordIsRupertThenReturnR163(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("Rupert")
        self.assertEqual(encodeword, "r163")

    def test_WhentTheWordIsRubinThenReturnR150(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("Rubin")
        self.assertEqual(encodeword, "r150")

    def test_WhentTheWordIsAshcraftThenReturnA261(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("Ashcraft")
        self.assertEqual(encodeword, "a261")

    def test_WhentTheWordIsAshcroftThenReturnA261(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("Ashcroft")
        self.assertEqual(encodeword, "a261")

    def test_WhentTheWordIsTymczakThenReturnT522(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("Tymczak")
        self.assertEqual(encodeword, "t522")

    def test_WhentTheWordIsPfisterThenReturnP123(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("Ashcraft")
        self.assertEqual(encodeword, "a261")

    def test_WhentTheWordIsHoneymanThenReturnH555(self):
        soundex = SoundexAlgorithm.SoundexAlgorithm()
        encodeword = soundex.Encode("Honeyman")
        self.assertEqual(encodeword, "h555")

    def test_MockTest(self):
        mock = Mock(spec=ISaveData)
        datacontainer = DataContaioner(mock)
        datacontainer.Save("abcd")
        mock.SaveWord.assert_called_once_with("abcd")

    def test_MockTestvol2(self):
        mock = Mock(spec=ISaveData)
        mock.SaveWord("abcd").return_value = True
        datacontainer = DataContaioner(mock)
        assert datacontainer.Save("abcd") == True