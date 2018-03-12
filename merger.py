fout=open("merge_yes.csv","a")   #file name to which you have to merge
f = open("Not_Known.csv","r+")		#filename which you want to merge,do it for all files 
next(f)
for line in f:
         fout.write(line)
f.close() 
fout.close()
