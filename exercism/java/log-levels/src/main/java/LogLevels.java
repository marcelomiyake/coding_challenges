public class LogLevels {

    public static String message(String logLine) {
        return logLine
                .replace(new StringBuilder("[").append(logLevel(logLine).toUpperCase()).append("]: ").toString(), "")
                .replace("\r", "")
                .replace("\n", "")
                .replace("\t", "")
                .trim();
    }

    public static String logLevel(String logLine) {
        return logLine.substring(logLine.indexOf("[") + 1, logLine.indexOf("]")).toLowerCase();
    }

    public static String reformat(String logLine) {
        return new StringBuilder(message(logLine)).append(" (").append(logLevel(logLine)).append(")").toString();
    }
}

