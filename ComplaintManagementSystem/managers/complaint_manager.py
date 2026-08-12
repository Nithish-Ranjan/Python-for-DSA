from .queue_manager import QueueManager


class ComplaintManager:
    """Application service connecting models/DSA structures with persistence."""
    def __init__(self, database): self.db=database; self.queue=QueueManager(); self.refresh()
    def refresh(self): self.queue.rebuild(self.db.get_complaints())
    def create(self, data, actor):
        cid=self.db.add_complaint(data, actor); self.refresh(); return cid
    def update(self, cid, changes, actor):
        old=next((x for x in self.db.get_complaints() if x["id"]==cid), None); self.db.update_complaint(cid, changes, actor); self.queue.push_undo("update", old); self.refresh()
    def delete(self, cid):
        old=self.db.delete_complaint(cid)
        if old: self.queue.push_undo("delete", old); self.refresh()
    def undo(self, actor):
        item=self.queue.pop_undo()
        if not item: return False
        action, data=item
        if action=="delete":
            data.pop("resolved_at", None); data.pop("id", None); data.pop("date", None); self.create(data, actor)
        elif action=="update": self.db.update_complaint(data["id"], data, actor); self.refresh()
        return True
