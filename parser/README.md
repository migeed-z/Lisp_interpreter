PARSER

-- P-expression -> AST, False, or raise an Exception

An AST is one of:
- BSLDef
- PrimDef
- IsPrimDef
- BSLExpr

A BSLDef is one of:
- StructDef
- ConstructorDef
- SelectorDef
- PredicateDef
- FunctionDef

A PrimDef is one of:
- ComparisonDef

An IsClsDef is one of:
- IsBooleanDef

A BSLExpr is one of:
- And
- Boolean
- FunctionApplication
- If
- Num
- Variable



Parser.
8.  Document which kind of P-expressions become which kind of ASTs. Do it in 2 columns.

BOTH:
9. Also write down the subset of S-expressions for which the parse will construct an AST.

HINT to 1:  An S-expression is ...
   ‘(‘ token …
        [And yes, I wrote this down for you when I launched you on the reader.]

Hint to 9:
   A Program consists of a DefSeq followed by an Expr.
   A DefSeq consists of a Def followed by a DefSeq — or nothing
  A Def is (define Head Expr)


Notes:

-- The parser will create an AST for any p-expression that does not contain context free errors.

-- Parser catches context free errors only.
   EX: A parser will not catch the following error: ['define', ['add', 'x', 'x', 'z'], ['+', 1, 3]]
       because it is not context free. It will catch the following error: ['define', ['f', 'x', 1, 'y'], 42]
       because we know that we do not need context to determine that function arguments cannot be numbers.

-- For a given function in the parser, the function could return  return false or raise an exception.

-- A function raises an exception if the parser cannot produce a valid AST from the given p-expression using any
    of the functions in the parser.
    EX: expr-parser will raise an exception here: [+, +, +] since we know that the list of parameters to a function
        application must be a list of valid BSLExpressions, without needing context.

-- A function will produce false if it cannot parse the expression but does not have enough information to determine
   if the given p-expression can be parsed.
   EX: [1, '+', 1]



