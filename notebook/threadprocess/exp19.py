# coding: utf8
import multiprocessing


def writer_proc(q):
    for i in range(0, 10):
        try:
            print i
            q.put(i)
        except:
            pass


def reader_proc(q):
    for i in range(0, 10):
        try:
            a = q.get()
            print a
        except:
            pass


if __name__ == '__main__':
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))
    writer.start()

    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()

    reader.join()
    writer.join()
