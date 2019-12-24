from parsers.logicVisitor import logicVisitor
from parsers.logicParser import logicParser
from parsers.logicLexer import logicLexer

from models.base_model import base_model

from copy import copy

from importlib import import_module

class EvalLogicVisitor(logicVisitor):
    def __init__(self, certificate, verbose):
        super().__init__()
        self.certificate = certificate
        self.verbose = verbose
        self.model = base_model()

        self.linked_variables = {}

    def visitImportModel(self, ctx: logicParser.ImportModelContext):
        if ctx.PARAMS():
            self.model = import_module(f"models.{ctx.PATHSTR().getText()}").model(ctx.PARAMS().getText())
        else:
            self.model = import_module(f"models.{ctx.PATHSTR().getText()}").model()

    def visitFormulaListBody(self, ctx: logicParser.FormulaListBodyContext):
        if self.verbose:
            print(self.visit(ctx.formula()))
        self.visit(ctx.formula_list())

    def visitFormulaListLast(self, ctx: logicParser.FormulaListLastContext):
        print(ctx.formula().getText())
        print(self.visit(ctx.formula()))

    def visitFormulaLand(self, ctx: logicParser.FormulaLandContext):
        a = self.visit(ctx.formula(0))
        b = self.visit((ctx.formula(1)))

        return a and b

    def visitFormulaLor(self, ctx: logicParser.FormulaLorContext):
        if self.visit(ctx.formula(0)):
            return True
        else:
            return self.visit((ctx.formula(1)))

    def visitAtomFormula(self, ctx: logicParser.AtomFormulaContext):
        return self.visit(ctx.formula())

    def visitAtomVar(self, ctx: logicParser.AtomVarContext):
        var = ctx.getText()

        if var in self.linked_variables:
            return self.linked_variables[var]
        else:
            raise Exception("Boom")

    def visitFormulaNot(self, ctx: logicParser.FormulaNotContext):
        return not self.visit(ctx.atom())

    def visitFormulaQforall(self, ctx: logicParser.FormulaQforallContext):
        save_value_set = copy(self.linked_variables)

        varname = ctx.VARNAME().getText()
        specifyed_type = ctx.TYPE().getText() if ctx.TYPE() else "bool"

        for x in self.model._value_set[specifyed_type]:
            self.linked_variables[varname] = x

            r_val = self.visit(ctx.formula())

            if not r_val:
                self.linked_variables = save_value_set
                return False

        self.linked_variables = save_value_set

        return True

    def visitFormulaQexists(self, ctx: logicParser.FormulaQexistsContext):
        save_value_set = copy(self.linked_variables)

        varname = ctx.VARNAME().getText()
        specifyed_type = ctx.TYPE().getText() if ctx.TYPE() else "bool"

        for x in self.model._value_set[specifyed_type]:
            self.linked_variables[varname] = x
            r_val = self.visit(ctx.formula())

            if r_val:
                if self.certificate:
                    print(f"{varname} = {x}")
                self.linked_variables = save_value_set
                return True

            self.linked_variables = save_value_set

        return False

    def visitFormulaExpr(self, ctx: logicParser.FormulaExprContext):
        return self.visit(ctx.expr())

    def visitAtomExpr(self, ctx: logicParser.AtomExprContext):
        return self.visit(ctx.atomexpr())

    def visitAtomxprPar(self, ctx: logicParser.AtomxprParContext):
        return self.visit(ctx.expr())

    def visitAtomTrue(self, ctx: logicParser.AtomTrueContext):
        return True

    def visitAtomFalse(self, ctx: logicParser.AtomFalseContext):
        return False

    def visitUnaryMinusExpr(self, ctx: logicParser.UnaryMinusExprContext):
        return - self.visit(ctx.expr())

    def visitMultiplicativeExpr(self, ctx: logicParser.MultiplicativeExprContext):
        op = ctx.myop.type
        a = self.visit(ctx.expr())
        b = self.visit(ctx.atomexpr())

        if op == logicLexer.MULT:
            return a * b
        elif op == logicLexer.DIV:
            return a / b

    def visitAdditiveExpr(self, ctx: logicParser.AdditiveExprContext):
        op = ctx.myop.type
        a = self.visit(ctx.expr(0))
        b = self.visit(ctx.expr(1))

        if op == logicLexer.PLUS:
            return a + b
        elif op == logicLexer.MINUS:
            return a - b

    def visitRelationalExpr(self, ctx: logicParser.RelationalExprContext):
        op = ctx.myop.type
        a = self.visit(ctx.expr(0))
        b = self.visit(ctx.expr(1))

        if op == logicLexer.GT:
            return a > b
        elif op == logicLexer.LT:
            return a < b
        elif op == logicLexer.LEQ:
            return a <= b
        elif op == logicLexer.GTEQ:
            return a >= b

    def visitEqualityExpr(self, ctx: logicParser.EqualityExprContext):
        op = ctx.myop.type
        a = self.visit(ctx.expr(0))
        b = self.visit(ctx.expr(1))

        if op == logicLexer.EQ:
            return a == b
        elif op == logicLexer.NEQ:
            return not (a == b)
        else:
            return False

    def visitPowerExpr(self, ctx: logicParser.PowerExprContext):
        a = self.visit(ctx.expr())
        b = self.visit(ctx.atomexpr())

        return a ** b

    def visitAtomExprInt(self, ctx: logicParser.AtomExprIntContext):
        return self.model.constante(int(ctx.getText()))

    def visitAtomExprVar(self, ctx: logicParser.AtomExprVarContext):
        var = ctx.getText()

        if var in self.linked_variables:
            return self.linked_variables[var]
        else:

            raise Exception(f"Variable {var} is not defined")
