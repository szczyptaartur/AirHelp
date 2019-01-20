import json

def parse(self, csv_path):
    with open(csv_path) as f:
        data = json.load(f)
    for row in data:
        self.row_length += 1
        self.distribution_of_passengers.append(int(data[row]['number_of_fellow_passenger']))
        self.message.append(data[row]['message'])
        if data[row]['did_receive_compensation'] in (1, 'yes', 'tak', '1'):
            self.percentage_of_users_who_got_compensation += 1

        self.average_compensation_per_passenger += float(data[row]['total_compensation_amount'])

        try:
            self.air_line_popularity[data[row]['airline_code']] += 1
        except:
            self.air_line_popularity[data[row]['airline_code']] = 1

    self.percentage_of_users_who_got_compensation /= self.row_length / 100
    self.average_compensation_per_passenger /= self.row_length


