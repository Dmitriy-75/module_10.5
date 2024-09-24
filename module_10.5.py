import multiprocessing
import time

def  read_info(name):
    all_data = []
    f = open(name, encoding="utf-8")
    for line in f:
        all_data.append(f.readline())
    f.close()

filenames = [f'file {number}.txt' for number in range(1, 5)]

start = time.time()
for file in filenames:
    read_info(file)
end = time.time()
res = end-start
print(f'{res} сек, линейный')

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = time.time()
        pool.map(read_info, filenames)
        end = time.time()
    res = end - start
    print(f'{res} сек, многопроцессорный')


