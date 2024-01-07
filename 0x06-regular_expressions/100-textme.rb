#!/usr/bin/env ruby
puts (((ARGV[0].scan(/[a-zA-Z0-9\+]{0,12}(?=\]\ \[to:)\b/))[0...-1]) + (ARGV[0].scan(/[a-zA-Z0-9\+]{0,12}(?=\]\ \[flags:)\b/))[0...-1] + (ARGV[0].scan(/\B[0-9\-:]+(?=\]\ \[msg:)\b/))).join(",")
