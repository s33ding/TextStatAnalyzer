import pickle

def creating_data_4_test(data,name):
    with open(f"shared_func/data/{name}.pickle", "w") as f:
        pickle.dump(data, f)
