

def process_sensor_data(raw_data, **config):

    """
Process a dataset with optional cleaning and scaling steps.

:param raw_data: The dataset to be processed.
:type raw_data: list[float]

:param config: Optional keyword arguments.
    **remove_outliers** (bool, default False)
   Discard values more than 3 standard deviations from the mean.
    **smooth** (bool, default False)
        Apply a 3-point moving average.
    **scale** (str, default "normalize")
        Scaling method to apply:
        ``"normalize"`` — scale values to the range [0, 1].
        ``"standardize"`` — standardize values to zero mean and unit variance.
:return: list[float]

Unknown keyword arguments are ignored.
"""

# raw_data = list of readings
# config options:
# remove_outliers=True (discard >3σ from mean)
# smooth=True (3-point moving average)
# scale="normalize" or "standardize"
# Unknown options → ignore
    data = raw_data
    remove_outliers = config.get("remove_outliers", False)
    smooth = config.get("smooth", False)
    scale = config.get("scale", "normalize")

    # STEPS TO CALCULATE A SIGMA
# 1. Calculate the mean (average) of the data set.
#    - Sum all the data points.
#    - Divide by the number of data points.
    mean = sum(data) / len(data)

# 2. Subtract the mean from each data point.
#    - individual data point - calculated mean = deviation
    deviation_values = [data_point - mean for data_point in data] 
# 3. Square each of the deviations.
#   - deviation ** 2 (or deviation * deviation)
    squared_deviations = [deviation ** 2 for deviation in deviation_values]
# 4. Sum all the squared deviations (from step 3).
    sum_squared_deviations = sum(squared_deviations)
# 5. Subtract 1 from the sample size
    n_minus_1 = len(data) - 1
# 6. Step 4 / Step 5
    variance = sum_squared_deviations / n_minus_1
# 7. Sqrt() of step 6 = 1 sigma
    sigma = variance ** 0.5
# 8. Multiply 1 sigma by desired number of sigmas (e.g., 2 sigma, 3 sigma)
    sigma_threshold = 3 * sigma

    if remove_outliers:
        data = [x for x in data if abs(x - mean) <= sigma_threshold]

    if smooth:
        smooth_data = []
        count = 0
        for i in range(len(data)):
            if count == 0:
                smooth_data.append((i+data[i+1])/2)
            elif count < len(data)-1:
                smooth_data.append((data[i-1]+i+data[i+1])/3)
            elif count == len(data)-1: # might need to do data-1
                smooth_data.append((data[i-1]+i)/2)
            else:
                print("oop something went wrong.")
                print(f"count {count}\ni: {i}\nrange(len(data)): {range(len(data))}")

            count = count + 1
    if scale == "normalize":
        normalized_data = []
        if smooth:
            max_val = max(smooth_data)
            min_val = min(smooth_data)
            normalized_data = [((x-min_val)/(max_val-min_val)) for x in smooth_data]
        
        else:
            max_val = max(data)
            min_val = min(data)
            normalized_data = [((x-min_val)/(max_val-min_val)) for x in data]

        return normalized_data
    elif scale == "standardize":
        standardized_data = []
        if smooth:
            standardized_data = [((x-mean)/sigma_threshold) for x in smooth_data]
        else:
            standardized_data = [((x-mean)/sigma_threshold) for x in data]

        return standardized_data