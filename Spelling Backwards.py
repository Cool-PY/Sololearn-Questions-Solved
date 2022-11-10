# Made By- Divyanshu Pawar
# 😉 Subscribe to Cool Py

def spell(txt):
    #your code goes here
    if txt:
        print(txt[-1])
        print(spell(txt[:-1]))
        
    return ''

txt = input()
spell(txt)