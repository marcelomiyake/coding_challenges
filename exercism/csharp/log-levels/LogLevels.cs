using System;

static class LogLine
{
    public static string Message(string logLine)
    {
        return logLine
            .Replace($"[{LogLevel(logLine).ToUpper()}]: ", "")
            .Replace("\r", "")
            .Replace("\n", "")
            .Replace("\t", "")
            .Trim();
    }

    public static string LogLevel(string logLine)
    {
        return logLine.Substring(logLine.IndexOf("[") + 1, logLine.IndexOf("]") - 1).ToLower();
    }

    public static string Reformat(string logLine)
    {
        return $"{Message(logLine)} ({LogLevel(logLine)})";
    }
}
