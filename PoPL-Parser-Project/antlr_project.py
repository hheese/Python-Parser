import sys 
from antlr4 import *
from antlr4.tree.Trees import Trees
from PythonGrammarLexer import PythonGrammarLexer
from PythonGrammarParser import PythonGrammarParser

def main(argv):
    io_stream = FileStream(argv[1])
    lexer = PythonGrammarLexer(io_stream)
    stream = CommonTokenStream(lexer)
    parser = PythonGrammarParser(stream)
    tree = parser.start()
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
        main(sys.argv)
