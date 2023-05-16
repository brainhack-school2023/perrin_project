# Give the name of the file with the most lines in aa directory with the extension
wc -l $1/*.$2 | sort -n | tail -n 2 | head -n 1
