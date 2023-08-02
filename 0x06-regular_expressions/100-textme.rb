#!/usr/bin/env ruby
send = ARGV[0].scan(/from:(\+?\w+)\]/).join(',')
rece = ARGV[0].scan(/to:(\+?\w+)\]/).join(',')
flag = ARGV[0].scan(/flags:(.*?)\]/).join()
puts "#{send},#{rece},#{flag}" 
