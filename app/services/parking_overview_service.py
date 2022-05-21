import pandas as pd
import numpy as np
import csv

from app.objects import models

df = pd.read_csv("app/data/papp_kgslyngby.csv", sep=";")


def get_overview():
    parking_overview = models.ParkingOverview(parking_categories=[])
    parking_overview.parking_categories.append(calc_top5_occupacy())
    parking_overview.parking_categories.append(calc_bot5_occupacy())
    parking_overview.parking_categories.append(calc_mean_occupacy_all())
    return parking_overview


def calc_top5_occupacy():
    df = get_occupacy_df()
    top5_dict = df.nlargest(5, "occupacy").to_dict()["occupacy"]
    parking_category = models.ParkingCategory(
        "Parkingsområder men højest belægning", top5_dict
    )
    return parking_category


def calc_bot5_occupacy():
    df = get_occupacy_df()
    bot5_dict = df.nsmallest(5, "occupacy").to_dict()["occupacy"]
    parking_category = models.ParkingCategory(
        "Parkingsområder med lavest belægning", bot5_dict
    )
    return parking_category


def calc_mean_occupacy_all():
    df = get_occupacy_df()
    mean_occupacy = round(float(df["occupacy"].mean()), 2)
    dif = 100 - mean_occupacy
    pieData = [mean_occupacy, dif]
    parking_category = models.ParkingCategory("Gennemsnitlig Belægningsgrad", pieData)
    return parking_category


def get_occupacy_df():
    vehicle_count_df = pd.DataFrame(
        {"vehicleCount": df.groupby("garageCode")["vehicleCount"].mean()}
    ).reset_index()
    vehicle_count = [
        int(v_count) for v_count in vehicle_count_df["vehicleCount"].tolist()
    ]

    total_spaces_df = pd.DataFrame(
        {"totalSpaces": df.groupby("garageCode")["totalSpaces"].first()}
    ).reset_index()
    total_spaces = [int(space) for space in total_spaces_df["totalSpaces"].tolist()]

    divided = np.divide(vehicle_count, total_spaces)
    occupacy = [i * 100 for i in divided]

    occupacy_df = pd.DataFrame(
        data=occupacy, index=total_spaces_df["garageCode"], columns=["occupacy"]
    )
    return occupacy_df
