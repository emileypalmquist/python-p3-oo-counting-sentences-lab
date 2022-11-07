#!/usr/bin/env python3
import re


class MyString:
    def __init__(self, value=""):
        if type(value) == str:
            self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if type(new_value) == str:
            self._value = new_value
            return self._value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        count = 0
        list_value = re.split('[.!?]', self.value)

        for element in list_value:
            if len(element) > 1:
                count += 1

        return count

    value = property(get_value, set_value,)
