(ns bob)

(defn response-for [s]
  (let [t (clojure.string/trim s)]
    (cond (= t "") "Fine. Be that way!"
          (and (= (subs t (- (.length t) 1)) "?")
               (= (.toUpperCase t) t)
               (not (nil? (re-find (re-pattern "[a-zA-Z]") t)))) "Calm down, I know what I'm doing!"
          (= (subs t (- (.length t) 1)) "?") "Sure."
          (and (= (.toUpperCase t) t)
               (not (nil? (re-find (re-pattern "[a-zA-Z]") t)))) "Whoa, chill out!"
          :else "Whatever."))
  )
