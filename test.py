import unittest
import os
import script
import csv

class TestScript(unittest.TestCase):

    def setUp(self):
        """
        This method will be called before each test.
        It sets up the audio directory and a sample filename.
        """

        # This method will be called before each test
        self.audio_dir = "audio"

    def test_get_total_files(self):
        """
        Tests if the total number of files in the directory is correct.
        """

        # Test if the total number of files in the directory is correct
        self.assertEqual(script.get_total_files(self.audio_dir), len([name for name in os.listdir(self.audio_dir) if name.endswith(".wav")]))

    def test_get_audio_in_array_format_int_1(self):
        """
        Tests if the function correctly converts a string of digits into an array of integers.
        """
        
        sample_text = "13247810"
        expected_output = [1, 3, 2, 4, 7, 8, 10]
        self.assertEqual(script.get_audio_in_array_format_int(sample_text), expected_output)

    def test_get_audio_in_array_format_int_2(self):
        """
        Tests if the function correctly converts a different string of digits into an array of integers.
        """
        sample_text = "12347610"
        expected_output = [1, 2, 3, 4, 7, 6, 10]
        self.assertEqual(script.get_audio_in_array_format_int(sample_text), expected_output)

    def test_get_audio_in_array_format_int_3(self):
        """
        Tests if the function correctly converts a different string of digits into an array of integers.
        """

        sample_text = "12345678910"
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(script.get_audio_in_array_format_int(sample_text), expected_output)

    def test_get_audio_in_array_format_int_4(self):
        """
        Tests if the function correctly converts a different string of digits into an array of integers.
        """

        sample_text = "12310"
        expected_output = [1, 2, 3, 10]
        self.assertEqual(script.get_audio_in_array_format_int(sample_text), expected_output)

    def test_get_audio_in_array_format_int_5(self):
        """
        Tests if the function correctly converts a different string of digits into an array of integers.
        """

        sample_text = "121035"
        expected_output = [1, 2, 10, 3, 5]
        self.assertEqual(script.get_audio_in_array_format_int(sample_text), expected_output)

    def test_get_audio_in_array_format_int_input_not_string(self):
        """
        Tests if the function raises a ValueError when the input is not a string.
        """

        sample_input = 12345678910
        self.assertRaises(ValueError, script.get_audio_in_array_format_int, sample_input)

    def test_get_audio_in_array_format_int_input_contains_non_digits(self):
        """
        Tests if the function raises a ValueError when the input string contains non-digit characters.
        """

        sample_input = "1234abc5678910"
        self.assertRaises(ValueError, script.get_audio_in_array_format_int, sample_input)

    def test_get_audio_in_array_format_int_input_invalid_format(self):
        """
        Tests if the function raises a ValueError when the input string is not in the expected format.
        """

        sample_input = "123 456 789 10"
        self.assertRaises(ValueError, script.get_audio_in_array_format_int, sample_input)

    def test_get_timestamp_1(self):
        """
        Tests if the timestamp extraction from filename is working correctly where the filename is in the format "date time.wav".
        """

        sample_filename = "12-25-2020 10-30-15.wav"
        expected_output = "2020-12-25T10:30:15"
        self.assertEqual(script.get_timestamp(sample_filename), expected_output)

    def test_get_timestamp_2(self):
        """
        Tests if the timestamp extraction from filename is working correctly where the filename is in the format "date time.wav".
        """

        sample_filename = "01-01-2022 00-00-00.wav"
        expected_output = "2022-01-01T00:00:00"
        self.assertEqual(script.get_timestamp(sample_filename), expected_output)


    def test_get_timestamp_3(self):
        """
        Tests if the timestamp extraction from filename is working correctly where the filename is in the format "date time.wav".
        """

        sample_filename = "09-30-2021 03-12-31.wav"
        expected_output = "2021-09-30T03:12:31"
        self.assertEqual(script.get_timestamp(sample_filename), expected_output)

    def test_get_timestamp_invalid_format_1(self):
        """
        Tests if the function raises a ValueError when the filename is not in the expected format.
        """

        sample_filename = "invalid_format.wav"
        self.assertRaises(ValueError, script.get_timestamp, sample_filename)

    def test_get_timestamp_invalid_format_2(self):
        """
        Tests if the function raises a ValueError when the filename is not in the expected format.
        """

        sample_filename = "no_date.wav"
        self.assertRaises(ValueError, script.get_timestamp, sample_filename)

    def test_get_timestamp_invalid_format_3(self):
        """
        Tests if the function raises a ValueError when the filename is not in the expected format.
        """

        sample_filename = "wrong_format_01-01-2022.wav"
        self.assertRaises(ValueError, script.get_timestamp, sample_filename)

    def test_find_longest_consecutive_count_and_order_1(self):
        """
        Tests if the function is correctly finding the longest consecutive count and order.
        """

        sample_input = [1, 2, 3, 1, 2]
        expected_output = (3, True)
        self.assertEqual(script.find_longest_consecutive_count_and_order(sample_input), expected_output)

    def test_find_longest_consecutive_count_and_order_2(self):
        """
        Tests if the function is correctly finding the longest consecutive count and order.
        """

        sample_input = [1, 2, 3, 4, 5]
        expected_output = (5, False)
        self.assertEqual(script.find_longest_consecutive_count_and_order(sample_input), expected_output)

    def test_find_longest_consecutive_count_and_order_3(self):
        """
        Tests if the function is correctly finding the longest consecutive count and order.
        """

        sample_input = [5, 4, 3, 2, 1]
        expected_output = (1, True)
        self.assertEqual(script.find_longest_consecutive_count_and_order(sample_input), expected_output)

    def test_find_longest_consecutive_count_and_order_4(self):
        """
        Tests if the function is correctly finding the longest consecutive count and order.
        """

        sample_input = [1, 3, 5, 7, 9]
        expected_output = (1, False)
        self.assertEqual(script.find_longest_consecutive_count_and_order(sample_input), expected_output)

    def test_find_longest_consecutive_count_and_order_5(self):
        """
        Tests if the function is correctly finding the longest consecutive count and order.
        """

        sample_input = [2, 2, 2, 2, 2]
        expected_output = (1, False)
        self.assertEqual(script.find_longest_consecutive_count_and_order(sample_input), expected_output)

    def test_find_longest_consecutive_count_and_order_value_error_1(self):
        """
        Tests if the function raises ValueError when input is not an array of integers.
        """

        sample_input = ['1', '2', '3', '4', '5']
        self.assertRaises(ValueError, script.find_longest_consecutive_count_and_order, sample_input)

    def test_find_longest_consecutive_count_and_order_value_error_2(self):
        """
        Tests if the function raises ValueError when input is an empty list.
        """

        sample_input = []
        self.assertRaises(ValueError, script.find_longest_consecutive_count_and_order, sample_input)

    def test_find_longest_consecutive_count_and_order_value_error_3(self):
        """
        Tests if the function raises ValueError when input is not a list.
        """

        sample_input = "12345"
        self.assertRaises(ValueError, script.find_longest_consecutive_count_and_order, sample_input)

    def test_write_row_to_csv_1(self):
        """
        Tests if the function correctly writes a row to the CSV file.
        """

        with open("test_output.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
            filename = "sample.wav"
            timestamp_iso8601 = "2022-01-01T00:00:00"
            count_of_audible_words = 5
            words_out_of_order = False
            longest_consecutive_count = 3
            script.write_row_to_csv(writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)
        with open("test_output.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header
            row = next(reader)
            self.assertEqual(row, [filename, timestamp_iso8601, str(count_of_audible_words), str(words_out_of_order), str(longest_consecutive_count)])
        os.remove("test_output.csv")

    def test_write_row_to_csv_2(self):
        """
        Tests if the function correctly handles a case where words are out of order.
        """

        with open("test_output.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
            filename = "sample.wav"
            timestamp_iso8601 = "2022-01-01T00:00:00"
            count_of_audible_words = 5
            words_out_of_order = True
            longest_consecutive_count = 3
            script.write_row_to_csv(writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)
        with open("test_output.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header
            row = next(reader)
            self.assertEqual(row, [filename, timestamp_iso8601, str(count_of_audible_words), str(words_out_of_order), str(longest_consecutive_count)])
        os.remove("test_output.csv")

    def test_write_row_to_csv_3(self):
        """
        Tests if the function correctly handles a case where there are no audible words.
        """

        with open("test_output.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
            filename = "sample.wav"
            timestamp_iso8601 = "2022-01-01T00:00:00"
            count_of_audible_words = 0
            words_out_of_order = False
            longest_consecutive_count = 0
            script.write_row_to_csv(writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)
        with open("test_output.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header
            row = next(reader)
            self.assertEqual(row, [filename, timestamp_iso8601, str(count_of_audible_words), str(words_out_of_order), str(longest_consecutive_count)])
        os.remove("test_output.csv")

    def test_write_row_to_csv_4(self):
        """
        Tests if the function raises a ValueError when the input types are incorrect.
        """

        with open("test_output.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
            filename = 123
            timestamp_iso8601 = "2022-01-01T00:00:00"
            count_of_audible_words = 5
            words_out_of_order = False
            longest_consecutive_count = 3
            self.assertRaises(ValueError, script.write_row_to_csv, writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)
        os.remove("test_output.csv")

    def test_write_row_to_csv_5(self):
        """
        Tests if the function raises a ValueError when the input types are incorrect.
        """

        with open("test_output.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
            filename = "sample.wav"
            timestamp_iso8601 = "2022-01-01T00:00:00"
            count_of_audible_words = "5"
            words_out_of_order = False
            longest_consecutive_count = 3
            self.assertRaises(ValueError, script.write_row_to_csv, writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)
        os.remove("test_output.csv")

    def test_write_row_to_csv_value_error_1(self):
        """
        Tests if the function raises a ValueError when the filename is not a string.
        """
        
        with open("test_output.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
            filename = 123  # Not a string
            timestamp_iso8601 = "2022-01-01T00:00:00"
            count_of_audible_words = 5
            words_out_of_order = False
            longest_consecutive_count = 3
            self.assertRaises(ValueError, script.write_row_to_csv, writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)
        os.remove("test_output.csv")

    def test_write_row_to_csv_value_error_2(self):
        """
        Tests if the function raises a ValueError when the count_of_audible_words is not an integer.
        """

        with open("test_output.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
            filename = "sample.wav"
            timestamp_iso8601 = "2022-01-01T00:00:00"
            count_of_audible_words = "5"  # Not an integer
            words_out_of_order = False
            longest_consecutive_count = 3
            self.assertRaises(ValueError, script.write_row_to_csv, writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)
        os.remove("test_output.csv")

    def test_write_row_to_csv_value_error_3(self):
        """
        Tests if the function raises a ValueError when the words_out_of_order is not a boolean.
        """

        with open("test_output.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
            filename = "sample.wav"
            timestamp_iso8601 = "2022-01-01T00:00:00"
            count_of_audible_words = 5
            words_out_of_order = "False"  # Not a boolean
            longest_consecutive_count = 3
            self.assertRaises(ValueError, script.write_row_to_csv, writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)
        os.remove("test_output.csv")

    def test_process_audio_file_1_to_10(self):
        """
        Tests if the function correctly processes a valid .wav file.
        """

        with open('test-output-1-to-10.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
        # Test if the function correctly processes a valid .wav file
        filename = "09-29-2021 23-50-07.wav"
        processed_files = 0
        total_files = 1
        script.process_audio_file(filename, 'test-output-1-to-10.csv', processed_files, total_files)
        with open("test-output-1-to-10.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header
            try:
                row = next(reader)
                self.assertEqual(row, [filename, '2021-09-29T23:50:07', '10', 'False', '10'])
            except StopIteration:
                self.fail("No row in the CSV file after the header")
        os.remove("test-output-1-to-10.csv")

    def test_process_audio_file_empty(self):
        """
        Tests if the function correctly handles a file that is not a .wav file.
        """

        with open('test-output-empty.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
            writer.writeheader()
        # Test if the function correctly handles a file that is not a .wav file
        filename = "09-30-2021 02-58-07.txt"
        processed_files = 0
        total_files = 1
        script.process_audio_file(filename, 'test-output-empty.csv', processed_files, total_files)
        with open("test-output-empty.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header
            try:
                row = next(reader)
                self.fail("Row has been written after the header")
            except StopIteration:
                pass  # No row in the CSV file after the header, as expected
        os.remove("test-output-empty.csv")

if __name__ == "__main__":
    unittest.main()