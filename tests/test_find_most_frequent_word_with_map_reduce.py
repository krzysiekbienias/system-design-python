import unittest

from system_design_python.big_data_processing.find_most_frequent_word_with_map_reduce import (
    MapReduceWordCounter,
)


class MostFrequentWordTest(unittest.TestCase):
    def setUp(self):
        self.counter = MapReduceWordCounter()

    def test_returns_the_only_word(self):
        self.assertEqual(self.counter.mostFrequent(["hello"]), "hello")

    def test_counts_words_across_lines(self):
        lines = ["cat dog", "cat bird", "dog"]
        self.assertEqual(self.counter.mostFrequent(lines), "cat")

    def test_counts_case_insensitively_and_returns_lowercase(self):
        lines = ["Hello", "HELLO world", "hello"]
        self.assertEqual(self.counter.mostFrequent(lines), "hello")

    def test_higher_frequency_wins_over_alphabetical_order(self):
        self.assertEqual(self.counter.mostFrequent(["b b a"]), "b")

    def test_tie_is_broken_by_alphabetical_order(self):
        lines = ["banana apple", "Banana Apple"]
        self.assertEqual(self.counter.mostFrequent(lines), "apple")

    def test_splits_on_whitespace_only(self):
        self.assertEqual(
            self.counter.mostFrequent(["  alpha   beta  alpha  "]),
            "alpha",
        )

    def test_calls_do_not_share_counts(self):
        self.assertEqual(self.counter.mostFrequent(["a a b"]), "a")
        self.assertEqual(self.counter.mostFrequent(["b"]), "b")

    def test_empty_input_raises(self):
        with self.assertRaises(ValueError):
            self.counter.mostFrequent([])

    def test_blank_lines_raise_when_there_are_no_words(self):
        with self.assertRaises(ValueError):
            self.counter.mostFrequent(["", "   "])


if __name__ == "__main__":
    unittest.main()
