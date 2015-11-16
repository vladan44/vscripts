#!/usr/bin/env ruby
require 'optparse'
require 'pp'

$banner = "Usage " + $0 + " [options] " + <<eos
    Ruby version of grepy.
eos

OPTIONS = { 
    'ignore' => ['-i', '--ignorecase', 'Ignore case', :ignorecase],
    'regex'  => ['-e', '--regex', 'Extended regular expressions', :eregex],
    'exclude'  => ['-x p', '--excludes p', 'Excluded pattern', :exclude],
    'dos' => ['-n f', '--filename f', 'Filename', :filename] 
}

$flags = {}

# globbing
def regex_glob(string, pattern)
    begin
        Dir.foreach('.') do |entry|
            next if /#{$flags[:exclude]}/.match(entry)

            if /#{pattern}/.match(entry)
                puts "Regex file #{entry}" if File.file? entry
            end
        end
    rescue => e
        puts e.to_s
    end
end

def glob(string, pattern)
    Dir.glob(pattern) do |entry|
        puts "File: #{entry}" if File.file? entry
    end
end

def bail_out(msg)
    puts msg
    exit -1
end

# command line arguments
def cline_arguments(argv)
    options = {}
    optparse = OptionParser.new do |opts|
        opts.banner = $banner
        OPTIONS.each do |k, v|
            opts.on(v.shift, v.shift, v.shift) do |o|
                options[v.shift] = o
            end
        end
    end

    optparse.parse!

    bail_out optparse unless argv.size == 2

    return options, argv
end

def process_options(opts)
    opts.each do |key, value|
        case key
            when :exclude
                $flags[:exclude] = value
            when :filename
                $flags[:filename] = value
            when :ignorecase 
                $flags[:ignoreflag] = true
            when :eregex 
                $flags[:eregex] = true
            else 
                bail_out "unknown option: #{key} #{value}"
        end
    end
end

def main
    opts, args = cline_arguments(ARGV)
    process_options(opts)

    if $flags[:eregex]
        regex_glob args.shift, args.shift
    else
        glob args.shift, args.shift
    end
end

if __FILE__ == $0
    main
end

