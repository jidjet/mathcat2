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
    fission_unit = input("Enter the fission-event frequency time unit (day, half-day, quarter-day, hour, minute, second, custom): ")
    
    custom_unit = None  
    if fission_unit == "custom":
        custom_unit = int(input("Enter the number of fission events per growth rate time unit: "))
    
    info = {
        "population": initial_population,
        "rate": growth_rate,
        "unit": growth_unit,
        "fission": fission_unit
    }

    if fission_unit == "custom":
        info["custom"] = custom_unit
    
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
    print(f"Naive Model: I = {naive.get("population")}, g = {naive.get("rate")}% per {naive.get("unit")}")
    if sophisticated.get("fission") == "custom":
        print(f"Sophisticated Model: I = {sophisticated.get("population")}, g = {sophisticated.get("rate")}% per {sophisticated.get("unit")}, Fission-event frequency: {sophisticated.get("custom")}")
    else:
        print(f"Sophisticated Model: I = {sophisticated.get("population")}, g = {sophisticated.get("rate")}% per {sophisticated.get("unit")}, Fission-event frequency: {sophisticated.get("fission")}")
    print(f"Projection timeframe: {projection.get("time")} {projection.get("unit")}")


def module_one():
    print("MODULE 1: NAIVE AND SOPHISTICATED MODEL COMPARISON")
    naive = naive_model()
    sophisticated = sophisticated_model()
    projection = projection_timeframe()
    data(naive, sophisticated, projection)

module_one()

