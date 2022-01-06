from qrgen import *
from passgen import *

import sys
import os
import argparse

# t = tested
# v = vax
# r = recovery

PRIVKEY = b"9d370d925476752486ab0e4a8e088228e493da12d1586fafae9f35880dbcfe03"
HEADER = b""
pass_data = {
    1: "DE",
    -260: {
        1: {
            "v": [
                {
                    "dn": 2,
                    "sd": float("inf"),
                    "ma": "ORG-100030215",
                    "vp": "1119349007",
                    "dt": "2021-06-11",
                    "co": "DE",
                    "ci": "420_69",
                    "mp": "EU/1/20/1528",
                    "is": "Reichsministerium für Volksaufklärung und Propaganda",
                    "tg": "840539006",
                }
            ],
            "nam": {
                "fnt": "Goebbels",
                "fn": "Goebbels",
                "gnt": "Paul Joseph",
                "gn": "Paul Joseph",
            },
            "ver": "1.0.0",
            "dob": "1897-10-29",
        }
    },
}

pass_data2 = {
    -260: {
        1: {
            "dob": "1998-02-26",
            "nam": {
                "fn": "Musterfrau-Gößinger",
                "fnt": "MUSTERFRAU<GOESSINGER",
                "gn": "Gabriele",
                "gnt": "GABRIELE",
            },
            "t": [
                {
                    "ci": "URN:UVCI:01:AT:B5921A35D6A0D696421B3E2462178297#I",
                    "co": "AT",
                    "is": "Ministry of Health, Austria",
                    "nm": "Roche LightCycler qPCR",
                    "ma": "1232",
                    "sc": "2021-02-20T12:34:56Z",
                    "tc": "Testing center Vienna 1",
                    "tg": "840539006",
                    "tr": "260415000",
                    "tt": "LP6464-4",
                }
            ],
            "ver": "1.2.1",
        }
    },
    1: "AT",
    4: 1624458597,
    6: 1624285797,
}


def main():
    # QrCode
    opt = cmd()
    make_dirs()
    payloads = get_words(opt)

    for i, p in enumerate(payloads):
        pass_data[1] = p.encode()
        msg = get_cose(pass_data2)
        msg = add_cose_key(msg, PRIVKEY)
        msg = flynn(msg.encode())
        msg = b45(msg)
        msg = b"HC1:" + msg
        print_qrs(msg, i)


def cmd():
    parser = argparse.ArgumentParser(
        description="Tool to generate Malformed QRCodes for fuzzing QRCode parsers/reader",
        usage="""main.py -l [number]\nusage: main.py -w [/path/to/custom/wordlist]\n\nPayload lists:
    0 : SQL Injections
    1 : XSS
    2 : Command Injection
    3 : Format String
    4 : XXE
    5 : String Fuzzing
    6 : SSI Injection
    7 : LFI / Directory Traversal""",
        epilog="Pay attention everywhere, even in the dumbest spot",
    )
    sgroup = parser.add_argument_group("Options for QRGen")
    sgroup.add_argument(
        "--list",
        "-l",
        type=int,
        help="Set wordlist to use",
        choices=[0, 1, 2, 3, 4, 5, 6, 7],
    )
    sgroup.add_argument(
        "--wordlist", "-w", type=str, default=None, help="Use a custom wordlist"
    )
    opt = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return opt


if __name__ == "__main__":
    main()
