object ResistorColor {

    fun colorCode(input: String): Int {
        when (input) {
            "black" -> return 0
            "brown" -> return 1
            "red" -> return 2
            "orange" -> return 3
            "yellow" -> return 4
            "green" -> return 5
            "blue" -> return 6
            "violet" -> return 7
            "grey" -> return 8
            "white" -> return 9
            else -> return -1
        }
    }

    fun colors(): List<String> {
        return listOf("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
    }

}
