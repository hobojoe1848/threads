
import pytest
from src.threading_manager import ThreadSafeList
from threading import Lock


def test_passes():
    assert True


class TestThreadSafeList:
    def test_init(self):
        obj = ThreadSafeList()

        ## Test object's initial state
        assert isinstance(obj.data, list)
        assert len(obj.data) == 0

    def test_lock_functionality(self):
        obj = ThreadSafeList()
        
        ## Test that the lock can be acquired
        assert obj.lock.acquire(blocking=False)  # Should be able to acquire the lock
        
        ## Test that the lock can't be acquired again while held
        assert not obj.lock.acquire(blocking=False)  # Should not be able to acquire the lock again
        
        ## Release the lock
        obj.lock.release()
        
        ## Test that the lock can be acquired again after release
        assert obj.lock.acquire(blocking=False)  ## Should be able to acquire the lock again
        obj.lock.release()  ## Clean up by releasing the lock