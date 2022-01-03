# QrGen 
import qrcode
import subprocess
import sys
import os
import argparse
from PIL import Image

lists = ['words/sqli.txt','words/xss.txt','words/cmdinj.txt','words/formatstr.txt','words/xxe.txt','words/strfuzz.txt','words/ssi.txt','words/lfi.txt']

def cmd():
    parser = argparse.ArgumentParser(description="Tool to generate Malformed QRCodes for fuzzing QRCode parsers/reader",
                                    usage='''main.py -l [number]\nusage: qrgen.py -w [/path/to/custom/wordlist]\n\nPayload lists:
    0 : SQL Injections
    1 : XSS
    2 : Command Injection
    3 : Format String
    4 : XXE
    5 : String Fuzzing
    6 : SSI Injection
    7 : LFI / Directory Traversal''',
    epilog="Pay attention everywhere, even in the dumbest spot")
    sgroup = parser.add_argument_group("Options for QRGen")
    sgroup.add_argument("--list","-l",type=int,help="Set wordlist to use",choices=[0,1,2,3,4,5,6,7])
    sgroup.add_argument("--wordlist","-w",type=str,default=None,help="Use a custom wordlist")
    opt = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return opt

def make_dirs():
    try:
        subprocess.check_output(['mkdir','genqr'],stderr=subprocess.STDOUT)
        print("Payload path generated..")
    except: pass
    try:
        subprocess.check_output(['rm', 'genqr/*'],stderr=subprocess.STDOUT)
        print("Clearing QR payloads dir..")
    except: pass

def get_words(opt):
    if opt.list!=None:
        payloads = open(lists[opt.list]).readlines()
    elif opt.wordlist:
        payloads = open(str(opt.wordlist)).readlines()
    payloads = [w.strip() for w in payloads]
    return payloads

def print_qrs(payload, i):
    img = qrcode.make(payload)
    img.save(f"genqr/payload-{i}.png")
    print(f"Generated {i} payloads!")

