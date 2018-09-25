import os
import pickle


def load(file_path, entity, resolvable):
    full_path = f'{file_path}.{entity}.pickle'

    if os.path.isfile(full_path):

        with open(full_path, 'rb') as f:
            return pickle.load(f)

    value = resolvable()
    persist(file_path, entity, value)

    return value


def persist(file_path, entity, value):
    full_path = f'{file_path}.{entity}.pickle'

    with open(full_path, 'wb') as f:
        return pickle.dump(value, f, pickle.HIGHEST_PROTOCOL)
