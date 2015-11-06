PARSER

-- P-expression -> AST, False, or raise an Exception

BSL_Pexpr is one of:
Numbers
Function Application
And expr
if expr
Boolean expr

P-expressions accepted by parsers:

Numbers
Boolean expr: 'true'/'false'
Struct definitions: ['define-struct', String, [String]]
Selector: ['structname-structfield', ['make-structname', *BSL_Pexpr]] 
Predicate: ['structname?', ['make-structname', *BSL_Pexpr]]
Function Definition: ['define', *String, [BSL_Pexpr]] 
Function Application: [String, *BSL_Pexpr]
And expr: ['and', *Boolean]
if expr: ['if', BSL_Pexpr, BSL_Pexpr, BSL_Pexpr]

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
- PrimitiveFunc

An IsClsDef is one of:
- IsBooleanDef

A BSLExpr is one of:
- And
- Boolean
- FunctionApplication
- If
- Num
- Variable


|    P-expressions     |         AST         |
|----------------------|---------------------|
| Number               | Num                 |
| Struct definitions   | StructDef           |
| Make struct          | FunctionApplication |
| Selector             | FunctionApplication |
| Predicate            | FunctionApplication |
| Function Definition  | FuncDef             |
| Function Application | FuncApplication     |
| And exp              | And                 |
| Boolean expr         | Boolean             |
| If expr If           |                     |


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



