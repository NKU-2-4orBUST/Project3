from os import system as s

import os, argparse
#Creates Command line Argument Parsers
parser=argparse.ArgumentParser(usage='Quickly install or reinstall servers',description='Used to install Monit monitoring server on newly imaged clients  |  Format:  0.0.0.0-->255.255.255.255',add_help=True,allow_abbrev=True)
parser.add_argument('-s','--server', required=True, help='Sets variable for Server IP')
parser.add_argument('-c','--client', required=True, help='Sets variable for Server IP')
args = parser.parse_args()
server = args.s
client = args.c

s('wget https://github.com/NKU-2-4orBUST/Project3/raw/main/monitrc_client')
s('sed "s/IP_SERVER.*/'+server+'/g" monitrc_client > monit_test; sed "s/IP_ClIENT.*/'+client+'/g" monitrc_test > monit_test')
