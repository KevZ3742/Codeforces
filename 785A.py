# A. Anton and Polyhedrons
# https://codeforces.com/contest/785/problem/A
# rating: 800

n = int(input())

polyhedrons = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
faces = 0
for _ in range(n):
    polyhedron = input()

    faces += polyhedrons[polyhedron]

print(faces)