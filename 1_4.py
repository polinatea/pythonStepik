namespaces = {'global': None} # ключ - namespace. значение - parent
variables = {'global': set()} # ключ - namespace. значение - множество переменных
def create(namesp,var):
    namespaces[namesp]=var
    variables[var]=None
    print(namespaces)
    print(variables)

def add(namesp,var):
    variables[namesp]=var

def get(namesp,var):
    print(variables.get[var])

while(True):
    n=input()
    cmd,namespace,variable=(str(i) for i in n.split())
    if (cmd=='create'):
        create(namespace,variable)
    elif (cmd=='add'):
        add(namespaces,variable)
    elif(cmd=='get'):
        get(namespaces,variable)


#get foo a