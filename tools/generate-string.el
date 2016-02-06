(require 'dash)

(defun random-range (low high)
  (+ low (random (1+ (- high low)))))

(defun generate-char (ignore)
  (if (zerop (random 2))
      (random-range ?a ?z)
    (random-range ?A ?Z)))

(defun generate-string (string-length)
  (->> string-length
       (number-sequence 1)
       (-map #'generate-char)
       (apply #'string)))
