on run argv
    tell application "Keynote"
        activate
        set theFile to POSIX file (item 1 of argv)
        set theOutFile to POSIX file (item 2 of argv)
        open theFile
        set theDoc to document 1
        export theDoc to file theOutFile as PDF
        close theDoc
    end tell
end run
