import csv

def parse(self, csv_path):
    with open(csv_path) as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            self.row_length += 1
            self.distribution_of_passengers.append(int(row['number_of_fellow_passenger']))
            self.message.append(row['message'])

            if row['did_receive_compensation'] in (1, 'yes', 'tak', '1'):
                self.percentage_of_users_who_got_compensation += 1

            self.average_compensation_per_passenger += float(row['total_compensation_amount'])

            try:
                self.air_line_popularity[row['airline_code']] += 1
            except:
                self.air_line_popularity[row['airline_code']] = 1

        self.percentage_of_users_who_got_compensation /= self.row_length / 100
        self.average_compensation_per_passenger /= self.row_length


