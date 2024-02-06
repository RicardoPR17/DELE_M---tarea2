import numpy as np


def rotation(angle: int, vec: [[]]):
    alpha = np.deg2rad(angle)
    rotation_matrix = [[np.cos(alpha), -np.sin(alpha)],
                       [np.sin(alpha), np.cos(alpha)]]

    rotated_vector = np.matmul(rotation_matrix, vec)
    return rotated_vector


def main():
    components = input("Components of the vector to rotate (separate by comma): ").split(",")
    alpha = int(input("Enter the angle in degrees: "))
    vector = [[int(components[0])], [int(components[1])]]
    rotated = rotation(alpha, vector)
    print(f"The rotated vector is <{rotated[0][0]:.4}, {rotated[1][0]:.4}>")


main()
