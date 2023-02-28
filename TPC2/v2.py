def somadorOnOff():
    total = 0
    sequence = ''
    soma = True

    while True:
        try:
            text = input()
        except EOFError:
            break
        
        i = 0
        while i < len(text):
            c = text[i]
            if c.isdigit() and soma:
                sequence += c
                i += 1
                while i < len(text) and text[i].isdigit():
                    sequence += text[i]
                    i += 1
                total += int(sequence)
                sequence = ''
            elif text[i:i+3].lower() == 'off':
                soma = False
                sequence = ''
                i += 3
            elif text[i:i+2].lower() == 'on':
                soma = True
                i += 2
            elif c == '=' and soma:
                print(total)
                sequence = ''
                i += 1
            else:
                i += 1

somadorOnOff()
