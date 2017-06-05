#lang racket

(define timestart (current-inexact-milliseconds))

(define (mySum L)
  (apply + L))

(define (is-beautiful num position)
  (cond
    ((or
      (eq? (modulo num position) 0)
      (eq? (modulo position num) 0))
     #t)
    (else #f))
)

(define (compute nums position)
  (cond
    ((eq? position 1) 1)
    (else
      (mySum
       (map
        (lambda (num)
         (cond
          ((is-beautiful num position) (compute (remove num nums) (- position 1)))
          (else 0)))
        nums))))
)

;(display (compute (list 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15) 15))

(define (countArrangement N)
  (compute (range 1 (+ N 1)) N))

(countArrangement 15)
(display (- (current-inexact-milliseconds) timestart))