class SqueakyClean {
    static String clean(String identifier) {
        StringBuilder sb = new StringBuilder();
        char[] chars = identifier.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ' ') {
                sb.append('_');
            } else if(chars[i] == '\0' || chars[i] == '\r' || chars[i] == '\n' || chars[i] == '\t' || chars[i] == '\u007F') {
                sb.append("CTRL");
            } else if(chars[i] == '-') {
                if (Character.isAlphabetic(chars[i + 1]) && (chars[i + 1] < 'α' || chars[i + 1] > 'ω') && !Character.isDigit(chars[i + 1])) {
                    sb.append(Character.toUpperCase(chars[i + 1]));
                }
                i++;
            } else if (Character.isAlphabetic(chars[i]) && (chars[i] < 'α' || chars[i] > 'ω') && !Character.isDigit(chars[i])) {
                sb.append(chars[i]);
            }
        }

        return sb.toString();
    }
}
