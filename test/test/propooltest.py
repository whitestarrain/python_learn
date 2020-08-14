from multiprocessing import Pool
import os,random,time

def worker(i):
    print("进程号为%d,资源为%d" %( os.getpid(),i))
    time.sleep(random.random()*2)

def main():
    p = Pool(3)
    for i in range(0,10):
        p.apply_async(worker,(i,))
    p.close()
    p.join()

if __name__ == "__main__":
    main()