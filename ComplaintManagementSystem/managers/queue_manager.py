import heapq


class QueueManager:
    """DSA showcase: heap priority queue plus FIFO waiting queue and undo stack."""
    WEIGHTS={"Critical":1,"High":2,"Medium":3,"Low":4}
    def __init__(self): self._priority=[]; self.waiting=[]; self.undo_stack=[]
    def rebuild(self, complaints):
        self._priority=[]
        for c in complaints:
            if c["status"] != "Resolved": heapq.heappush(self._priority, (self.WEIGHTS.get(c["priority"], 5), c["date"], c))
    def next_urgent(self): return self._priority[0][2] if self._priority else None
    def enqueue(self, complaint): self.waiting.append(complaint)
    def dequeue(self): return self.waiting.pop(0) if self.waiting else None
    def push_undo(self, action, payload): self.undo_stack.append((action, payload))
    def pop_undo(self): return self.undo_stack.pop() if self.undo_stack else None
