Interpreter
AST -> Value

A Value is one of:
- Boolean
- Num
- Structure

Subset of AST for which the interpreter produces a Value

|         AST          |  Value  |  
|----------------------|---------|
| And                  | Boolean |  
| Boolean              | Boolean |  
| Num                  | Num     |  
| FunctionApplication  | Value   |  
| If                   | Value   | 

Values produced from calling the eval_internal() method on a FunctionApplication based on the given Definition

|    Definition    |    Value    |
|------------------|-------------|
| PrimitiveFunc    | Num/Boolean |
| IsClsDef         | Boolean     |
| PredicateDef     | Boolean     |
| SelectorDef      | Value       |
| ConstructorDef   | Structure   |






