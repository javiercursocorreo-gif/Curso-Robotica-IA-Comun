on run argv
    set posixIn to item 1 of argv
    set posixOut to item 2 of argv
    set macIn to POSIX file posixIn as text
    set macOut to POSIX file posixOut as text
    
    tell application "Microsoft PowerPoint"
        activate
        open file macIn
        save active presentation in file macOut as save as PDF
        close active presentation
    end tell
end run
