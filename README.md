# PhoneticFlashCards
This is a command line project to help study the International Phonetic Alphabet. It uses audio files from wikipedia to randomly play audio of vowels or consonants. After pressing <ENTER> it will display the correct annotations. For vowels this is `backness`, `open-ness` and `roundness`. The wikipedia sounds do not include information on `tenseness` so that is not included at this time. For consonants this includes manner and place of articulation (e.g. [Voiced velar plosive](https://en.wikipedia.org/wiki/Voiced_velar_plosive)).

<img width="500" alt="image" src="https://github.com/joshstephenson/PhoneticFlashCards/assets/11002/1579eb87-28de-448a-8f7a-3159226e0880">
<img width="500" alt="image" src="https://github.com/joshstephenson/PhoneticFlashCards/assets/11002/d118eb37-9d51-4916-a641-fd92c20fad5a">

# Notes on platform and library support
This has only been tested on a mac and requires that the machine have `afplay` for playing audio. You can install it if you have [homebrew](https://brew.sh/) installed with the command `brew install afplay`.
Displaying strings and reading input is done with the curses library to make the experience a bit more game like.

# How to run
Make sure to `chmod u+x quiz.py` and then you can run with:
```
./quiz.py
```

# How the files were annotated
The files were downloaded from wikipedia with their original filenames which include their annotations. The IPA symbol for each phoneme was added manually to the filenames for classification purposes.

The filenames are read by the script to display the annotations.

# Attributions

Audio files included in this project are from the Wikipedia articles: 

[IPA Vowel chart with audio](https://en.wikipedia.org/wiki/IPA_vowel_chart_with_audio)

[IPA consonant chart with audio](https://en.wikipedia.org/wiki/IPA_consonant_chart_with_audio)

Creative Commons Attribution-Share-Alike License 3.0
