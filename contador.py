frase = "Uma vez Flamengo\
Sempre Flamengo\
Flamengo sempre eu hei de ser\
\
É meu maior prazer vê-lo brilhar\
Seja na terra, seja no mar\
Vencer, vencer, vencer\
\
Uma vez Flamengo\
Flamengo até morrer\
\
Na regata, ele me mata\
Me maltrata, me arrebata\
Que emoção no coração\
Consagrado no gramado\
Sempre amado, o mais cotado\
No Fla-Flu é o: Ai, Jesus!\
\
Eu teria um desgosto profundo\
Se faltasse o Flamengo no mundo\
Ele vibra, ele é fibra\
Muita libra já pesou\
Flamengo até morrer eu sou\
\
Uma vez Flamengo\
Sempre Flamengo\
Flamengo sempre eu hei de ser\
\
É meu maior prazer vê-lo brilhar\
Seja na terra, seja no mar\
Vencer, vencer, vencer\
\
Uma vez Flamengo\
Flamengo até morrer\
\
Na regata, ele me mata\
Me maltrata, me arrebata\
Que emoção no coração\
Consagrado no gramado\
Sempre amado, o mais cotado\
No Fla-Flu é o: Ai, Jesus!\
\
Eu teria um desgosto profundo\
Se faltasse o Flamengo no mundo\
Ele vibra, ele é fibra\
Muita libra já pesou\
Flamengo até morrer eu sou"

frase = frase.lower()

print(frase)

i = 0
qt_vezes = 0
let_mais_vezes = ""

x = len(frase)

while i < x:
    letra = frase[i]

    if letra == " ":
        i += 1
        continue

    qt_vezes1 = frase.count(letra)

    if qt_vezes < qt_vezes1:
        qt_vezes = qt_vezes1
        let_mais_vezes = letra
        
    i += 1


print("="*50)
print(f"A letra que apareceu mais vezes foi: '*{let_mais_vezes}*' e apareceu {qt_vezes}")
    
