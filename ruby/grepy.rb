#!/usr/bin/env ruby
require 'optparse'
require 'pp'

$banner = "Usage " + $0 + " [options] " + <<eos

    Zima je bila sa puno snega...
eos


# globbing
def glob
    Dir.foreach(".") do |entry|
       puts entry if File.file? entry
    end
end


# globbing
def cline_arguments(argv)
    options = {}
    optparse = OptionParser.new do |opts|
        opts.banner = $banner
        opts.on('-f o', '--flag o', 'Flag name') do |o|
            options[:flag] = o
        end
        opts.on('-n f', '--filename f', 'Filename') do |f|
            options[:filename] = f
        end
    end
    if argv.empty?  
        puts optparse 
        exit -1 
    end
    optparse.parse!
    return options
end

def process_options(opts)
    opts.each do |key, value|
        puts "Option #{key} : " + "#{value}\n"
    end
end

def main
    opts = cline_arguments(ARGV)
    process_options(opts)

    unless ARGV.empty?  
        ARGV.each do|a|
            puts "Argument: #{a}"
        end
    end
    glob
end

if __FILE__ == $0
    main 
end

