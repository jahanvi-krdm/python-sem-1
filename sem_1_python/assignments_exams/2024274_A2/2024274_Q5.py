def multiply_matrices(mat1, mat2):
    result_matrix = []
    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat2[0])):
            total = 0
            for k in range(len(mat2)):
                total += mat1[i][k] * mat2[k][j]
            new_row.append(total)
        result_matrix.append(new_row)
    return result_matrix

def apply_scaling(coords, scale_x, scale_y):
    shape_matrix = [[x, y, 1] for x, y in coords]
    scale_matrix = [
        [scale_x, 0, 0],
        [0, scale_y, 0],
        [0, 0, 1]
    ]
    scaled_matrix = multiply_matrices(shape_matrix, scale_matrix)
    return [(row[0], row[1]) for row in scaled_matrix]

num_coords = int(input("Enter the number of coordinates: "))
input_coords = []
i = 0

while i < num_coords:
    x_val, y_val = map(float, input(f"Enter x{i + 1}, y{i + 1} separated by space: ").split())
    input_coords.append((x_val, y_val))
    i += 1

scale_x = float(input("Enter scaling factor for x-axis: "))
scale_y = float(input("Enter scaling factor for y-axis: "))

scaled_coords = apply_scaling(input_coords, scale_x, scale_y)
print("Scaled coordinates:", scaled_coords)

def test_scaling():
    coords1 = [(1, 1), (2, 2), (3, 3)]
    assert apply_scaling(coords1, 2, 2) == [(2, 2), (4, 4), (6, 6)]

    coords2 = [(1, 2), (3, 4), (5, 6)]
    assert apply_scaling(coords2, 0.5, 0.5) == [(0.5, 1.0), (1.5, 2.0), (2.5, 3.0)]

    shape1 = [[1, 2, 1], [3, 4, 1]]
    scale1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert multiply_matrices(shape1, scale1) == [[1, 2, 1], [3, 4, 1]]

test_scaling()