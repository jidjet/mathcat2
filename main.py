time_periods = {
    "day": 24,
    "half-day": 12,
    "quarter-day": 6,
    "hour": 1,
    "minute": 1/60,
    "second": 1/3600
}

def naive_model():
    initial_population = int(input("Enter the initial population: ")) 
    growth_rate = int(input("Enter the growth rate (enter 7% as 7): "))
    growth_unit = input("Enter the growth rate time unit (day, half-day, quarter-day, hour, minute, second): ")
    info = {
        "population": initial_population,
        "rate": growth_rate,
        "unit": growth_unit
    }
    return info 

def sophisticated_model():
    initial_population = int(input("Enter the initial population: ")) 
    growth_rate = int(input("Enter the growth rate (enter 7% as 7): "))
    growth_unit = input("Enter the growth rate time unit (day, half-day, quarter-day, hour, minute, second): ")
    fission_unit =  input("Enter the fission-event frequency time unit(day, half-day, quarter-day, hour, minute, second): ")
    info = {
        "population": initial_population,
        "rate": growth_rate,
        "unit": growth_unit,
        "fission": fission_unit
    }
    return info

# def projection

def module_one():
    print("MODULE 1: NAIVE AND SOPHISTICATED MODEL COMPARISON")
    naive = naive_model()
    print(naive)
    sophisticated = sophisticated_model()
    print(sophisticated)

module_one()

