from app.base import app

print(app)

@app.get('/items')
def g():
    return 123