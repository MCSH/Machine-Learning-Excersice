import pickle
from db import DB
import numpy as np

def load_model(file_address):
    with open(file_address, 'rb') as f:
        return pickle.load(f)

def main():
    models = load_model('../model.pkl')
    model = models["model"]
    means = models["means"]
    print(means)
    db = DB()
    for (id, x) in db.read():
        print(id)
        x = np.array(x)
        # Replace non-existing values with means
        for i,v in enumerate(x):
            if v == None:
                x[i] = means[i]
        y = model.predict([x])
        db.write(id, int(y[0]))

if __name__ == "__main__":
    main()
