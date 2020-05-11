import re
layoutlower = {
        'd': 'w',
        'r': 'e',
        'w': 'r',
        'b': 't',
        'j': 'y',
        'f': 'u',
        'u': 'i',
        'p': 'o',
        'h': 'd',
        't': 'f',
        'n': 'h',
        'e': 'j',
        'o': 'k',
        'i': 'l',
        'm': 'c',
        'c': 'v',
        'v': 'b',
        'k': 'n',
        'l': 'm',
        }

layoutupper = dict((k.upper(), v.upper()) for k, v in layoutlower.items())

layout = {**layoutlower, **layoutupper}
layout[';'] = 'p'
layout[':'] = 'P'
layout['y'] = ';'
layout['Y'] = ':'

inv_layout = {v: k for k, v in layout.items()}
c.bindings.commands = dict()
pattern = re.compile('|'.join(inv_layout.keys()))
for mode in ['normal', 'caret']:
    c.bindings.commands[mode] = dict()
    c.bindings.commands[mode] = c.bindings.commands.setdefault(mode)
    for key in layout.keys():
        c.bindings.commands[mode].setdefault(key)
    for oldkey in c.bindings.default[mode].keys():
        if not (oldkey.startswith('<') and oldkey.endswith('>')):
            c.bindings.commands[mode][pattern.sub(lambda x: inv_layout[x.group()], oldkey)] = c.bindings.default[mode][oldkey]


#print(c.bindings.default['normal']['J'])
#for i in c.bindings.commands['normal']:
#    if c.bindings.commands['normal'][i] == 'tab-next':
#        print (i)
config.load_autoconfig()
