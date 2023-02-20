object ResistorColorDuo {

    fun value(vararg colors: Color): Int {
        return colorCode(colors[0]) * 10 + colorCode(colors[1])
    }

    fun colorCode(input: Color): Int {
        when (input) {
            Color.BLACK -> return 0
            Color.BROWN -> return 1
            Color.RED -> return 2
            Color.ORANGE -> return 3
            Color.YELLOW -> return 4
            Color.GREEN -> return 5
            Color.BLUE -> return 6
            Color.VIOLET -> return 7
            Color.GREY -> return 8
            Color.WHITE -> return 9
        }
        return -1
    }
}
