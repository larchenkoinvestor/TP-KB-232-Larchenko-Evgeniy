# Функція для обчислення дискримінанту
def find_dis(a, b, c):
    return b**2 - 4*a*c

# Функція для знаходження коренів
def find_roots():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))
    
    if a == 0:
        print("Це не квадратне рівняння.")
        return
    
    D = find_dis(a, b, c)
    print("Дискримінант:", D)

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print("Два корені:", x1, x2)
    elif D == 0:
        x = -b / (2*a)
        print("Один корінь:", x)
    else:
        print("Коренів немає (дискримінант менше 0).")

find_roots()
