from collections import deque     # we use deque only for O(1) queue ops

class StackWithTwoQueues:
    """LIFO stack realised with two FIFO queues q1 (main) and q2 (helper)."""
    
    def __init__(self) -> None:
        self.q1: deque[int] = deque()   # primary queue - top of the stack is at the *front*
        self.q2: deque[int] = deque()   # secondary queue (empty except during push)

    # ---------- core stack operations ----------

    def push(self, value: int) -> None:
        """O(n) – enqueue value, then rotate previous elements behind it."""
        self.q2.append(value)               # enqueue new item in helper queue
        while self.q1:                      # move all old items after the new one
            self.q2.append(self.q1.popleft())
        # swap queues: q2 becomes the new main, q1 is emptied helper
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """O(1) – dequeue from front of main queue (top of stack)."""
        if not self.q1:
            raise IndexError("pop from empty stack")
        return self.q1.popleft()

    def peek(self) -> int:
        """O(1) – look at the element on top without removing it."""
        if not self.q1:
            raise IndexError("peek from empty stack")
        return self.q1[0]

    def is_empty(self) -> bool:
        """O(1) – True when stack has no elements."""
        return not self.q1

    def __len__(self) -> int:              # optional, stack size
        return len(self.q1)