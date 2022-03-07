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
    "words/json.txt",
    "words/metachars.txt",
    "naughty-strings.txt",
    "special-chars.txt",
    "words/test.txt" # for testing purpose
]

fuzz_type = {
    0 : "SQL_Injections",
    1 : "XSS",
    2 : "Command_Injection",
    3 : "Format_String",
    4 : "XXE",
    5 : "String_Fuzzing",
    6 : "SSI_Injection",
    7 : "LFI_Directory_Traversal",
    8 : "JSON",
    9 : "Metachars",
    10: "Naughty_strings",
    11: "Special_Chars",
    12: "Test" # for testing purpose
}


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
    elif opt.wordlist != None:
        payloads = open(str(opt.wordlist)).readlines()
    payloads = [w.strip() for w in payloads]
    return payloads


def print_qrs(payload, t, i):
    img = qrcode.make(payload)
    img.save(f"genqr/{t}-{i}.png")
    print(f"Generated {i} payloads!")
