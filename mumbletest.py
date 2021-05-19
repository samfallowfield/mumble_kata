import unittest

def mumble_letters(input):
    return '-'.join([x.upper() + x.lower() * i for i, x in enumerate(input)])



class MumbleTests(unittest.TestCase):
    def test_handles_abc_input(self):
        expected_output = "A-Bb-Ccc"
        input = "abC"
        result = mumble_letters(input)

        self.assertEqual(expected_output, result)


    def test_returns_capital_a(self):
        expected_output = "A"
        input = "a"
        result = mumble_letters(input)

        self.assertEqual(expected_output, result)

    
    def test_empty_string_returns_empty_string(self):
        expected_output = ""
        input = ""
        result = mumble_letters(input)

        self.assertEqual(expected_output, result)

    def test_return_full_caps_word_correctly(self):
        expected_output = "Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy"
        input = "QWERTY"
        result = mumble_letters(input)

        self.assertEqual(expected_output, result)

    def test_return_capital_then_lower(self):
        expected_output = "A-Bb-Ccc"
        input = "abC"
        result = mumble_letters(input)

        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    unittest.main()


