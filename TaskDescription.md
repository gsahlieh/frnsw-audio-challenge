**Introduction:**
Welcome to the Audio Challenge! In this coding challenge, you will be tasked with processing a set of timestamped audio files containing a person counting from 1 to 10. Your goal is to determine the audibility of each word in the audio files and identify if any words are out of order.

**Instructions:**

**Dataset:**
You will be provided with a dataset containing audio files, each labeled as "date time.wav". The audio files contain recordings of a person counting from 1 to 10, but some words may be missing, out of order or both.

**Objective:**
Your task is to write a Python program that processes all the audio files and produces the following outputs for each file:

1. Count of audible words: Determine how many words (numbers) are audibly spoken in each audio file (audio: 2 3 4 5 6 8 9 10 answer: 8).

2. Identify if words are out of order: Determine if any of the words in the counting sequence are spoken out of order (audio: 1 2 4 3 5 6 7 8 answer: true).

3. Longest count: Determine the longest consecutive count (audio: 1 3 4 5 6 8 9 10 answer: 4)

**Guidelines:**

1. You can use any python library or online audio proccessing API you wish.

2. You can assume that the counting starts with "one" and ends with "ten."

**Output Format:**
Your code should output a CSV file that contains a row for each audio file with the following headings:

- Filename: <string>
- Timestamp <timestamp>
- Count of Audible Words: <int>
- Words Out of Order: <bool>
- Longest Consecutive Count: <int>


**Submission:**
Please provide a Python script that accomplishes the tasks described above. This should be delivered in a public git repo and include comments and documentation to explain your code as well as a folder that contains the final output CSV file.

**Evaluation:**
Your code will be evaluated based on correctness, efficiency, code quality, and adherence to the guidelines provided.

Good luck with the challenge!