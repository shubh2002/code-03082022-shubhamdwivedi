from bmi import BMI
from typing import Dict



def calculate_bmi(data: Dict):
    """
    Used to calculate bmi_range, bmi_category, health_risk of a person
    """
    bmi_category= None
    health_risk= None
    bmi_range = None
    x =data["HeightCm"]
    y = data["WeightKg"]
    bmi = y/((x/100)**2)

    if bmi <= 18.4 :
        bmi_category = BMI.bmi_category.get('UW')
        bmi_range = bmi
        health_risk = BMI.health_risk.get('MR')
    elif bmi >=18.5 and bmi <= 24.9:
        bmi_category = BMI.bmi_category.get('NW')
        bmi_range = bmi
        health_risk = BMI.health_risk.get('LR')
    elif bmi >=25 and bmi <= 29.9:
        bmi_category = BMI.bmi_category.get("OW")
        bmi_range = bmi
        health_risk = BMI.health_risk.get('ER')
    elif bmi >=30 and bmi <= 34.9:
        bmi_category = BMI.bmi_category.get("MO")
        bmi_range = bmi
        health_risk = BMI.health_risk.get('MRS')
    elif bmi >= 35 and bmi <= 39.9:
        bmi_category = BMI.bmi_category.get("SO")
        bmi_range = bmi
        health_risk = BMI.health_risk.get('HR')
    elif bmi > 40:
        bmi_category = BMI.bmi_category.get("VSO")
        bmi_range = bmi
        health_risk = BMI.health_risk.get('VHR')

    output_list = [bmi_category,bmi_range,health_risk]

    return output_list