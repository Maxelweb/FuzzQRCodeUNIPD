from qrgen import *
from passgen import *

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
                    "tg": "840539006"
                }
            ],
            "nam": {
                "fnt": "Goebbels",
                "fn": "Goebbels",
                "gnt": "Paul Joseph",
                "gn": "Paul Joseph"
            },
            "ver": "1.0.0",
            "dob": "1897-10-29"
        }
    }
}


def main():
    # QrCode
    opt = cmd()
    make_dirs()
    payloads = get_words(opt)

    for i, p in enumerate(payloads):
        pass_data[1] = p.encode()
        msg = get_cose(pass_data)
        msg = add_cose_key(msg, PRIVKEY)
        msg = flynn(msg.encode())
        msg = b45(msg)
        msg = b"HC1:" + msg
        print_qrs(msg, i)

if __name__ == "__main__":
    main()
