#!/usr/bin/env python

import pathlib
from curses import wrapper
import time
from subprocess import Popen
from random import randrange
import os.path

vowels_path = pathlib.Path("ipa_audio/vowels")
consonants_path = pathlib.Path("ipa_audio/consonants")

def get_files(kind):
    return [str(file) for file in list(kind.iterdir()) if str(file).endswith('mp3')]


def play(file):
    # using popen for asynchronous playback
    return Popen(['afplay', file])

def get_answer(file, vowel_mode):
    file = file.split('/')[-1]
    file = file.split('.')[0]
    chars = list(file)
    symbol = chars[-1]

    file = "".join(chars[:-2])
    if vowel_mode:
        answer = " ".join(file.split('_')[:-1])
    else:
        answer = " ".join(file.split('_'))

    return symbol, answer

def main(stdscr):
    def refresh():
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(0,0, 'Use <ENTER> to advance. Any other key to repeat.')

    def display(text):
        stdscr.addstr(1,0, text)

    def mode_prompt():
        display('Which do you want to test?\n1. Vowels\n2. Consonants\n')
        select = stdscr.getkey()
        match int(select):
            case 1:
                files = get_files(vowels_path)
            case 2:
                files = get_files(consonants_path)
            case 3:
                files = list(vowels.iterdir()) + list(consonants.iterdir())
        return select == '1', files

    def prompt():
        refresh()
        return stdscr.getkey() == '\n'

    vowel_mode, files = mode_prompt()

    while len(files):
#        selected = randrange(len(files))
        selected = 0
        file = str(files[selected])
        p = play(file)

        symbol, answer = get_answer(file, vowel_mode)

        if prompt():
            display(f'{answer}: {symbol} ')
            while stdscr.getkey() != '\n':
                p.terminate()
                p = play(file)
            del files[selected]
        p.terminate()

wrapper(main)
