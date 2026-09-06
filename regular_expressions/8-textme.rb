#!/usr/bin/env ruby
line = ARGV[0]
match = line.match(/\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\]/)
puts "#{match[1]},#{match[2]},#{match[3]}"

