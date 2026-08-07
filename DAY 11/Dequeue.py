'''implement dequeue operation in queue'''

queue=list(map(int,input("enter elememts:").split()))
if len(queue)==0:
    print("queue underflow")
else:
    removed=queue.pop(0)
    print(removed)
    print(queue)