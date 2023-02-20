object Hamming {

    fun compute(leftStrand: String, rightStrand: String): Int {
        var hammingDistance = 0
        if (leftStrand.length != rightStrand.length) {
            throw IllegalArgumentException("left and right strands must be of equal length")
        }

        for (i in leftStrand.indices) {
            if (leftStrand.get(i) !== rightStrand.get(i)) {
                hammingDistance++
            }
        }
        return hammingDistance
    }
}
