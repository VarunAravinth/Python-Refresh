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
# print('time taken - {} (s)'.format(round(time_taken,5)))
# print('program execution ------ end ----------')





#------------- sample 2 ---------------------------------

# import threading
# import time
# print('program execution ------ start ----------')
# start_time = time.time()

# def sample(name,seconds):
#     print('{} - sample going to sleep for {}'.format(name,seconds))
#     time.sleep(seconds)
#     print('{} - sample done.....'.format(name))


# # sample('call-1',2)
# # sample('call-2',3)

# t1 = threading.Thread(target=sample, args=['call-1',2] )
# t2 = threading.Thread(target=sample, args=['call-2',2] )

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# end_time = time.time()

# time_taken = end_time - start_time
# print('time taken - {} (s)'.format(round(time_taken,5)))
# print('program execution ------ end ----------')


#------------- sample 2.5 ---------------------------------

# import threading
# import time
# print('program execution ------ start ----------')
# start_time = time.time()

# def sample(name,seconds):
#     print('{} - sample going to sleep for {}'.format(name,seconds))
#     time.sleep(seconds)
#     print('{} - sample done.....'.format(name))


# threads = []
# # throw away variable - _
# for _ in range(1,4):
#     t1 = threading.Thread(target=sample, args=['call-1',2] )
#     t1.start()
#     threads.append(t1)


# for thread in threads:
#     thread.join()



# end_time = time.time()

# time_taken = end_time - start_time
# print('time taken - {} (s)'.format(round(time_taken,5)))
# print('program execution ------ end ----------')



# -------- sample 3 --------------------------------------------------
# newer way of threading. introduced from python 3.2
# called as thread Pool executor
# can get return values from a function - (cannot be done using threading module)
# you can easily switch between multi-processing and multi-threading

# from concurrent.futures import ThreadPoolExecutor
# import time
# print('program execution ------ start ----------')
# start_time = time.time()

# def sample(seconds):
#     print('sample going to sleep for {}'.format(seconds))
#     time.sleep(seconds)
#     return '{} - sample done.....'.format(seconds)


# with ThreadPoolExecutor() as executor:
#     t1 = executor.submit(sample,4)
#     t2 = executor.submit(sample,4)

#     print('result - ', t1.result())
#     print('result - ', t2.result())


# end_time = time.time()

# time_taken = end_time - start_time
# print('time taken - {} (s)'.format(round(time_taken,5)))
# print('program execution ------ end ----------')


#-------- sample 4 --------------------------------------------------


# from concurrent.futures import ThreadPoolExecutor, as_completed
# import time
# print('program execution ------ start ----------')
# start_time = time.time()

# def sample(seconds):
#     print('sample going to sleep for {}'.format(seconds))
#     time.sleep(seconds)
#     return '{} - sample done.....'.format(seconds)

# threads =[]
# with ThreadPoolExecutor() as executor:
#     for seconds in range(5,0,-1):
#         t = executor.submit(sample,seconds) # SUBMUT ORDER 5,4,3,2,1
#         threads.append(t)

#     for result in as_completed(threads):  # COMPLETED ORDER 1,2,3,4,5
#         print(result.result())
   


# end_time = time.time()

# time_taken = end_time - start_time
# print('time taken - {} (s)'.format(round(time_taken,5)))
# print('program execution ------ end ----------')


#-------- sample 5 --------------------------------------------------


# from concurrent.futures import ThreadPoolExecutor, as_completed
# import time
# print('program execution ------ start ----------')
# start_time = time.time()

# def sample(seconds):
#     print('sample going to sleep for {}'.format(seconds))
#     time.sleep(seconds)
#     return '{} - sample done.....'.format(seconds)


# with ThreadPoolExecutor() as executor:
#     li = [5,4,3,2,1]
#     threads = executor.map(sample,li)


#     for result in threads:  # COMPLETED ORDER 1,2,3,4,5
#         print(result)
   

# end_time = time.time()

# time_taken = end_time - start_time
# print('time taken - {} (s)'.format(round(time_taken,5)))
# print('program execution ------ end ----------')


# -------- sample 6 ---- Real time example -------------
# import requests
# import time
# from concurrent.futures import ThreadPoolExecutor, as_completed

# start_time = time.time()

# def get_data(url):
#     return requests.get(url).text

# threads = []
# with ThreadPoolExecutor() as executor:
#     result1 = executor.submit(get_data,'http://api.open-notify.org/iss-now.json')
#     result2 = executor.submit(get_data,'http://api.open-notify.org/astros.json')
#     result3 = executor.submit(get_data,'http://api.open-notify.org/astros.json')

#     threads.append(result1)
#     threads.append(result2)
#     threads.append(result3)

#     for thread in as_completed(threads):
#         print(thread.result())



# # print(get_data('http://api.open-notify.org/iss-now.json'))
# # print(get_data('http://api.open-notify.org/astros.json'))
# # print(get_data('http://api.open-notify.org/astros.json'))

# end_time = time.time()

# time_taken = end_time - start_time
# print('time taken - {} (s)'.format(round(time_taken,5)))
# print('program execution ------ end ----------')



# --------- multi-processing-------------------

# speeds up the program
# multiple processes run in parallel


# import multiprocessing
# import time
# print('program execution ------ start ----------')
# start_time = time.time()

# def sample(name,seconds):
#     print('{} - sample going to sleep for {}'.format(name,seconds))
#     time.sleep(seconds)
#     print('{} - sample done.....'.format(name))


# # sample('call-1',2)
# # sample('call-2',3)

# if __name__ == '__main__':
#     t1 = multiprocessing.Process(target=sample, args=['call-1',10] )
#     t2 = multiprocessing.Process(target=sample, args=['call-2',10] )

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()


#     end_time = time.time()

#     time_taken = end_time - start_time
#     print('time taken - {} (s)'.format(round(time_taken,5)))
#     print('program execution ------ end ----------')



from concurrent.futures import ProcessPoolExecutor
import time
print('program execution ------ start ----------')
start_time = time.time()

def sample(seconds):
    print('sample going to sleep for {}'.format(seconds))
    time.sleep(seconds)
    return '{} - sample done.....'.format(seconds)

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        t1 = executor.submit(sample,4)
        t2 = executor.submit(sample,4)

        print('result - ', t1.result())
        print('result - ', t2.result())


end_time = time.time()

time_taken = end_time - start_time
print('time taken - {} (s)'.format(round(time_taken,5)))
print('program execution ------ end ----------')
