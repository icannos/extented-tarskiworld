# Generated from /run/media/maxime/Documents/_ENS/M1_philo/thmodele/exttarski/logic.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logicParser import logicParser
else:
    from logicParser import logicParser

# This class defines a complete generic visitor for a parse tree produced by logicParser.

class logicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by logicParser#programm.
    def visitProgramm(self, ctx:logicParser.ProgrammContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#prog.
    def visitProg(self, ctx:logicParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#importModel.
    def visitImportModel(self, ctx:logicParser.ImportModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaListBody.
    def visitFormulaListBody(self, ctx:logicParser.FormulaListBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaListLast.
    def visitFormulaListLast(self, ctx:logicParser.FormulaListLastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaQforall.
    def visitFormulaQforall(self, ctx:logicParser.FormulaQforallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaLand.
    def visitFormulaLand(self, ctx:logicParser.FormulaLandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaExpr.
    def visitFormulaExpr(self, ctx:logicParser.FormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaLor.
    def visitFormulaLor(self, ctx:logicParser.FormulaLorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaAtom.
    def visitFormulaAtom(self, ctx:logicParser.FormulaAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaQexists.
    def visitFormulaQexists(self, ctx:logicParser.FormulaQexistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#formulaNot.
    def visitFormulaNot(self, ctx:logicParser.FormulaNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#powerExpr.
    def visitPowerExpr(self, ctx:logicParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:logicParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#atomExpr.
    def visitAtomExpr(self, ctx:logicParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:logicParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#relationalExpr.
    def visitRelationalExpr(self, ctx:logicParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:logicParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#equalityExpr.
    def visitEqualityExpr(self, ctx:logicParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#atomExprVar.
    def visitAtomExprVar(self, ctx:logicParser.AtomExprVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#atomxprPar.
    def visitAtomxprPar(self, ctx:logicParser.AtomxprParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#atomExprInt.
    def visitAtomExprInt(self, ctx:logicParser.AtomExprIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#atomVar.
    def visitAtomVar(self, ctx:logicParser.AtomVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#atomFormula.
    def visitAtomFormula(self, ctx:logicParser.AtomFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#atomTrue.
    def visitAtomTrue(self, ctx:logicParser.AtomTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logicParser#atomFalse.
    def visitAtomFalse(self, ctx:logicParser.AtomFalseContext):
        return self.visitChildren(ctx)



del logicParser