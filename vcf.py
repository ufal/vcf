#!/usr/bin/env python3
#coding: utf-8

import sys

import logging
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


# ^ Name                 ^ Department ^ Office  ^ Work phone  ^ Home phone  ^  Mobile phone ^ E-mail                       ^
# | Michal Auersperger   | ÚFAL      | 424      |             |             | 777 628 379  | auersperger                  


# BEGIN:VCARD
# VERSION:3.0
# REV:2017-09-11 15:31:28
# PRODID:-//class_vcard from thewebvendor.com//NONSGML Version 1//EN
# ORG:ÚFAL
# TEL;TYPE=work,voice:4325
# TEL;TYPE=home,voice:+420 222 362 603
# TEL;TYPE=cell,voice:+420 606 833 591
# EMAIL;TYPE=internet,pref:fucik@ufal.mff.cuni.cz
# N:Fučík;Milan;;;;
# FN:Milan Fučík
# ADR;TYPE=work:;;426;;;;
# END:VCARD
 
def isphone(text):
    return text and text.replace(' ', '').replace('+', '').isnumeric()

for line in sys.stdin:
    fields = line.split('|')
    if len(fields) > 4:
        if len(fields) != 9:
            logging.warn('Bad line: {}'.format(line))
        else:
            _, name, department, office, workphone, homephone, mobilephone, email, _ = [x.strip() for x in fields]
            if name:
                if ' ' not in name:
                    logging.warn('Bad line: {}'.format(line))
                else:
                    firstname, surname = name.split(' ', 1)            
                    # this looks like a valid line
                    print('BEGIN:VCARD')
                    print('VERSION:3.0')
                    print('FN:{}'.format(name))
                    print('N:{};{};;;'.format(surname, firstname))
                    if department:
                        if department == 'ÚFAL':
                            print('ORG:MFF UK;ÚFAL;')
                        else:
                            print('ORG:{};;'.format(department))
                    if office:
                        if office.startswith('N'):
                            street = 'V Holešovičkách 747/2'
                            town = 'Praha 8'
                            zipcode = '180 00'
                        else:
                            street = 'Malostranské náměstí 25'
                            town = 'Praha 1'
                            zipcode = '118 00'
                        print('ADR;TYPE=work:;Office {};{};{};;{};'.format(office, street, town, zipcode))
                    if isphone(workphone):
                        print('TEL;TYPE=work:{}'.format(workphone))
                        print('TEL;TYPE=work:+420 95155 {}'.format(workphone))
                    if isphone(homephone):
                        print('TEL;TYPE=home:{}'.format(homephone))
                    if isphone(mobilephone):
                        print('TEL;TYPE=cell:{}'.format(mobilephone))
                    if email:
                        if '@' not in email:
                            email = email + '@ufal.mff.cuni.cz'
                        print('EMAIL'.format(email))
                    print('END:VCARD')







