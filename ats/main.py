from concurrent.futures import ThreadPoolExecutor, as_completed

# Sample function to process each ID (replace with your actual function)
def process_id(id):
    # Simulate a time-consuming operation
    import time
    time.sleep(1)  # Replace this with the actual processing logic
    return f"Result for {id}"

def process_ids_in_parallel(ids):
    results = []
    
    with ThreadPoolExecutor() as executor:
        # Submit all tasks to the executor
        future_to_id = {executor.submit(process_id, id): id for id in ids}
        
        # Process results as they complete
        for future in as_completed(future_to_id):
            id = future_to_id[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                print(f"ID {id} generated an exception: {exc}")
    
    return results

# Example usage
ids = [1, 2, 3, 4, 5]
results = process_ids_in_parallel(ids)
print(results)