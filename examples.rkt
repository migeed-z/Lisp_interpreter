
;; definitions 
(define (f x) x)
(define (g) (+ (f 4) 2))
(define (z x y) (+ x y))

;; expressions 
(z (if0 (g) 42 (f 4)) 2)

(posn 3 4)
(posn (posn 3 4) 5)
(posn (posn 3 4) (posn 5 6))
