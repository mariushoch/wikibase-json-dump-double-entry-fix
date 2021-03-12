import argparse
import json
import urllib.request
import math

parser = argparse.ArgumentParser(description='Fix Wikibase JSON dumps that (erroneously) have more than one entity on a line.')
parser.add_argument("infile", help="Input file")
parser.add_argument("outfile", help="Output file")

args = parser.parse_args()

def separate_lines(line, line_nr):
    offset = 0
    split = line.find( "}{" )
    while split != -1:
        line_1 = line[0:split + 1]
        # Note: This will not work if line is the last entity in the dump (but we don't expect the
        # problem there)
        line_2 = line[split + 1:-2]
        try:
            json.loads(line_1)
            json.loads(line_2)

            return line_1 + ",\n" + line_2 + ",\n"
        except:
            pass

        offset = split + 1
        split = line.find( "}{", offset )
    raise Exception( "Could not divide input file line " + str( line_nr ) + "." )


with open(args.infile) as in_file:
    with open(args.outfile, 'w') as out_file:
        line = in_file.readline()
        line_nr = 1
        while line:
            if line.find("}{") != -1:
                try:
                    try:
                        json.loads(line[0:-2])
                    except:
                        # Second to last line, no trailing comma
                        json.loads(line)
                except:
                    # Very short lines are the start/end of the dump ([, ] and new lines)
                    if len(line) > 4:
                        line = separate_lines( line, line_nr )
    
            out_file.write(line)
            line = in_file.readline()
            line_nr += 1
