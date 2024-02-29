grammar PythonGrammar;

start: (expr COMMENT? NEWLINE)* ;

expr:
    COMMENT
    | ifstatement
    | '(' expr ')'
    | NEWLINE expr
    | printRule
    | assignment
    | whilestatement
    | forloopstatement
    | functionDeclaration
    | functionCall
    ;

COMMENT: '#' ~[\r\t\n]* ;

TAB: '\t' | '    ';
NEWLINE: [\n]+ ;

WS: [\t ]+ -> skip;

printRule: 'print(' (expr | varitem) ')';

INT    : [-]?[0-9]+ ;
FLOAT  : [-]?[0-9]+ '.' [0-9]+;
STRING : '"' ([a-z] | [A-Z] | [0-9] | '_')+ '"';
BOOL   : TRUE | FALSE;
LITERAL: INT
        | FLOAT
        | STRING
        | BOOL
        | LIST;

VARNAME: ([A-Z] | [a-z] | [0-9] | '_')+;
        
ASSIGNMENTOPERATOR
    : '='
    | '+='
    | '-='
    | '*='
    | '/=';

ARITHMETICOPERATOR
    : '+'
    | '-'
    | '/'
    | '*'
    | '%'
    | '^';

SIGNS
    : '+'
    | '-'
    | '/'
    | '*'
    | '%'
    | '^'
    | '!'
    ;

IFELSE
    : 'if'
    | 'elif'
    | 'else'
    ;
    
LIST : '[' LISTITEM (',' LISTITEM )* ']';
LISTITEM : LITERAL;

TRUE: 'True';
FALSE: 'False';

NOT: 'not';

CONOPERATORS
    : '>='
    | '<='
    | '>'
    | '<'
    | '=='
    | '!='
    | 'and'
    | 'or'
    ;

varitem
    : INT
    | FLOAT
    | STRING
    | BOOL
    | LIST;

constatement: NOT? (VARNAME | varitem) CONOPERATORS NOT? (VARNAME | varitem);

arguments
    : VARNAME (',' VARNAME)*
    | '*' VARNAME
    ;
arithmeticstatement
    : (VARNAME | varitem) ARITHMETICOPERATOR (VARNAME | varitem) (ARITHMETICOPERATOR (VARNAME | varitem) )*;

assignment: VARNAME (ASSIGNMENTOPERATOR | '=') (arithmeticstatement | VARNAME | varitem) ;

constatements
        : constatement (('and' | 'or') (constatement | NOT? VARNAME | NOT? LITERAL) )*;

ifstatement
    : 'if' '(' constatements ')' ':' blockstatement elifstatement*  elsestatement?
    | 'if' constatements ':' blockstatement elifstatement* elsestatement?;


elifstatement: '\nelif' '(' constatements ')' ':' blockstatement
    | '\nelif' constatements ':' blockstatement;

elsestatement: '\nelse:' blockstatement;

blockstatement: (NEWLINE TAB? (expr | 'break' | 'continue'))+;

whilestatement
    : 'while' '(' constatements ')' ':' blockstatement
    | 'while' constatements ':' blockstatement;

forloopstatement
    : 'for' VARNAME 'in' (VARNAME | STRING) ':' blockstatement
    | 'for' '(' VARNAME 'in' (VARNAME | STRING) ')' ':' blockstatement;

functionDeclaration
    : 'def' VARNAME '(' arguments? ')' ':' blockstatement
    ;

functionCall
    : VARNAME '(' arguments? ')'
    | VARNAME '(' (VARNAME '=' varitem) (',' VARNAME '=' varitem)* ')'
    ;