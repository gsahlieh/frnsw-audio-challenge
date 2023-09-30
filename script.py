import os
import csv
import re
import speech_recognition as sr
from datetime import datetime

# Initialize recognizer
r = sr.Recognizer()

# Directory containing the audio files
audio_dir = "audio"

# Output CSV file
output_file = "output.csv"

def get_total_files(audio_dir):
    """
    Counts the total number of .wav files in a given directory.

    Parameters:
    audio_dir (str): The directory to search for .wav files.

    Returns:
    int: The total number of .wav files in the directory.
    """
    return len([name for name in os.listdir(audio_dir) if name.endswith(".wav")])

def get_audio_in_array_format_int(text):
    """
    Converts a string of digits into an array of integers.

    Parameters:
    text (str): The string of digits to convert.

    Returns:
    list: The converted array of integers.

    Raises:
    ValueError: If the input is not a string or if the string contains non-digit characters.
    """

    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    if not text.isdigit():
        raise ValueError("Input string must only contain digits.")
    text_with_spaces = ' '.join(text)
    if '1 0' in text_with_spaces:
        text_with_spaces = text_with_spaces.replace('1 0', '10')
    text_array = text_with_spaces.split()
    try:
        text_array_int = [int(word) for word in text_array]
    except ValueError:
        raise ValueError("Input string must be in formats like '1234678910'.")
    return text_array_int

def get_timestamp(filename):
    """
    Extracts the timestamp from a filename.

    Paramete
    filename (str): The filename to extract the timestamp from.

    Returns:
    str: The extracted timestamp in ISO 8601 format.

    Raises:
    ValueError: If the filename is not in the expected format.
    """

    if not re.match(r'\d{2}-\d{2}-\d{4} \d{2}-\d{2}-\d{2}\.wav', filename):
        return None
    try:
        date_str = filename.split('.')[0]
        date_time_obj = datetime.strptime(date_str, '%m-%d-%Y %H-%M-%S')
        return date_time_obj.isoformat()
    except ValueError:
        print(f"Invalid filename format for {filename}. Expected format: 'mm-dd-yyyy hh-mm-ss.wav'")
        return None

def find_longest_consecutive_count_and_order(text_array_int):
    """
    Finds the longest consecutive count and checks if the words are out of order.

    Parameters:
    text_array_int (list): The array of integers to check.

    Returns:
    tuple: The longest consecutive count and a boolean indicating if the words are out of order.

    Raises:
    ValueError: If the input is not a list or if the list contains non-integer items.
    """

    if not text_array_int:
        raise ValueError("Input must not be an empty list.")
    if not all(isinstance(item, int) for item in text_array_int):
        raise ValueError("Input must be an array of integers.")
    words_out_of_order = False
    longest_consecutive_count = 0
    current_consecutive_count = 1
    previous_number = text_array_int[0]

    for i in range(1, len(text_array_int)):
        if text_array_int[i] < previous_number:
            words_out_of_order = True

        if text_array_int[i] == previous_number + 1:
            current_consecutive_count += 1
        else:
            longest_consecutive_count = max(longest_consecutive_count, current_consecutive_count)
            current_consecutive_count = 1

        previous_number = text_array_int[i]

    longest_consecutive_count = max(longest_consecutive_count, current_consecutive_count)
    return longest_consecutive_count, words_out_of_order

def write_row_to_csv(writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count):
    """
    Writes a row to a CSV file.

    Parameters:
    writer (csv.DictWriter): The writer object to use for writing to the CSV file.
    filename (str): The filename of the audio file.
    timestamp_iso8601 (str): The timestamp of the audio file in ISO 8601 format.
    count_of_audible_words (int): The count of audible words in the audio file.
    words_out_of_order (bool): A boolean indicating if the words in the audio file are out of order.
    longest_consecutive_count (int): The longest consecutive count of words in the audio file.

    Raises:
    ValueError: If the inputs are not of the expected types.
    """
    
    if not isinstance(writer, csv.DictWriter) or not isinstance(filename, str) or not isinstance(timestamp_iso8601, str) or not isinstance(count_of_audible_words, int) or not isinstance(words_out_of_order, bool) or not isinstance(longest_consecutive_count, int):
        raise ValueError("Invalid input types. Expected types are: DictWriter, str, str, int, bool, int.")
    writer.writerow({'Filename': filename, 'Timestamp': timestamp_iso8601, 'Count of Audible Words': count_of_audible_words, 'Words Out of Order': words_out_of_order, 'Longest Consecutive Count': longest_consecutive_count})

def process_audio_file(filename, output_file, processed_files, total_files):
    """
    Processes an audio file and writes the results to a CSV file.

    Parameters:
    filename (str): The filename of the audio file to process.
    output_file (str): The filename of the CSV file to write the results to.
    processed_files (int): The number of files that have already been processed.
    total_files (int): The total number of files to process.

    Returns:
    int: The updated number of processed files.
    """

    if not filename.endswith(".wav"):
        return processed_files
    if filename.endswith(".wav"):
        audio_file = os.path.join(audio_dir, filename)
        
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)
        
        timestamp_iso8601 = get_timestamp(filename) or "None"

        try:
            text = r.recognize_google(audio_data)
            text_array_int = get_audio_in_array_format_int(text)
            count_of_audible_words = len(text_array_int)
            longest_consecutive_count, words_out_of_order = find_longest_consecutive_count_and_order(text_array_int)
            with open(output_file, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
                write_row_to_csv(writer, filename, timestamp_iso8601, count_of_audible_words, words_out_of_order, longest_consecutive_count)

        except Exception as e:
            with open(output_file, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count'])
                write_row_to_csv(writer, filename, timestamp_iso8601, 0, False, 0)

    processed_files += 1
    percentage_complete = round((processed_files / total_files) * 100, 2)
    print(f"Processing: {percentage_complete}% complete")

    return processed_files  # return the updated value

def main():
    """
    The main function that processes all audio files in a directory and writes the results to a CSV file.
    """

    total_files = get_total_files(audio_dir)
    processed_files = 0

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Filename', 'Timestamp', 'Count of Audible Words', 'Words Out of Order', 'Longest Consecutive Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    for filename in os.listdir(audio_dir):
        processed_files = process_audio_file(filename, output_file, processed_files, total_files)  # update the variable with the returned value

if __name__ == "__main__":
    main()