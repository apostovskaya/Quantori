import unittest
from app.script import convert_dna_to_rna


class TestDnaRna(unittest.TestCase):

    def test_standard(self):
        """Test handling of a standard input sequence."""
        given_input = "TATGAAAAACTCAAA"
        expected_output = "UAUGAAAAACUCAAA"
        actual_output = convert_dna_to_rna(given_input)

        self.assertEqual(actual_output, expected_output,
                         f"Expected: {expected_output}")

    def test_empty(self):
        """Tests handling of empty sequence as an input."""
        given_input = ""
        expected_output = ""
        actual_output = convert_dna_to_rna(given_input)

        self.assertEqual(actual_output, expected_output,
                         f"Expected: {expected_output}")

    # @unittest.skip("Not finished, so skip for now.")
    def test_not_string(self):
        # could also test here None, number, sth else
        """Tests handling of a wrong input type - not a string. """
        given_input = ["TATGAAAAACTCAAA", "TATGAAAAACTCAAA"]

        with self.assertRaises(TypeError):
            convert_dna_to_rna(given_input)

    def test_lower_case(self):
        """Tests handling of lower case string of valid DNA seq as an input."""
        given_input = "tatgaaaaactcaaa"
        expected_output = "UAUGAAAAACUCAAA"
        actual_output = convert_dna_to_rna(given_input)

        self.assertEqual(actual_output, expected_output,
                         f"Expected: {expected_output}")

    def test_wrong_base(self):
        """Tests handling of a wrong base in the DNA sequence. """
        given_input = "TATGAAyAACTCAAA"

        with self.assertRaises(KeyError):
            convert_dna_to_rna(given_input)

    def test_wrong_method(self):
        # need to test method=123 as well
        """Tests handling of unsupported method being provided."""
        expected_output = "UAUGAAAAACUCAAA"
        actual_output = convert_dna_to_rna("TATGAAAAACTCAAA",
                                           "transcribe")

        self.assertEqual(actual_output, expected_output,
                         f"Expected: {expected_output}")

    def test_transcription(self):
        """Tests that 'transcription' method works correctly."""
        expected_output = "UAAACCGAUGAUUGUUAGAU"
        actual_output = convert_dna_to_rna("ATTTGGCTACTAACAATCTA",
                                           "transcription")

        self.assertEqual(actual_output, expected_output,
                         f"Expected: {expected_output}")


if __name__ == "__main__":
    unittest.main()
