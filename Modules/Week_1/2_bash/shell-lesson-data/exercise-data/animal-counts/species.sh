# Script to find unique species in csv files where species is the second data
# This script accepts any number of file names as command line arguments
# Usage: bash species.sh one_or_more_filenames

# Loop over all files
for file in $@
do
echo "Unique species in $file:"
cut -d , -f 2 "$file" | sort | uniq
done
