import multiprocessing as mp

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

def calculate_fibonacci(start, end):
    results = []
    for i in range(start, end):
        results.append(fibonacci(i))
    return results

def main():
    num_processes = mp.cpu_count()
    total_terms = 1000

    # Divide el trabajo de manera dinámica entre los procesos
    work_per_process = total_terms // num_processes
    remainder = total_terms % num_processes

    with mp.Pool(processes=num_processes) as pool:
        tasks = []
        start = 0
        for _ in range(num_processes):
            end = start + work_per_process
            if remainder > 0:
                end += 1
                remainder -= 1
            tasks.append(pool.apply_async(calculate_fibonacci, args=(start, end)))
            start = end
        
        all_results = []
        for task in tasks:
            all_results.extend(task.get())

    print(f"Los primeros 1000 términos de la secuencia de Fibonacci son:")
    print(", ".join(map(str, all_results)))

if __name__ == "__main__":
    main()
