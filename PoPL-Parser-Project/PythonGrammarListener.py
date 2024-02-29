# Generated from PythonGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonGrammarParser import PythonGrammarParser
else:
    from PythonGrammarParser import PythonGrammarParser

# This class defines a complete listener for a parse tree produced by PythonGrammarParser.
class PythonGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by PythonGrammarParser#start.
    def enterStart(self, ctx:PythonGrammarParser.StartContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#start.
    def exitStart(self, ctx:PythonGrammarParser.StartContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#expr.
    def enterExpr(self, ctx:PythonGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#expr.
    def exitExpr(self, ctx:PythonGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#printRule.
    def enterPrintRule(self, ctx:PythonGrammarParser.PrintRuleContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#printRule.
    def exitPrintRule(self, ctx:PythonGrammarParser.PrintRuleContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#varitem.
    def enterVaritem(self, ctx:PythonGrammarParser.VaritemContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#varitem.
    def exitVaritem(self, ctx:PythonGrammarParser.VaritemContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#constatement.
    def enterConstatement(self, ctx:PythonGrammarParser.ConstatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#constatement.
    def exitConstatement(self, ctx:PythonGrammarParser.ConstatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#arguments.
    def enterArguments(self, ctx:PythonGrammarParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#arguments.
    def exitArguments(self, ctx:PythonGrammarParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#arithmeticstatement.
    def enterArithmeticstatement(self, ctx:PythonGrammarParser.ArithmeticstatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#arithmeticstatement.
    def exitArithmeticstatement(self, ctx:PythonGrammarParser.ArithmeticstatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#assignment.
    def enterAssignment(self, ctx:PythonGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#assignment.
    def exitAssignment(self, ctx:PythonGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#constatements.
    def enterConstatements(self, ctx:PythonGrammarParser.ConstatementsContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#constatements.
    def exitConstatements(self, ctx:PythonGrammarParser.ConstatementsContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#ifstatement.
    def enterIfstatement(self, ctx:PythonGrammarParser.IfstatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#ifstatement.
    def exitIfstatement(self, ctx:PythonGrammarParser.IfstatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#elifstatement.
    def enterElifstatement(self, ctx:PythonGrammarParser.ElifstatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#elifstatement.
    def exitElifstatement(self, ctx:PythonGrammarParser.ElifstatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#elsestatement.
    def enterElsestatement(self, ctx:PythonGrammarParser.ElsestatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#elsestatement.
    def exitElsestatement(self, ctx:PythonGrammarParser.ElsestatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#blockstatement.
    def enterBlockstatement(self, ctx:PythonGrammarParser.BlockstatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#blockstatement.
    def exitBlockstatement(self, ctx:PythonGrammarParser.BlockstatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#whilestatement.
    def enterWhilestatement(self, ctx:PythonGrammarParser.WhilestatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#whilestatement.
    def exitWhilestatement(self, ctx:PythonGrammarParser.WhilestatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#forloopstatement.
    def enterForloopstatement(self, ctx:PythonGrammarParser.ForloopstatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#forloopstatement.
    def exitForloopstatement(self, ctx:PythonGrammarParser.ForloopstatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:PythonGrammarParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:PythonGrammarParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#functionCall.
    def enterFunctionCall(self, ctx:PythonGrammarParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#functionCall.
    def exitFunctionCall(self, ctx:PythonGrammarParser.FunctionCallContext):
        pass



del PythonGrammarParser