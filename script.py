N=4
'''
with open("file.tex") as myfile:
    head = [next(myfile) for x in range(N)]
    print(next(myfile))
print(head[0])

y=head[0].replace('3','5')
print(y)
'''
from tempfile import mkstemp
from shutil import move, copymode


import os as os

def replace(file_path, DICT):
    #Create temp file
    for i in range(len(DICT[0])-1):
        count=0
        fh, abs_path = mkstemp()
        with os.fdopen(fh,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    if (count<N):
                        new_file.write(line.replace(
                            str(DICT[count][i]), 
                            str(DICT[count][i+1])))
                    else:
                        new_file.write(line)
                    count=count+1
        #Copy the file permissions from the old file to the new file
        copymode(file_path, abs_path)
        #Remove original file
        os.remove(file_path)
        #Move new file
        move(abs_path, file_path)
        outfile='out'+str(i)
        os.system('pdflatex -jobname=out'+outfile+' -output-directory pdf file.tex ')
    
    

DICT={
        0:[49,9,9,19,29,39,49],
        1:[48,9,8,18,28,38,48],
        2:[47,9,7,17,27,37,47],
        3:[46,9,6,16,26,36,46]
            }

    
replace("file.tex",DICT)


