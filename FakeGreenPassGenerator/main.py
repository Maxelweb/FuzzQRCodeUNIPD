from qrgen import *
from passgen import *
from datetime import datetime

import sys
import argparse

# TODO: test with current today date

yesterday = datetime.timestamp(datetime.now()) - 86400
tomorrow = datetime.timestamp(datetime.now()) + (7 * 86400)

# --- Legend GP types ---
# t = tested
# v = vax
# r = recovery
# -----------------------

fuzz_type = {
    0 : "SQL_Injections",
    1 : "XSS",
    2 : "Command_Injection",
    3 : "Format_String",
    4 : "XXE",
    5 : "String_Fuzzing",
    6 : "SSI_Injection",
    7 : "LFI_Directory_Traversal",
    8 : "Test",
}

PRIVKEY = b"9d370d925476752486ab0e4a8e088228e493da12d1586fafae9f35880dbcfe03"
HEADER = b""

def get_pass(data: str):
    return {
            4: 1683849600,
            6: 1635501173,
            1: "IT",
            -260: {
                1: {
                    "t": [
                        {
                            "sc": "2022-01-06T11:40:00+02:00",
                            "ma": "1268",
                            "tt": "LP217198-3",
                            "co": "IT",
                            "tc": "PINCOPALLO SRL",
                            "ci": "01ITFF9EECC5890441F5AC77BA97A5577C22#6",
                            "is": "Ministero della Salute",
                            "tg": "840539006",
                            "tr": "260415000",
                        }
                    ],
                    "nam": {
                        "fnt": data,
                        "fn": data,
                        "gnt": "SNOW",
                        "gn": "SNOW",
                    },
                    "ver": "1.3.0",
                    "dob": "2000-01-01",
                }
            },
        }

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
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8],
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
