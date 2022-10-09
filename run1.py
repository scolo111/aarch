#!/usr/bin/python
# -*- coding: UTF-8 -*-
 

from xml.dom.minidom import parse
import xml.dom.minidom
import os 
import sys
import re


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        else:
            rc.append(getText(node.childNodes))
    return ''.join(rc)

#def get_pcode_from_iclass_element(e):
#    for node in e.childNodes:
#        if node.nodeType not node.TEXT_NODE:
            

def get_pcode_from_xml_by_iclass(d, fn, iname='', all=False):
    path = os.path.join(d, fn)
    dom = parse(path)
    root = dom.documentElement
    e_list = root.getElementsByTagName('iclass') 
    for i, e in enumerate(e_list):
        if all:
            print(' '.join(['='*20, fn, f'{i+1}/{len(e_list)}', e.getAttribute("name")]))
            if e.getElementsByTagName('ps'):
                ps_node = e.getElementsByTagName('ps')[0]
                print("%s" % getText(ps_node.childNodes))
                print('='*20)
        else: 
            if (e.getAttribute("name") == iname):
                ps_node = e.getElementsByTagName('ps')[0]
                p_codes = getText(ps_node.childNodes)
                #print("%s" % p_codes)
                return p_codes

def dump_all_pcode(d):
    if os.path.isdir(d):
        #get_pcode_from_xml_by_iclass(dir, "ld1b_z_p_br.xml", all=True)
        for fn in sorted(os.listdir(d)):
            if fn[0] != '.' and fn.endswith('.xml') and fn != 'onebigfile.xml' and fn != 'shared_pseudocode.html':
                get_pcode_from_xml_by_iclass(d, fn, all=True)
    else:
        print(f"{dir} is not a directory")
        sys.exit(1)

def get_prev_res_word(lines):
    lines 
    return word 

if __name__ == "__main__":
    d = 'A64/ISA_A64_xml_A_profile-2022-06/'
    #dump_all_pcode(d)
    pcode = get_pcode_from_xml_by_iclass(d, 'msr_imm.xml', 'System')
    pcode_lines = pcode.splitlines()
    one_line = ''.join(pcode_lines[42:45])
    print(f'one line before: {one_line}')
    one_line = re.sub(r'if (?!if).*$', '', one_line)
    print(f'one line after: {one_line}')
    #for i, line in enumerate(pcode_lines):
    #    if 'UNDEFINED' in line:
    #        get_prev_res_word(lines[0:i+1])