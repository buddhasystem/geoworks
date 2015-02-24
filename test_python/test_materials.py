#!/usr/bin/python
import sys, getopt
import gwMaterials
from gwMaterials import *


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"i:")
    except getopt.GetoptError:
        print 'test.py -i <filename>'
        sys.exit(2)

    if len(opts)==0:
        print 'No input file specified, exiting...'
        sys.exit(2)

    xml_file = opts[0][1]

    gmm = gwMaterialManager()

    try:
        gmm.parse_XML(xml_file)
    except:
        print 'Failed to parse file', xml_file
        sys.exit(1)
        
    gmm.output_elements()

if __name__ == "__main__":
    main(sys.argv[1:])
