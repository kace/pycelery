# pycelery

## celery flower
sudo pip install flower

# Add the rabbitmq_management plugi
rabbitmq-plugins enable rabbitmq_management

# Start a flower instance with persistence
celery flower -A execute_test --bker=amqp://guest@localhost:5672// --persistent=True --db=flower.db

# Start a worker with 2 concurrent threads
celery -A execute_test worker --loglevel=info -c 2

# Kill celery processes include flower
ps auxww | grep 'celery' | awk '{print $2}' | xargs kill -9
