import numpy as np


def projection(a, b):
    numerator = np.dot(a, b)
    denominator = np.linalg.norm(b) ** 2
    return (numerator / denominator) * b


def main():
    components = input(
        "Please type 4 number separate by space, each pair represents the components of a vector: ").split(" ")

    vector_a = np.array([int(components[0]), int(components[1])])
    vector_b = np.array([int(components[2]), int(components[3])])
    print(projection(vector_a, vector_b))


main()
