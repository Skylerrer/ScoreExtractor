
import os
import argparse
from pathlib import Path
import time
import csv

def get_default_output_path():
    curr_time_to_prepend = time.strftime("%H%M%S_")
    file_name = curr_time_to_prepend + "score_stats.csv"
    default_file_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', file_name)
    return Path(default_file_path)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str, help="path to video file or directory containing possibly multiple video files")
    parser.add_argument("-o", "--output_path", type=str, help="path to file where scoreboard data gets stored")

    args = parser.parse_args()

    input_path = Path(args.input_path)

    if args.output_path is not None:
        output_path = Path(args.output_path)
    else:
        output_path = get_default_output_path()

    print(input_path)
    print(output_path)

    #Check whether input_path exists (can be file or directory)
    if not input_path.exists():
        raise RuntimeError("Given input_path does not exist!")

    #test writing to csv
    with open(output_path, 'w', newline='') as csvfile:
        score_writer = csv.writer(csvfile, delimiter=',')
        score_writer.writerow(["Tore Team 1", "Tore Team 2", "Verbleibende Zeit in Viertel", "Zeit verbracht in Viertel", "Viertel"])
        score_writer.writerow(["0", "1", "678", "42", "1"])




if __name__ == "__main__":

    main()

    #TODO
    # get video file
    # ask for region of interest
    # extract score and time from region of interest
    # save score and time to file (e.g. json / txt / database / ...)