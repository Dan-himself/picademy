from time import sleep, time

sleep(5)

start = time()
print('Quick, press the enter key')
input()

reaction_time = time() - start
print('You took ', reaction_time, ' seconds')
