
from utils import calculate_bmi
from typing import List

def main(records: List):
    """
    Driver code for calculation BMI
    Output: records: List 
    This code will add three more keys bmi_category, bmi_range, health_risk in the same record of the person
    and also return number of over weight people.
    """
    overweight_people = 0
    for record in records:
        if isinstance(record["Gender"], str) and isinstance(record["HeightCm"], int) and isinstance(record["WeightKg"], int) :
            bmi_result = calculate_bmi(record)
            record["bmi_category"] = bmi_result[0]
            record["bmi_range"] = bmi_result[1]
            record["health_risk"] = bmi_result[2]
            if bmi_result[1] == 'Over Weight':
                overweight_people = overweight_people + 1
        else:
            record["bmi_category"] = "Invalide data"
            record["bmi_range"] = "Invalide data"
            record["health_risk"] = "Invalide data"

    return records, overweight_people




# dummy input
records = [ 
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },

            { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },

            { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },

            { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},

            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},

            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
            ]


calculated_bmi_data, number_of_overweight_people = main(records)
print(f"There are {number_of_overweight_people} over weight people.\n")
print(calculated_bmi_data)


