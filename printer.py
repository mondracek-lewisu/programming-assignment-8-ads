from Queue import Queue
import random
import time

printer_queue = Queue(10)
for i in range(1, 11):
    printer_queue.enqueue((i, random.randint(1, 100)))

while not printer_queue.isEmpty():
    record = printer_queue.dequeue()
    print(f"Printing document {record[0]} with {record[1]} page(s)...")
    start_time = time.time()
    time.sleep((60/18)*record[1])
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Document {record[0]} with {record[1]} page(s) printed in {elapsed_time:.2f} seconds.")

print("All documents have been printed.")