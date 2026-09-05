#!/usr/bin/env ruby

# Repetition token
# Matches strings with a 'b', followed by 2 to 5 't', followed by an 'n'
regex = /bt{2,5}n/

p ARGV[0].scan(regex)
