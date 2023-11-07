import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GeometricFigure:
    def __init__(self, figure_type, points):
        self.figure_type = figure_type
        self.points = points

def calculate_distance(point1, point2):
    delta_x = point2.x - point1.x
    delta_y = point2.y - point1.y
    return math.sqrt(delta_x**2 + delta_y**2)

def are_overlapping(figure1, figure2):
    for point1 in figure1.points:
        for point2 in figure2.points:
            distance = calculate_distance(point1, point2)
            if distance == 0:
                return True
    return False

def create_point():
    x = float(input("Digite a coordenada x do ponto: "))
    y = float(input("Digite a coordenada y do ponto: "))
    return Point(x, y)

def create_line():
    print("Digite os pontos para criar a reta:")
    point1 = create_point()
    point2 = create_point()
    return GeometricFigure("Reta", [point1, point2])

def create_circle():
    print("Digite os pontos para criar o círculo (centro e ponto na circunferência):")
    center = create_point()
    circumference_point = create_point()
    radius = calculate_distance(center, circumference_point)
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    print(f"Círculo criado com raio: {radius}")
    print(f"Área do círculo: {area}")
    print(f"Perímetro do círculo: {perimeter}")
    return GeometricFigure("Círculo", [center, circumference_point])

def create_rectangle():
    print("Digite os pontos para criar o retângulo (três vértices):")
    vertex1 = create_point()
    vertex2 = create_point()
    vertex3 = create_point()
    width = calculate_distance(vertex1, vertex2)
    height = calculate_distance(vertex2, vertex3)
    area = width * height
    perimeter = 2 * (width + height)
    print(f"Retângulo criado com largura: {width} e altura: {height}")
    print(f"Área do retângulo: {area}")
    print(f"Perímetro do retângulo: {perimeter}")
    return GeometricFigure("Retângulo", [vertex1, vertex2, vertex3])

def create_square():
    print("Digite os pontos para criar o quadrado (dois pontos em um dos lados):")
    side_point1 = create_point()
    side_point2 = create_point()
    side_length = calculate_distance(side_point1, side_point2)
    area = side_length**2
    perimeter = 4 * side_length
    print(f"Quadrado criado com lado: {side_length}")
    print(f"Área do quadrado: {area}")
    print(f"Perímetro do quadrado: {perimeter}")
    return GeometricFigure("Quadrado", [side_point1, side_point2])

def check_overlap(figures):
    for i in range(len(figures) - 1):
        for j in range(i + 1, len(figures)):
            if are_overlapping(figures[i], figures[j]):
                print(f"As figuras {figures[i].figure_type} e {figures[j].figure_type} estão sobrepostas.")

def main():
    figures = []

    while True:
        print("Universo Geométrico!")
        print("Você pode criar, calcular e verificar figuras geométricas aqui.")
        print("Escolha uma opção abaixo:")
        print("1. Criar um ponto")
        print("2. Criar uma reta")
        print("3. Criar uma figura geométrica")
        print("4. Verificar sobreposição de figuras")
        print("5. Sair")

        option = int(input("Digite o número da opção desejada: "))

        if option == 1:
            point = create_point()
            print(f"Ponto criado em ({point.x}, {point.y})")

        elif option == 2:
            line = create_line()
            figures.append(line)

        elif option == 3:
            if len(figures) < 2:
                print("É necessário pelo menos 2 pontos para criar uma figura.")
            else:
                print("Escolha uma figura geométrica para criar:")
                print("1. Círculo")
                print("2. Retângulo")
                print("3. Quadrado")
                figure_option = int(input("Digite o número da figura desejada: "))

                if figure_option == 1:
                    circle = create_circle()
                    figures.append(circle)

                elif figure_option == 2:
                    rectangle = create_rectangle()
                    figures.append(rectangle)

                elif figure_option == 3:
                    square = create_square()
                    figures.append(square)

                else:
                    print("Opção inválida.")

        elif option == 4:
            check_overlap(figures)

        elif option == 5:
            print("Finalizar Universo Geométrico!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
