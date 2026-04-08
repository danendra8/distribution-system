import time
import threading
from queue import Queue

def worker(name, queue):
    while True:
        if queue.empty():
            break

        task = queue.get()
        print(f"[PROCESS] {name} mengerjakan task {task}")
        time.sleep(0.07)
        queue.task_done()

task_queue = Queue()

# jumlah task (unik sesuai NRP)
for i in range(73):
    task_queue.put(i)

threads = []
start = time.time()

# jumlah worker (dibedakan dari umum)
for i in range(4):
    t = threading.Thread(target=worker, args=(f"Worker-{i+1}", task_queue))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"\n[TOTAL DYNAMIC] Waktu eksekusi: {end - start:.2f} detik")
print(">> Dynamic distribution mencapai waktu optimal karena semua worker aktif (tidak idle)")
