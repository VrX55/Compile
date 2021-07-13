# open source
import marshal
import os
import time
# color
################
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
################
pareasi="""
%s   ______                      _ __
  / ____/___  ____ ___  ____  (_) /__    ____  __  __  
 / /   / __ \/ __ `__ \/ __ \/ / / _ \  / __ \/ / / /   
/ /___/ /_/ / / / / / / /_/ / / /  __/ / /_/ / /_/ /   
\____/\____/_/ /_/ /_/ .___/_/_/\___(_) .___/\__, /   
%s{ %sM A R S H A L%s } %s  /_/              /_/    /____/ 
%s{ %sBy.Zar%s}
%s------------------------------------------------------
   %s     [ %sGithub: https://github.com/Zar-ID %s]
%s------------------------------------------------------%s
"""%(G,W,B,W,G,W,B,W,B,G,W,G,B,W)
try:
	os.system('clear')
	print pareasi
	path=raw_input("\033[1;32m[\033[1;31m/\033[1;32m]%s File Name: "%(W))
	x=open(path).read()
	m=compile(x,'','exec')
	v=marshal.dumps(m)
	d=open("Hore_"+path,'w')
	d.write('import marshal\n')
	d.write('exec(marshal.loads('+repr(v)+'))')
	d.close()
	time.sleep(2)
	print("\033[1;32m[\033[1;31m+\033[1;32m] Berhasil!!!:\033[1;37m Hore_"+path)
	print
except KeyboardInterrupt:
	print("\033[1;32m[\033[1;31m!\033[1;32m] \033[1;31muHmmm Ada Yang Salah...%s"%(W))
	exit()
