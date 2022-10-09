#!/usr/bin/python3
import re

lines=[
    " when '0xxxx1' size = 0; ",
    " if !(reg IN {'000x','0101','011x','1000'}) then UNPREDICTABLE; ",
    " opc2 != '000' && !(opc2 IN {'10x'}) ",
    " immh IN {'000x'} || (immh IN {'001x'} && !HaveFP16Ext()) ",
    " if size = '0x' then UNDEFINED; "
]

def main():
    for line in lines:
        m = re.findall(r"([^\s\(\)]+?)\s*(?:!?=|IN)",line)
        if m :
            print(m)
            #print(m.group(1))
    return

if __name__ == "__main__":
    main()