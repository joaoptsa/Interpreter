import re
import readline

variaveis = dict()

def tokenize(str):
    str =  re.split("(\s|\(|\))", str)
    str = filter(lambda a: a != ' ', str)
    str = filter(lambda a: a != '', str)
    return str

def parse(tokens):
    token = tokens.pop(0)
    if (token=='('):
        lista = list()
        while tokens[0] != ')':
            lista.append(parse(tokens))
        tokens.pop(0)
        return tuple(lista)
    else:
        if(token.replace('.','',1).isdigit()):
            if('.' in token):
               return float(token)
            else:
               return int(token)        
        elif(token!=')'):
            return token
    
def calc(args):    
    if(isinstance(args, tuple)):
        if(args[0]=='define'):
            variaveis[args[1]]=args[2]
            return
        if(args[0]=='+'):
            return (calc(args[1])+calc((args[2])))
        if(args[0]=='-'):
            return (calc(args[1])-calc((args[2])))        
        if(args[0]=='*'):
            return (calc(args[1])*calc((args[2])))
        if(args[0]=='/'):
            return (calc(args[1])/calc((args[2])))
        else:
            return avalia(args)
    else:
        if(isinstance(args, str)):
            return variaveis[args]
        return args
  
def avalia(args):
    for exp in args:
        value = calc(exp)
        if value is not None:
            return value

def interpreta(str):
    return(avalia(parse(tokenize("(" + str + ")"))))

def main():
    print("Trabalho 2 - interpretador de expressoes aritmeticas")
    print("Exemplo de input: ( define x 5.3 ) ( + ( * ( + 1 1) x) (+ ( * 3 2) 1))")
    while(1):
        expr = raw_input('> ')
        print(interpreta(expr))            
        
if __name__ == "__main__":
    main()
