

from __future__ import annotations

RotorPositionT = tuple[int, int, int]
RotorSelectionT = tuple[str, str, str]


abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


rotor1 = "EGZWVONAHDCLFQMSIPJBYUKXTR"
rotor2 = "FOBHMDKEXQNRAULPGSJVTYICZW"
rotor3 = "ZJXESIUQLHAVRMDOYGTNFWPBKC"

reflector = {
    "A": "N",
    "N": "A",
    "B": "O",
    "O": "B",
    "C": "P",
    "P": "C",
    "D": "Q",
    "Q": "D",
    "E": "R",
    "R": "E",
    "F": "S",
    "S": "F",
    "G": "T",
    "T": "G",
    "H": "U",
    "U": "H",
    "I": "V",
    "V": "I",
    "J": "W",
    "W": "J",
    "K": "X",
    "X": "K",
    "L": "Y",
    "Y": "L",
    "M": "Z",
    "Z": "M",
}


rotor4 = "RMDJXFUWGISLHVTCQNKYPBEZOA"
rotor5 = "SGLCPQWZHKXAREONTFBVIYJUDM"
rotor6 = "HVSICLTYKQUBXDWAJZOMFGPREN"
rotor7 = "RZWQHFMVDBKICJLNTUXAGYPSOE"
rotor8 = "LFKIJODBEGAMQPXVUHYSTCZRWN"
rotor9 = "KOAEGVDHXPQZMLFTYWJNBRCIUS"


def _validator(
    rotpos: RotorPositionT, rotsel: RotorSelectionT, pb: str
) -> tuple[RotorPositionT, RotorSelectionT, dict[str, str]]:
    

    if (unique_rotsel := len(set(rotsel))) < 3:
        msg = f"Please use 3 unique rotors (not {unique_rotsel})"
        raise Exception(msg)

    
    rotorpos1, rotorpos2, rotorpos3 = rotpos
    if not 0 < rotorpos1 <= len(abc):
        msg = f"First rotor position is not within range of 1..26 ({rotorpos1}"
        raise ValueError(msg)
    if not 0 < rotorpos2 <= len(abc):
        msg = f"Second rotor position is not within range of 1..26 ({rotorpos2})"
        raise ValueError(msg)
    if not 0 < rotorpos3 <= len(abc):
        msg = f"Third rotor position is not within range of 1..26 ({rotorpos3})"
        raise ValueError(msg)

    
    pbdict = _plugboard(pb)

    return rotpos, rotsel, pbdict


def _plugboard(pbstring: str) -> dict[str, str]:
    
    if not isinstance(pbstring, str):
        msg = f"Plugboard setting isn't type string ({type(pbstring)})"
        raise TypeError(msg)
    elif len(pbstring) % 2 != 0:
        msg = f"Odd number of symbols ({len(pbstring)})"
        raise Exception(msg)
    elif pbstring == "":
        return {}

    pbstring.replace(" ", "")

    
    tmppbl = set()
    for i in pbstring:
        if i not in abc:
            msg = f"'{i}' not in list of symbols"
            raise Exception(msg)
        elif i in tmppbl:
            msg = f"Duplicate symbol ({i})"
            raise Exception(msg)
        else:
            tmppbl.add(i)
    del tmppbl

    
    pb = {}
    for j in range(0, len(pbstring) - 1, 2):
        pb[pbstring[j]] = pbstring[j + 1]
        pb[pbstring[j + 1]] = pbstring[j]

    return pb


def enigma(
    text: str,
    rotor_position: RotorPositionT,
    rotor_selection: RotorSelectionT = (rotor1, rotor2, rotor3),
    plugb: str = "",
) -> str:
    
    text = text.upper()
    rotor_position, rotor_selection, plugboard = _validator(
        rotor_position, rotor_selection, plugb.upper()
    )

    rotorpos1, rotorpos2, rotorpos3 = rotor_position
    rotor1, rotor2, rotor3 = rotor_selection
    rotorpos1 -= 1
    rotorpos2 -= 1
    rotorpos3 -= 1

    result = []

    
    for symbol in text:
        if symbol in abc:
            
            if symbol in plugboard:
                symbol = plugboard[symbol]

            
            index = abc.index(symbol) + rotorpos1
            symbol = rotor1[index % len(abc)]

            
            index = abc.index(symbol) + rotorpos2
            symbol = rotor2[index % len(abc)]

            
            index = abc.index(symbol) + rotorpos3
            symbol = rotor3[index % len(abc)]

        

            symbol = reflector[symbol]

           
            symbol = abc[rotor3.index(symbol) - rotorpos3]
            symbol = abc[rotor2.index(symbol) - rotorpos2]
            symbol = abc[rotor1.index(symbol) - rotorpos1]

            
            if symbol in plugboard:
                symbol = plugboard[symbol]

           
            rotorpos1 += 1
            if rotorpos1 >= len(abc):
                rotorpos1 = 0
                rotorpos2 += 1
            if rotorpos2 >= len(abc):
                rotorpos2 = 0
                rotorpos3 += 1
            if rotorpos3 >= len(abc):
                rotorpos3 = 0

        
        result.append(symbol)

    return "".join(result)


if __name__ == "__main__":
    message = "This is my Python script that emulates the Enigma machine from WWII."
    rotor_pos = (1, 1, 1)
    pb = "pictures"
    rotor_sel = (rotor2, rotor4, rotor8)
    en = enigma(message, rotor_pos, rotor_sel, pb)

    print("Encrypted message:", en)
    print("Decrypted message:", enigma(en, rotor_pos, rotor_sel, pb))
