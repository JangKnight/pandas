#!.venv/bin/python
import os, csv
import pandas as pd


def main():
    with open("weather_data.csv", "r+") as data_file:
        data = pd.read_csv(data_file)
        # data_dict = data.to_dict()
        # for idx, entry in enumerate(data):
        #     if idx:
        #         temps.append(int(entry[1]))
    # print(sum(temps)/len(temps))
    print(data["temp"].mean())


if __name__ == "__main__":
    main()
