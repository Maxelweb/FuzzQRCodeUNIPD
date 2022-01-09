#
# QrGen
# --------------------

import qrcode
import subprocess

from PIL import Image

lists = [
    "words/sqli.txt",
    "words/xss.txt",
    "words/cmdinj.txt",
    "words/formatstr.txt",
    "words/xxe.txt",
    "words/strfuzz.txt",
    "words/ssi.txt",
    "words/lfi.txt",
    "words/test.txt" # for testing purpose
]


def make_dirs():
    try:
        subprocess.check_output(["mkdir", "genqr"], stderr=subprocess.STDOUT)
        print("Payload path generated..")
    except:
        pass
    try:
        subprocess.check_output(["rm", "genqr/*"], stderr=subprocess.STDOUT)
        print("Clearing QR payloads dir..")
    except:
        pass


def get_words(opt):
    if opt.list != None:
        payloads = open(lists[opt.list]).readlines()
    elif opt.wordlist:
        payloads = open(str(opt.wordlist)).readlines()
    payloads = [w.strip() for w in payloads]
    return payloads


def print_qrs(payload, i):
    img = qrcode.make(payload)
    img.save(f"genqr/payload-{i}.png")
    print(f"Generated {i} payloads!")
