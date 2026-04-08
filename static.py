import time
import threading

def worker(name, tasks):
    print(f"[START] {name} memproses {len(tasks)} task")
    start = time.time()

    for t in tasks:
        time.sleep(0.07)  # delay beda (biar unik)

    end = time.time()
    print(f"[DONE] {name} selesai dalam {end - start:.2f} detik")

# jumlah task (sesuai NRP biar unik)
tasks = list(range(73))

# pembagian uneven (40% - 35% - 25%)
w1_tasks = tasks[:29]     # ~40%
w2_tasks = tasks[29:55]   # ~35%
w3_tasks = tasks[55:]     # ~25%

t1 = threading.Thread(target=worker, args=("Worker A", w1_tasks))
t2 = threading.Thread(target=worker, args=("Worker B", w2_tasks))
t3 = threading.Thread(target=worker, args=("Worker C", w3_tasks))

start_total = time.time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end_total = time.time()

print(f"\n[TOTAL STATIC] Waktu eksekusi: {end_total - start_total:.2f} detik")
print(">> Evaluasi: cek apakah waktu tiap worker seimbang (ideal distribution)")
