#!/usr/bin/env ruby

# Repetition Token #1
# Matches strings with an 'h', an optional 'b', a 't', and an 'n'
regex = /hb?tn/

puts ARGV[0][regex]
