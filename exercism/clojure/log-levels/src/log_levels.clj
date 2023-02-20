(ns log-levels)

(defn message
  "Takes a string representing a log line
   and returns its message with whitespace trimmed."
  [s]
  (.trim (subs s (+ 1 (.indexOf s ":"))))
  )

(defn log-level
  "Takes a string representing a log line
   and returns its level in lower-case."
  [s]
  (.toLowerCase (subs s (+ 1 (.indexOf s "[")) (.indexOf s "]")))
  )

(defn reformat
  "Takes a string representing a log line and formats it
   with the message first and the log level in parentheses."
  [s]
  (str (message s) " (" (log-level s) ")")
  )
