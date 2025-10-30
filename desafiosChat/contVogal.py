pal=input('Digite uma palavra: ')
spal= list(pal)
for espaco in spal:
    if espaco in ' ':
        spal.remove(espaco)
conta_letra=len(spal)
i=0
for vogais in spal:
    if vogais in 'aeiou':
        i+=1
print('Na sua palavra {}, você tem {} letras e {} vogais.'.format(pal,conta_letra,i))