import sys

def print_script_and_arguments():
    script_name = sys.argv[0]
    arguments = sys.argv[1:]
    print('Script Name:', script_name)
    print('Script and Variables:', script_name, arguments)

print_script_and_arguments()
def helloWorld():
	print(‘Hello World’)


helloWorld()


