
; Brandon Jun // COMSC 078 // Programming in Scheme

(define (cube x)

  (*
    x
    x
    x
  )

)

(define (sum-integers a b)

  (if (> a b)
  0
  ; else
  (+
    a
    (sum-integers (+ a 1) b)
    )
  )
)

(define (sum-cubes a b)

  (if (> a b)
    0
    ; else
    (+
      (cube a)
      (sum-cubes (+ a 1) b)
      )
  )
)

(define (pi-sum n)

  (if (< n 1)
    0
    ; else
    (+
      (/ 8.0
        (*
          (- (* 4 n) 3)
          (- (* 4 n) 1)
          )
        )
      (pi-sum (- n 1))
      )
  )
)

(define (sum-prime f lower upper)

  (if (> lower upper)
    0
    ; else
    (+
      (f lower)
      (sum-prime f (+ lower 1) upper)
      )
  )
)

(define (pi-term k)
  (/ 8.0 (* (- (* 4 k) 3) (- (* 4 k) 1))))

(display "Showing cube x: 10 -> ")
(display (cube 10))
(newline) ; 1000

(display "Showing sum-integers: 1-10 -> ")
(display (sum-integers 1 10))
(newline) ; 55

(display "Showing sum-cubes: 1-5 -> ")
(display (sum-cubes 1 5))
(newline) ; 225

(display "pi-sum 100 -> ")
(display (pi-sum 100))
(newline) ; ~3.137

(display "Showing sum-prime: cubes 1-5 -> ")
(display (sum-prime cube 1 5))
(newline) ; 225

(display "Showing sum-prime: pi-sum 1-100 -> ")
(display (sum-prime pi-sum 1 100))
(newline) ; ~311.597