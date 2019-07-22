import sys
import json


def json( string, value="" ):
        global json_data
        return string

json_data ='{'
xml_keys = {}
with open(sys.argv[2],'r') as xml_file:
        xml_file = xml_file.readlines()
        for xml in xml_file:
                if '=' in xml:
                        for val in xml.split(' '):
                                if '=' in val:
                                        a = val.split('=')[0]
                                        b = val.split('=')[1].split('"')[1]
                                        xml_keys.update([(a,b)])



template = []
with open(sys.argv[1],'r') as template_file:
        template_file = template_file.readlines()
        for temp in template_file:
                if 'node' in temp or '.each' in temp or '.map' in temp:
                        template.append(temp)

value = ''
for line in template:
        for element in line.split('"'):
                if len(element) > 0 and element[-1] == '=' and element.split(' ')[-1][:-1] in xml_keys:
                        ele = element.split(' ')[-1][:-1]
                        value = xml_keys[ele]
                elif '<%= node' in element and '.each' not in line and '.map' not in line:
                        if  '[' in element.split(' ')[1][4]:
                                print(element.split(' ')[1][4:])
                                print(''.join(x for x in element.split(' ')[1][4:].split("'")[0]))
                                #print(value)
                elif '.map' in element and '.join' in element:
                        if '@' in element:
                                each = element.split('.')[0].split(' ')[1]
                                delimiter = element.split('.')[2].split("'")[1]
                                loop = value.count(delimiter) + 1
                        else:
                                delimiter = element.split('.')[2].split("'")[1]
                                loop = value.count(delimiter) + 1
                elif '.each' in element:
                        if '[' in element:
                                find = element.split(' ')[3]
                                delimiter = ';'
                                loop = value.count(delimiter)
                                #elemet =''.join( x for x in element.split('<%= ')).split('%>')
                        else:
                                #print(element)
                                input()
                else:
                        next
