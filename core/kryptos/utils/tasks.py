import os
from rq import Connection, Queue
import redis
from kryptos.settings import DEFAULT_CONFIG, get_from_datastore


REDIS_HOST = os.getenv('REDIS_HOST', 'redis-19779.c1.us-central1-2.gce.cloud.redislabs.com')
REDIS_PORT = os.getenv('REDIS_PORT', 19779)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None) or get_from_datastore('REDIS_PASSWORD', 'production')

CONN = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def queue_notification(msg, telegram_id):
    with Connection(CONN):
        q = Queue('updates')
        q.enqueue(
            'updater.send_notification',
            msg=msg,
            telegram_id=telegram_id
        )


def enqueue_ml_calculate(df_current, name, idx, current_datetime, df_final, **kw):
    df_current_json = df_current.to_json()
    df_final_json = df_final.to_json()
    with Connection(CONN):
        q = Queue('ml')
        return q.enqueue(
            'worker.calculate',
            args=[df_current_json, name, idx, current_datetime, df_final_json],
            kwargs=kw,
            timeout=str(DEFAULT_CONFIG['MINUTE_FREQ']) + 'm'  # allow job to run for full iteration
        )


def enqueue_ml_analyze(namespace, name, df_final, df_results, data_freq, extra_results):
    df_final_json = df_final.to_json()
    df_results_json = df_results.to_json()
    with Connection(CONN):
        q = Queue('ml')
        return q.enqueue(
            'worker.analyze',
            args=[namespace, name, df_final_json, df_results_json, data_freq, extra_results],
            timeout=str(DEFAULT_CONFIG['MINUTE_FREQ']) + 'm'  # allow job to run for full iteration
        )
