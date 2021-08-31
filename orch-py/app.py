import redis 
from flask import Flask, request, Response

r = redis.Redis(host='localhost', port=6379, db=0)

app = Flask(__name__)

@app.route("/add", methods=['POST'])
def addTask() -> bool:
    inputData = request.form['inputData']
    model = request.form['model']

    key = "TASK/" +  str(r.incr("COUNTER"))
    print(key)
    r.lpush("TASKS", key)
    result = r.hset(
        key, 
       key='inputData',
       value=inputData
    )

    result = r.hset(
        key, 
       key='model',
       value=model
    )

    return Response(str(result), status=200)


@app.route("/pop", methods=['POST'])
def popTask():
    key = r.rpop("TASKS")

    if key is None:
        return Response("Queue empty", status=200)

    key = key.decode('utf-8')
    
    inputData = r.hget(key, 'inputData')
    model = r.hget(key, 'model')

    data = {
        'inputData': inputData.decode('utf-8'),
        'model': model.decode('utf-8'),
    }
    r.hdel(key, 'inputData')
    r.hdel(key, 'model')

    return data

if __name__ == "__main__":
    app.run()