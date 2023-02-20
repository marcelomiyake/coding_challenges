class Hamming {
  int distance(String leftStrand, String rightStrand) {
    var hammingDistance = 0;
    if (leftStrand.length != rightStrand.length) {
      throw new ArgumentError("strands must be of equal length");
    }

    for (var i = 0; i < leftStrand.length; i++) {
      if (leftStrand.substring(i, i + 1) != rightStrand.substring(i, i + 1)) {
        hammingDistance++;
      }
    }
    return hammingDistance;
  }
}
