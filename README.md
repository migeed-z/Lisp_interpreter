# Lisp_interpreter

> (define (f x) x)
> (define (g x) (+ x 1))
> (f (g 10))
11
> (g (g 10))
12

STEP 0:
 Definition of BSL surface syntax
 BSL is one of:
   -- BSLDef 
   -- BSLExp

  BSLDef is
    -- (define-struct name (name ...)) - TODO
    -- (define name BSLExp) - 
    -- (define (name name ...) BSLExp) -
  BSLExp is one of:
    -- Number
    -- Name
    -- (+ BSLExp ...)
    -- (* BSLExp ...)
    -- (/ BSLExp BSLExp ...)
    -- (- BSLExp BSLExp ...)
    -- (make-posn BSLExp BSLExp) -
    -- (posn-left BSLExp) -
    -- (posn-right BSLExp) -
    -- (if BSLExp BSLexp BSLExp) -
    -- EMPTY -- need value for it and parsing -
    -- (Name BSLExp ...) - ?????
    -- (posn? BSLexpr) - TODO
    -- (number? BSLexpr) - TODO
    -- SOMETHING STRING LIKE and STRING? - TODO

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

    -- if expression
    -- cons
    -- define-struct
    -- assignment statement and loop

 STEP 4: implement this properly

