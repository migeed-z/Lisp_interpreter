# Lisp_interpreter

STEP 0:
 Definition of BSL surface syntax
 BSL is one of:
   -- BSLDef 
   -- BSLExp
    
 BSLDef is one of:
    -- FunctionDefinition
    -- StructDefinition
    -- ConstructorDef
    -- SelectorDef
    -- PredicateDef

 StructDefinition is:
    -- StructDefinition(struct-name, [params])
    
     EX:
     StructDefinition(struct-name, [x, y, z])
     In the scope we now extend name with StructDefinition(struct-name, [x, y, z])


     Upon creating a StructDefinition, the following function definitions are initialized: ** currently have to call function **
        -- ConstructorDef
        -- SelectorDef (one for each parameter)
        -- PredicateDef
              
 BSLExp is one of:
    -- Num
    -- Variable
    -- Operation
    -- if0
    -- EMPTY -- need value for it and parsing - TODO
    -- SOMETHING STRING LIKE and STRING? - TODO
    -- FunctionApplication
    
 Operation is one of:
    -- Add
    -- Subtract
    -- Multiply
    -- Divide

   
STEP 1:
 The READER will consume the text a programmer types into the console and produce a P-expression.

A P-expression is one of:
 - string, represents a symbol in BSL
 - number
 - [P-expression, ..., P-expression]

STEP 2 a:
 The PARSER consumes P-expressions and produces pre-BSL-expression, it's a BSL-expression but with errors

 NAIVE approach
 parser : P-expression -> [Maybe BSLexpr]

A BSLexpr is one of:
  Num(number)
  Var(string)
  Add([Listof BSLexpr])
  Mul([BSLexpr])
  Sub([BSLexpr])
  Div([BSLexpr])
  App(string,[BSLexpr])

 A FuncDef is:
   Def(string,string,BSLexpr)

A P-expression/e is one of:
 - string, represents a symbol in BSL
 - number
 - Error("an explanation of the error")
 - [P-expression/e, ..., P-expression/e]

 WORKING approach
 parser : P-expression -> P-expression/e
 translate given p-expression into p-expression/e with Error where it is not a proper BSL 'thing'

A pre-BSL-expression is one of:
 - string, represents a symbol in BSL
 - number
 - [pre-BSL-expression, ..., pre-BSL-expression]
 but all expressions represent scope-perfect BSL programs

STEP 2 b:
 The "checker" consumes pre-BSL-expressions and discovers scope errors such as (define (x x) x) or (define (f x x) 10)
 Imagine BSL with TYPES. ***** type systems research *****

 checker : p-expression/e ... other arguments ... -> p-expression/e
 check more properties and insert more Error nodes when find errors

 STEP 2 c:
 if p-expression/e does NOT contain ERROR, it is a good BSL representation
 otherwise, tell programmer about errors

 if it is a good BSL expression, generate BSL-expression then go to step 3

STEP 3:
 The BSLexpression .eval method determines the value of each input expression.
 Extend BSL with lambda, if, assignment statement, non-local control (Python: generator), ... (see node.js)
    *** language design ****

 a Value is one of:
 - Python numbers
 - Structure("struct-name", [("param", value)])
 - True
 - False
   
  Once we have a make-struct, we create a structure with param-value tuples

 STEP 4: implement this properly

