import pickle


def load_beastiary():
    with open("beastiary.pkl", 'rb') as f:
        return pickle.load(f)


beastiary = load_beastiary()

print(beastiary)
