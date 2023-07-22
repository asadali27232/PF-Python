def counts(arr, key):
    count = arr.count(key)
    if count == 0:
        print(f"Element {key} is not present in {arr}.")
    else:
        print(f"Element {key} is present {count} times in {arr}")


arr = [1, 1, 1, 2, 3, 4, 5]
counts(arr, 1)
