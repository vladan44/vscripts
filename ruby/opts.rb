#!/usr/bin/env ruby
require 'optparse'

$usage = "Usage: " + $0 + " [options] <string> <filepattern>" + 
<<eos

    Available options:
-------------------------------------------------------------------------------
eos

$excludes = Array.new
$string  = ''
$pattern = ''

def cline_options(argv)
    options = {}
    optparse = OptionParser.new do |opts|
        opts.banner = $usage
        opts.on('-i o', '--ignore', 'Ignore case') do
            options[:ignore] = true
        end
        opts.on('-x x', '--excludes x', 'Exclude patterns') do |x|
            options[:excludes] = x
        end
    end
    optparse.parse!
    unless argv.length == 2
        puts optparse
        exit -1 
    end
    return options
end

def cline_args(argv)
    argv.each do |a|
        puts "Argument: #{a}"
    end
    $string = argv[0]
    $pattern = argv[1]
end

def options_do(opts)
    opts.each do |key, value|
        puts "Option #{key} : " + "#{value}\n"
    end
    $excludes.push(opts[:excludes])
end

def main 
    opt = cline_options(ARGV)
    options_do(opt)
    cline_args(ARGV)
end

if __FILE__ == $0
    main 
end
