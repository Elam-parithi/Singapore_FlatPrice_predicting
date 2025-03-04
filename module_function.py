import json
import pickle
import numpy as np

json_settings = r"settings.json"
ML_file = r"model_data/RTR_model.pkl"

with open(ML_file, "rb") as f:
    regg_model = pickle.load(f)

with open(json_settings, "rb") as f:
    json_data = json.load(f)


# Mapping functions
def town_mapping(town: str):
    mapping = json_data['town']
    return mapping.index(town)

def flat_type_mapping(flat_type: str):
    mapping = json_data['flat_type']
    return mapping.index(flat_type)

def flat_model_mapping(flat_model: str):
    mapping = json_data['flat_model']
    return mapping.index(flat_model)

# Prediction function
def predict_price(town, flat_type, floor_area_sqm, flat_model, lease_commence_date, year,
                  storey_start, storey_end, remaining_lease_year, remaining_lease_month):
    in_year = int(year)
    in_town = town_mapping(town)
    in_flat_type = flat_type_mapping(flat_type)
    in_flat_area = float(floor_area_sqm)
    in_flat_model = flat_model_mapping(flat_model)

    # Handling log transformation, add 1 to avoid log(0)
    in_str_str = np.log(float(storey_start) + 1)
    sin_tr_end = np.log(float(storey_end) + 1)

    in_rem_les_year = int(remaining_lease_year)
    in_rem_les_month = int(remaining_lease_month)
    in_lease_commence_data = int(lease_commence_date)

    list_arr = [in_town, in_flat_type, in_flat_area, in_flat_model, in_lease_commence_data, in_year,
                in_str_str, sin_tr_end, in_rem_les_year, in_rem_les_month]

    user_data = np.array([list_arr])

    # Ensure data is finite
    if not np.all(np.isfinite(user_data)):
        print("Input data contains invalid or infinite values.")
        return None

    y_pred_1 = regg_model.predict(user_data)
    price = np.exp(y_pred_1[0])

    return round(price)


if __name__ == "__main__":
    # ,,,,,,,,,
    predict_price(town=25, flat_type=5.0, floor_area_sqm=145.0, flat_model=3.0, lease_commence_date=1987,
                  year=2025, storey_start=0.011858263308657468, storey_end=1.0986122886681098,
                  remaining_lease_year=61, remaining_lease_month=10)
