#!/usr/bin/env python


# 1. Full english breakfast
def contains_full_english_alphabet(text):
    return _count_unique_letters(text) == 26


def _count_unique_letters(text):
    return len({item for item in set(text.lower()) if item.isalpha()})


# 2.
