# concurrent programming
# asynchronous 

# GIL -> Global intrepretor lock 
# multi threading and multi processing 

# threading is used to run things concurrently.

# heavy task
# CPU bound -> using calculations. (Avoid multi threading, use multi processing)
# IO bound -> reading a lot of files, writing, good network, api , db write (multi threading)

# creates an illusion that it runs at the same time.

# During IO wait it proceeds to the next line/thread execution.



# import time
# print('program execution ------ start ----------')
# start_time = time.time()

# def sample(name,seconds):
#     print('{} - sample going to sleep for {}'.format(name,seconds))
#     time.sleep(seconds)
#     print('{} - sample done.....'.format(name))


# sample('call-1',2)
# sample('call-2',2)



# end_time = time.time()

# time_taken = end_time - start_time
# print('time taken - {} (s)'.format(round(time_taken,2)))
# print('program execution ------ end ----------')





#------------- sample 2 ---------------------------------


import threading
import time
print('program execution ------ start ----------')
start_time = time.time()

def sample(name,seconds):
    print('{} - sample going to sleep for {}'.format(name,seconds))
    time.sleep(seconds)
    print('{} - sample done.....'.format(name))


# sample('call-1',2)
# sample('call-2',3)

t1 = threading.Thread(target=sample, args=['call-1',2] )
t2 = threading.Thread(target=sample, args=['call-2',3] )

t1.start()
t2.start()

t1.join()
t2.join()


end_time = time.time()

time_taken = end_time - start_time
print('time taken - {} (s)'.format(round(time_taken,2)))
print('program execution ------ end ----------')