import unittest
from app.script import convert_rna_to_protein


class TestRnaProtein(unittest.TestCase):

    def test_standard(self):
        """Test handling of a standard input sequence."""
        given_input = "UAUGAAAAACUCAAA"
        expected_output = "YEKLK"
        actual_output = convert_rna_to_protein(given_input)

        self.assertEqual(actual_output, expected_output,
                         f"Expected: {expected_output}")

    def test_empty(self):
        """Tests handling of empty sequence as an input."""
        given_input = ""
        expected_output = ""
        actual_output = convert_rna_to_protein(given_input)

        self.assertEqual(actual_output, expected_output,
                         f"Expected: {expected_output}")

    def test_not_string(self):
        # could also test here None, number, sth else
        """Tests handling of a wrong input type - not a string. """
        given_input = ["UAUGAAAAACUCAAA", "UAUGAAAAACUCAAA"]

        with self.assertRaises(TypeError):
            convert_rna_to_protein(given_input)

    def test_lower_case(self):
        """Tests handling of lower case string of valid RNA seq as an input."""
        given_input = "UAUGaaaaacucaaa"
        expected_output = "YEKLK"
        actual_output = convert_rna_to_protein(given_input)

        self.assertEqual(actual_output, expected_output,
                         f"Expected: {expected_output}")

    def test_wrong_base(self):
        """Tests handling of a wrong triplet in the RNA sequence. """
        given_input = "UAUGAAAAACU.AAA"

        with self.assertRaises(KeyError):
            convert_rna_to_protein(given_input)


if __name__ == "__main__":
    unittest.main()