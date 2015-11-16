#!/usr/bin/env ruby
require 'optparse'
require 'pp'

$banner = "Usage " + $0 + " [options] " + <<eos
    Ruby version of grepy.
eos

OPTIONS = {
    'uno' => ['-f o', '--flag o', 'Flag name', 'flag'],
    'dos' => ['-n f', '--filename f', 'Filename', 'filename']
}


def display_file(filename)
    File.open(filename, 'r') do |f|
        f.readlines.each { |c| puts c }
    end
end

def bail_out(msg)
    puts msg 
    exit -1 
end


def cline_arguments(argv)
    options = {}
    optparse = OptionParser.new do |opts|
        opts.banner = $banner 
        OPTIONS.each do |k, v|
            opts.on(v.shift, v.shift, v.shift) do |o|
                options[v.shift.to_sym] = o
            end
        end
    end

    optparse.parse!

    bail_out optparse unless argv.size == 1  

    return options, argv
end

def main
    opts, args = cline_arguments(ARGV)
    display_name args.shift
end

if __FILE__ == $0
    main 
end

