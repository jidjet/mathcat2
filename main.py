time_periods = {
    "year": 365 * 24,
    "quarter": 91.25 * 24,
    "month": 30 * 24,
    "week": 7 * 24,
    "day": 24,
    "half-day": 12,
    "quarter-day": 6,
    "hour": 1,
    "minute": 1 / 60,
    "second": 1 / 3600
}

def naive_model():
    print("Naive population model:")
    initial_population = int(input("Enter the initial population: "))
    growth_rate = int(input("Enter the growth rate (enter 7% as 7): "))
    growth_unit = input("Enter the growth rate time unit (day, half-day, quarter-day, hour, minute, second): ")
    return {
        "population": initial_population,
        "rate": growth_rate,
        "unit": growth_unit
    }

def sophisticated_model():
    print("Sophisticated population model:")
    initial_population = int(input("Enter the initial population: "))
    growth_rate = int(input("Enter the growth rate (enter 7% as 7): "))
    growth_unit = input("Enter the growth rate time unit (day, half-day, quarter-day, hour, minute, second): ")
    fission_unit = input("Enter the fission-event frequency time unit (day, half-day, quarter-day, hour, minute, custom): ")

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
    projection_time_unit = input("Enter the projection time unit (day, half-day, quarter-day, hour, minute, second): ")
    return {
        "time": projection_time,
        "unit": projection_time_unit
    }

def population_calculation(model, data, projection):
    time_ratio = time_periods[projection["unit"]] / time_periods[data["unit"]]
    num_growth_periods = projection["time"] * time_ratio
    rate = data["rate"] / 100
    population = data["population"]

    if model == "naive":
        final_population = population * ((1 + rate) ** num_growth_periods)
        return final_population

    elif model == "sophisticated":
        if data["fission"] == "custom":
            fission_per_growth = data["custom"]
        else:
            fission_per_growth = time_periods[data["unit"]] / time_periods[data["fission"]]

        effective_periods = num_growth_periods * fission_per_growth
        adjusted_rate = rate / fission_per_growth
        final_population = population * ((1 + adjusted_rate) ** effective_periods)
        return final_population

def print_data(naive, sophisticated, projection):
    print(f'Naive Model: I = {naive.get("population")}, g = {naive.get("rate")}% per {naive.get("unit")}')
    if sophisticated.get("fission") == "custom":
        print(f'Sophisticated Model: I = {sophisticated.get("population")}, g = {sophisticated.get("rate")}% per {sophisticated.get("unit")}, Fission-event frequency: {sophisticated.get("custom")}')
    else:
        print(f'Sophisticated Model: I = {sophisticated.get("population")}, g = {sophisticated.get("rate")}% per {sophisticated.get("unit")}, Fission-event frequency: {sophisticated.get("fission")}')
    print(f'Projection timeframe: {projection.get("time")} {projection.get("unit")}')

def module_one_with_results():
    print("MODULE 1: NAIVE AND SOPHISTICATED MODEL COMPARISON")
    naive = naive_model()
    sophisticated = sophisticated_model()
    projection = projection_timeframe()

    print("\nSummary of entered data:")
    print_data(naive, sophisticated, projection)

    naive_result = population_calculation("naive", naive, projection)
    sophisticated_result = population_calculation("sophisticated", sophisticated, projection)

    print(f"\nNaive model projected population size: {naive_result:.2f}")
    print(f"Sophisticated model projected population size: {sophisticated_result:.2f}")

def sophisticated_model_to_target():
    print("MODULE 2: TIME FOR A POPULATION TO REACH A TARGET SIZE")

    initial_population = int(input("Enter the initial population: "))
    growth_rate = float(input("Enter the growth rate (enter 7% as 7): "))
    growth_unit = input("Enter the growth rate time unit (year, quarter, month, week, day): ")

    fission_unit = input("Enter the fission-event frequency time unit (day, half-day, quarter-day, hour, minute, custom): ")
    custom_unit = None
    if fission_unit == "custom":
        custom_unit = int(input("Enter the number of fission events per growth rate time unit: "))

    target_amount = int(input("Enter the target amount: "))

    model_info = {
        "population": initial_population,
        "rate": growth_rate,
        "unit": growth_unit,
        "fission": fission_unit,
        "target": target_amount
    }

    if fission_unit == "custom":
        model_info["custom"] = custom_unit

    print("\nSummary of entered data:")
    if fission_unit == "custom":
        print(f'Sophisticated model: I = {initial_population}, g = {growth_rate}% per {growth_unit}, Fission-event frequency: {custom_unit}')
    else:
        print(f'Sophisticated model: I = {initial_population}, g = {growth_rate}% per {growth_unit}, Fission-event frequency: {fission_unit}')
    print(f'Target amount: {target_amount}')

    return model_info

sophisticated_model_to_target()