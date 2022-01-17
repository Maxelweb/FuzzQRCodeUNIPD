#
# Fake Green Pass Generator
# -------------------------


from qrgen import *
from passgen import *
from datetime import datetime

import sys
import argparse

# --------------------- MAIN ---------------------
def main():
    opt = cmd()
    make_dirs()
    payloads = get_words(opt)

    for i, p in enumerate(payloads):
        msg = get_cose(get_pass(p))
        msg = add_cose_key(msg, PRIVKEY)
        msg = flynn(msg.encode(), HEADER)
        msg = b45(msg)
        msg = b"HC1:" + msg
        print("RAW certificate: ", msg)
        
        if(opt != None and opt.display):
            pass
        else:
            print_qrs(msg, fuzz_type[opt.list], i)
        print("-"*20)


def cmd():
    parser = argparse.ArgumentParser(
        description="Tool to generate Malformed QRCodes for fuzzing QRCode parsers/reader",
        usage=f"main.py -l [number]\nusage: main.py -w [/path/to/custom/wordlist]\n\nPayload lists: \n {fuzz_type}",
        epilog="Pay attention everywhere, even in the dumbest spot",
    )
    sgroup = parser.add_argument_group("Options for QRGen")
    sgroup.add_argument(
        "--list",
        "-l",
        type=int,
        help="Set wordlist to use",
        choices=fuzz_type.keys(),
    )
    sgroup.add_argument(
        "--wordlist", "-w", type=str, default=None, help="Use a custom wordlist"
    )
    sgroup.add_argument(
        "--display", "-d", type=str, default=None, help="Display Mode for QR Code Fuzzing"
    )
    opt = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return opt


if __name__ == "__main__":
    main()
