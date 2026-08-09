#!.venv/bin/python
import os, csv
import pandas as pd

def main():
    with open("squirrel_data.csv", "r+") as data_file:
        data = pd.read_csv(data_file)
        data_dict = data.to_dict()
        color_count = {}
        # data_json = str(data.to_json())

        for color in data_dict["Primary Fur Color"].values():
            if str(color) != "nan":
                if color not in color_count:
                    color_count[color] = 1
                else:
                    color_count[color] += 1

        for color, count in color_count.items():
            print(f"{color}: {count}")

    # with open("squirrel_data.json", "w+") as json_file:
    #     json_file.write(data_json)

if __name__ == "__main__":
    main()
