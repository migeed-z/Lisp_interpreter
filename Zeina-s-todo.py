
#TODO:


# e is one of:
# -- n
# -- (+ e ... e)
# -- (* e ... e)
# -- x
# -- (x e)
# where
# -- x is a string
# -- n is a number

# d is:
# -- (define (x x) e

# if0 e-test e-then e-else : if e-test evaluates to 0, then evaluate e-then; otherwise evaluate e-else
#
# ** make sure BSL is type defined ** for all classes!
# & implement posn-y


#name must be string
#val must be one of:
# num, string, function def, posn, posn selector, func_app (should use BSLexpr or values? and should we in that case evaluate val first?)