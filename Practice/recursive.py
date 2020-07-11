def recursive(goal, total):
    if total == goal:
        return 1
    if total > goal:
        return 0
    return recursive(goal, total + 1) + recursive(goal, total + 2) + recursive(goal, total + 3)

if __name__ == "__main__":
    print(recursive(5, 0))
