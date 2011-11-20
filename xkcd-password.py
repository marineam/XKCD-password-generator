#!/usr/bin/env python
# encoding: utf-8

__LICENSE__ = """
Copyright (c) 2011, Steven Tobin.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import random
import os
import sys

WORD_FILE = os.path.join(os.path.dirname(__file__), "2of12.txt")

class Generator(object):

    Random = random.SystemRandom
    word_file = os.path.join(os.path.dirname(__file__), "2of12.txt")
    min_length = 4
    max_length = 9
    phrase_length = 4

    def __init__(self):
        """Load the word list"""

        self.random = self.Random()
        self.words = []

        try:
            with open(self.word_file) as wlf:
                for line in wlf:
                    word = line.strip()
                    if self.min_length <= len(word) <= self.max_length:
                        self.words.append(word)
        except IOError, ex:
            sys.stderr.write("Failed to read word list: %s" % ex)
            sys.exit(1)

        if not self.words:
            sys.stderr.write("Empty word list from %s" % self.word_file)
            sys.exit(1)

    def generate(self):
        """Generate a single pass phrase."""

        return " ".join(self.random.sample(self.words, self.phrase_length))

    def interactive_generator(self):
        """Generate pass phrases until the user is happy."""

        print self.generate()
        while not raw_input():
            print self.generate()

if __name__ == '__main__':
    g = Generator()
    g.interactive_generator()
