# README.md

## Introduction

This project consists of two main Python scripts: `script.py` and `test.py`. 

- `script.py` is the main script that processes audio files, extracts information from them, and writes the results to a CSV file.
- `test.py` contains a suite of unit tests that verify the correctness of the functions in `script.py`.

The `run.py` script is a utility script that allows you to easily run either `script.py` or `test.py` (or both) from the command line.

## Running the Scripts

To run the scripts, you can use the `run.py` script. Here's how to use it:

```python3 run.py script test``` will run `test.py`, then if successful will run `script.py`
```python3 run.py script``` will only run `script.py`
```python3 run.py test``` will only run `script.py`


This command will run both `script.py` and `test.py`. If you only want to run one of them, you can specify just `script` or `test` as the argument.

## script.py

The `script.py` script processes audio files in the `audio` directory. For each audio file, it uses Google's speech recognition service to transcribe the audio to text. It then performs some analysis on the transcribed text, such as counting the number of audible words, checking if the words are in order, and finding the longest consecutive count of words. The results are written to a CSV file.

## test.py

The `test.py` script contains a suite of unit tests for the functions in `script.py`. These tests verify that the functions are working correctly. The tests cover various scenarios, such as valid and invalid inputs, and expected outputs. The tests can be run using the `run.py` script, as described above.

## Conclusion

This project provides a useful tool for processing and analyzing audio files. The `run.py` script makes it easy to run the main script and the tests. The `script.py` script performs the main processing and analysis, and the `test.py` script ensures that the functions in `script.py` are working correctly.