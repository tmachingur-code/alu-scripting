#!/usr/bin/env ruby

# Repetition Token #0
# Matches strings with an 'h', 'b', followed by 2 to 5 't', followed by an 'n'
regex = /hbt{2,5}n/

puts ARGV[0][regex]
