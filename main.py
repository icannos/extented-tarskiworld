import argparse
import antlr4

from parsers.logicLexer import logicLexer
from parsers.logicParser import logicParser
from logicEvaluator import EvalLogicVisitor


def parse_file(path):
    input_s = antlr4.FileStream(path, encoding='utf8')
    lexer = logicLexer(input_s)
    stream = antlr4.CommonTokenStream(lexer)
    parser = logicParser(stream)
    tree = parser.programm()

    return tree

if __name__ == "__main__":
    # ======================================================================== #
    parser = argparse.ArgumentParser(description='Test if formulas are true under the specified model.')
    parser.add_argument('path', type=str, help='file of formulas to test')
    parser.add_argument('-c', '--certificate', help='Display a certificate in case of "there exists" clauses',
                        action="store_true")
    parser.add_argument('-v', '--verbose', help='Displays formulas and some debugging data',
                        action="store_true")
    args = parser.parse_args()

    # ======================================================================== #

    logicEval = EvalLogicVisitor(certificate=args.certificate, verbose=args.verbose)

    tree = parse_file(args.path)
    logicEval.visit(tree)

