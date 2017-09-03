import compiler
from compiler.ast import *

ast = compiler.parseFile("input_file")

name = "flat_expr_";

def spit_flat_expr(n, count):
    if isinstance(n, Module):
        count = 0
        spit_flat_expr(n.node,count)
    elif isinstance(n, Stmt):
        for x in n.nodes:
            count = count + 1
            spit_flat_expr(x, count)
    elif isinstance(n, Printnl):
        count = count + 1
        buff = spit_flat_expr(n.nodes[0], count)
        print("print "+buff)
    elif isinstance(n, Discard):
        buff = spit_flat_expr(n.expr, count)
        return buff
    elif isinstance(n, Const):
        count = count + 1
        buff = name + str(count)
        buff = buff + ' = ' + str(n.value)
        print (buff)
        return (name + str(count))
    elif isinstance(n, Add):
        store = count
        count = count + 1
        left = spit_flat_expr(n.left, count)
        count = count + 1
        right = spit_flat_expr(n.right, count)
        buff = (name + str(store))
        buff = buff + " = " + left + " + " + right
        print (buff)
        return (name + str(store))
    elif isinstance(n, UnarySub):
        store = count
        count = count + 1
        buff = spit_flat_expr(n.expr, count)
        curr_expr = (name + str(store))
        print (curr_expr + " = " + "-" + buff)
        return curr_expr
    elif isinstance(n, CallFunc):
        count = count + 1
        buff = (name + str(count))
        print (buff + " = " + "input()")
        return buff
    else:
        print("Unrecognised AST expression")



spit_flat_expr(ast, 0)
