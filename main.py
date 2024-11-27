def task1() -> str:
    msg: str = """Create good script to create new list, which only contains users from Poland.
        Try to do it with List Comprehension."""
    users: list[dict] = [
        {"name": "Kamil", "country": "Poland"},
        {"name": "John", "country": "USA"},
        {"name": "Yeti"},
    ]
    
    polishPeoples: list[str] = [
        person['name'] 
        for person in users 
            if 'country' in person.keys() 
                and person['country'] == 'Poland'
    ]

    return f"Task 1: {msg}\nData: {users}\nAnswer: {polishPeoples}\n"

def task2() -> str:
    msg: str = "Display sum of first ten elements starting from element 5."
    numbers: list[int] = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]

    start_index = numbers.index(5)
    result = numbers[start_index : start_index+10]

    return f"Task 2: {msg}\nData: {numbers}\nAnswer: {result} = {sum(result)}\n"

def task3() -> str:
    msg: str = "Fill list with powers of 2, n [1...20]"

    powerList: int = [2<<n for n in range(1, 21)]

    return f"Task 3: {msg}\nAnswer: {powerList}\n"

if __name__ == "__main__":
    print()
    print(task1())
    print(task2())
    print(task3())