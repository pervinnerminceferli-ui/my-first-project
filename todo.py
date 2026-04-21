
tasks = []

while True:
    task = input("Tapşırıq yaz. Çıxmaq üçün 'stop' yaz: ")
    if task == "stop":
        break
    tasks.append(task)

print("\nSənin siyahın:")
for i, t in enumerate(tasks, 1):
    print(f"{i}. {t}")
