
start_worker:
	celery -A execute_test worker --loglevel=info -c 2 &

.PHONY: clean
clean:
	rm *.pyc
