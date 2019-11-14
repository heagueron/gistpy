import sys


old_filename = sys.argv[1]
new_filename = sys.argv[2]

old_file = open(old_filename)
# Get the old file rows via comprehension list
rows = [
    line.split('|')
    for line in old_file.read().splitlines()
]

new_file = open(new_filename, mode='wt', newline='\r\n')

print( "\n".join(",".join(row) for row in rows), file=new_file )

old_file.close()
new_file.close()