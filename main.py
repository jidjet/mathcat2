time_periods = {
    "day": 24,
    "half-day": 12,
    "quarter-day": 6,
    "hour": 1,
    "minute": 1/60,
    "second": 1/3600
}

def naive_model():
    print("Naive population model:")
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
    print("Sophisticated population model:")
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

def projection_timeframe():
    print("Future projection timeframe for both models:")
    projection_time = int(input("Enter the amount of time to project into the future: "))
    projection_time_unit = input("Enter the projection time unit (day, half-day, quarter-day, hour, minute, second):")
    info = {
        "time": projection_time,
        "unit": projection_time_unit
    }
    return info

def data(naive, sophisticated, projection):
    print(f"Naive Model: I = {naive[initial_population]}, g = {naive[growth_rate]}% per {naive[growth_unit]}")
    print(f"Sophisticated Model: I = {sophisticated[initial_population]}, g = {sophisticated[growth_rate]}% per {sophisticated[growth_unit]}, Fission-event frequency: {sophisticated[fission_unit]}")
    print(f"Projection timeframe: {projection[projection_time]} {projection[projection_time_unit]}")


def module_one():
    print("MODULE 1: NAIVE AND SOPHISTICATED MODEL COMPARISON")
    naive = naive_model()
    sophisticated = sophisticated_model()
    projection = projection_timeframe()
    data(naive, sophisticated, projection)

module_one()

