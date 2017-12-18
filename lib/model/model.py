import uuid
import recommender
import sched
import time

_session_dict = {}

def start_new_session(_session_id):
    _session_dict[_session_id] = recommender.Recommender()

def end_session(_session_id):
    del _session_dict[_session_id]

def check_expired_sessions():
    for session_id, session in zip(*_session_dict.items()):
        if time.time() - session.complete > 1800:
            end_session(session_id)

s = sched.scheduler(time.time, time.sleep)
s.enter(300, 1, check_expired_sessions)
s.run()

