#import adiciona novos módulos ao programa. 
#Os módulos tem funções e objetos que podem ser reutilizados
import sys #provê de acesso ao sistema
import time #disponibiliza, dentre outras coisas, a função sleep, que faz o processo atual dormir por um tempo.

for i in range(100):
	if i % 2 == 0:
		print('\r', end='')
		print('/ ', i, end=' ')
	else:
		print('\r', end='')
		print('\\ ', i, end=' ')
	#sys.stdout.flush()
	time.sleep(0.4)
print('the end')
