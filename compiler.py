import compiler 
from compiler.ast import *


if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print('Usage:', sys.argv[0], 'pythonfile.py')
		sys.exit(1)
	compfile = open(sys.argv[1])
	compdata = compfile.read()
	compfile.close()

	ast = compiler.parse(compdata)

	flag = true
	lprim = ast.getChildren()
	#apparently the compiler module has a method for getting a flattened list? 
	
	
	
	#while(flag)
		#traverse ast
		#if primitive node (variable or constant, add to lprim)
		#if isInstance(ast.module):
			
		#elif isInstance

