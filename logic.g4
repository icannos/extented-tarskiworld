

grammar logic;

programm: prog EOF;

prog
    : model_definition prog
    | formula_list prog
    | formula_list
    | model_definition
    ;


model_definition
    : IMPORT PATHSTR (COMMA PARAMS)? SEMICOL #importModel
    ;

formula_list
    : formula SEMICOL formula_list  #formulaListBody
    | formula SEMICOL               #formulaListLast
    ;

formula
    : FORALL VARNAME (COLUMN TYPE)? COMMA formula                   #formulaQforall
    | EXISTS VARNAME (COLUMN TYPE)? COMMA formula                         #formulaQexists
    | formula LAND formula                              #formulaLand
    | formula LOR formula                               #formulaLor
    | expr                                              #formulaExpr
    | NOT atom                                          #formulaNot
    | atom                                              #formulaAtom
    ;

expr
    : MINUS expr                           #unaryMinusExpr
    | expr myop=(MULT|DIV) atomexpr       #multiplicativeExpr
    | expr myop=(PLUS|MINUS) expr          #additiveExpr
    | expr myop=(GT|LT|GTEQ|LEQ)  expr     #relationalExpr
    | expr myop=(EQ|NEQ) expr              #equalityExpr
    | expr POWER atomexpr                     #powerExpr
    | atomexpr                             #atomExpr
    ;

atomexpr
    : VARNAME #atomExprVar
    | LPAR expr RPAR #atomxprPar
    | INT #atomExprInt
    ;

atom
    : VARNAME #atomVar
    | LPAR formula RPAR #atomFormula
    | TRUE #atomTrue
    | FALSE #atomFalse
    ;

LAND : '/\\';
LOR : '\\/';

TRUE : 'True';
FALSE : 'False';

NOT : 'not';

FORALL : 'forall';
EXISTS : 'there exists';

SEMICOL : ';';
COMMA : ',';
COLUMN : ':';

LPAR : '(';
RPAR : ')';

EQ : '=';
NEQ : '!=';
LEQ : '<=';
LT : '<';
GT : '>';
GTEQ : '>=';
PLUS : '+';
MINUS : '-';
MULT : '*';
POWER : '^';
DIV : '/';
MOD : 'mod';


IMPORT : 'import';


fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;

INT : [0-9]+;

VARNAME : [a-z0-9]+;
TYPE : [A-Za-z0-9]+;
PARAMS : [A-Za-z0-9/]+;

PATHSTR : [A-Za-z0-9_]+;

SPACE
 : [ \t\r\n] -> skip
 ;

OTHER
 : .
 ;
