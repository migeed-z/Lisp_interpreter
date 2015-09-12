READER

-- S-expression -> P-expression

An S-expression has the following textual representation:
- Token
- '(' followed by Seq

A Seq is one of:
- ')'
- S-expression followed by Seq

A Token is one of:
- Any sequence of characters not including '(', ')' up to an Empty string

An P-expression is one of
- Atom
- [P-expressions]

An Atom is:
- Any sequence of characters 


|     S-expression     |  P-expression   |
|----------------------|-----------------|
| Token                | Atom            |
| '(' followed by Seq  | [P-expressions] |


Notes:
A p-expression must have the following properties:
-- Well-balanced parens
   EX: (). Reader will continue to read if parens are not balanced.
-- The expression must be well-formed
   EX: ('+', a, b, c) is well-formed. )( is not, and Reader will raise an exception.









