import requests as re
import threading as th
import time

def thred1():
    count = 0
    max_count = 1000

    while count < max_count:
        print(f"###########################:: {count} of {max_count} ::#####################################")
        print("Thread 1 is executing....")
        re.get("http://cyan-mirrors-smile-34-86-111-132.loca.lt").text
        count +=1
        time.sleep(3)

def thred2():
    count = 0
    max_count = 1000

    while count < max_count:
        print(f"###########################:: {count} of {max_count} ::#####################################")
        print("Thread 2 is executing....")
        re.get("http://cyan-mirrors-smile-34-86-111-132.loca.lt").text
        count +=1
        time.sleep(3)

def thred3():
    count = 0
    max_count = 1000

    while count < max_count:
        print(f"###########################:: {count} of {max_count} ::#####################################")
        print("Thread 3 is executing....")
        re.get("http://cyan-mirrors-smile-34-86-111-132.loca.lt").text
        count +=1
        time.sleep(3)

def thred4():
    count = 0
    max_count = 1000

    while count < max_count:
        print(f"###########################:: {count} of {max_count} ::#####################################")
        print("Thread 4 is executing....")
        re.get("http://cyan-mirrors-smile-34-86-111-132.loca.lt").text
        count +=1
        time.sleep(3)

def thred5():
    count = 0
    max_count = 1000

    while count < max_count:
        print(f"###########################:: {count} of {max_count} ::#####################################")
        print("Thread 5 is executing....")
        re.get("http://cyan-mirrors-smile-34-86-111-132.loca.lt").text
        count +=1
        time.sleep(3)

def thred6():
    count = 0
    max_count = 1000

    while count < max_count:
        print(f"###########################:: {count} of {max_count} ::#####################################")
        print("Thread 6 is executing....")
        re.get("http://cyan-mirrors-smile-34-86-111-132.loca.lt").text
        count +=1
        time.sleep(3)

def thred7():
    count = 0
    max_count = 1000

    while count < max_count:
        print(f"###########################:: {count} of {max_count} ::#####################################")
        print("Thread 7 is executing....")
        re.get("http://cyan-mirrors-smile-34-86-111-132.loca.lt").text
        count +=1
        time.sleep(3)


t1 = th.Thread(target=thred1)
t2 = th.Thread(target=thred2)
t3 = th.Thread(target=thred3)
t4 = th.Thread(target=thred4)
t5 = th.Thread(target=thred5)
t6 = th.Thread(target=thred6)
t7 = th.Thread(target=thred7)

reads = [t1,t2,t3,t4,t5,t6,t7]

for i in reads:
    i.start()

