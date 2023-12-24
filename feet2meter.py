def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    c = v.rstrip("ft")
    p = float(c)
    v = 0.3048
    w = p * v
    return w


main()