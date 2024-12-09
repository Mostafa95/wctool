# wctool

This project is a command-line utility that counts the number of bytes/characters/words/lines in a given file. 

This project is a solution to the [WC-lite challenge](https://codingchallenges.fyi/challenges/challenge-wc) on Coding Challenges. 

To run this project run the following commands

```
python -m venv test_env
source test_env/bin/activate
python setup.py install
```

Then run the following command:

```
ccwc [option] filename
```

There are five options supported:

- generic: without an option, outputs the number of lines, words and bytes in a file.
- ```-c```: outputs the number of bytes in a file.
- ```-l```: outputs the number of lines in a file.
- ```-w```: outputs the number of words in a file.
- ```-m```: outputs the number of chars in a file.