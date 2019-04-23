import os, shutil

FLOP_TO_SCAN = [1,2,4,8,16,32,64,128]
WORKING_SET_SIZE = [64, 128, 256]
THREADS = [1,2,3,4]

if __name__=="__main__":
    shutil.rmtree('output', ignore_errors=True)
    os.mkdir("output")
    for flop in FLOP_TO_SCAN:
        for size in WORKING_SET_SIZE:
            for thread_count in THREADS:
                os.system("./bin/gables {} {} {} > output/{}-FLOP-{}MB-{}-THREADS.gables".format(thread_count, flop, size, flop, size, thread_count))
                print("Finished {} flop, {} MB, {} threads".format(flop, size, thread_count))