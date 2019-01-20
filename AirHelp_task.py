import csv_parser
import json_parser

import os
import operator
import matplotlib.pyplot as plt

class Report_Generator:
    def __init__(self):
        self.average_compensation_per_passenger = 0
        self.percentage_of_users_who_got_compensation = 0
        self.air_line_popularity = {}
        self.row_length = 0
        self.distribution_of_passengers = []
        self.message = []

    def run(self, path):
        file = open('Report.txt', "w")
        mess_file = open("Messages.txt", "w")
        for filename in os.listdir(path):
            is_file = 0
            if os.path.splitext(filename)[1] == '.csv':
                file.write('\nBelow report created for: ' + str(filename) + '\n')
                csv_path = os.path.join(path, filename)
                csv_parser.parse(self, csv_path)
                self.report(file, filename, mess_file)
                is_file = 1

            elif os.path.splitext(filename)[1] == '.json':
                file.write('\nBelow report created for: ' + str(filename) + '\n')
                json_path = os.path.join(path, filename)
                json_parser.parse(self, json_path)
                self.report(file, filename, mess_file)
                is_file = 1

        if is_file == 0:
            print('There is no right file!')
        else:
            print('Report created!')



    def report(self, file, filename, mess_file):
        file.write('percentage of users who got_compensation: ' + str(self.percentage_of_users_who_got_compensation) + '%\n')
        file.write('average compensation per passenger: ' + str(self.average_compensation_per_passenger) + '\n')
        file.write('the most popular airline: ' + str(max(self.air_line_popularity.items(), key=operator.itemgetter(1))[0]) + '\n')
        mess_file.write("Below messages are from: " + filename + '\n')
        mess_file.write(str(self.message) + '\n')


        plt.hist(self.distribution_of_passengers, facecolor='green')
        plt.xlabel('number of passengers on the plane')
        plt.ylabel('the number of arrivals of a given number of passengers')
        plt.savefig(str(filename) + '.png')
        plt.close()
        self.average_compensation_per_passenger = 0
        self.percentage_of_users_who_got_compensation = 0
        self.air_line_popularity = {}
        self.row_length = 0
        self.distribution_of_passengers = []
        self.message = []


if __name__ == '__main__':
    report = Report_Generator()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(dir_path, "examples")

    report.run(folder_path)
