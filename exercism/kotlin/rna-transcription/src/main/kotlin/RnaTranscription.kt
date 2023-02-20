fun transcribeToRna(dna: String): String {
    var result = ""
    dna.forEach {
        when (it) {
            'G' -> result = result.plus('C')
            'C' -> result = result.plus('G')
            'T' -> result = result.plus('A')
            'A' -> result = result.plus('U')
        }
    }
    return result

}