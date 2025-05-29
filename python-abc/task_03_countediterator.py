class CountedIterator:
    """
    A custom iterator that wraps around any iterable and keeps track
    of how many items have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and counter.
        :param iterable: Any iterable object (e.g., list, tuple, set).
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """
        Return the next item and increment the counter.
        Raise StopIteration when done.
        """
        item = next(self.iterator)  # This raises StopIteration when needed
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated over so far."""
        return self.count


# ✅ Test example
if __name__ == "__main__":
    data = [10, 20, 30, 40]
    ci = CountedIterator(data)

    print("Iterating:")
    for item in ci:
        print(f"Item: {item} | Count: {ci.get_count()}")

    print("\nFinal count:", ci.get_count())  # Should print 4
