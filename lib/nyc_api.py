import requests
import json

class GetPrograms:
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.json()  # Use .json() to directly parse JSON response

    def program_school(self):
        programs_list = []
        programs = self.get_programs()  # Directly call the method
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

# Create an instance of GetPrograms
programs = GetPrograms()

# Call the program_school method
programs_schools = programs.program_school()

# Print the results
for school in set(programs_schools):
    print(school)
