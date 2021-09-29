import utils 

lines, headers = utils.read_data("Checking_Data.csv")

data, new_headers = utils.display_table(lines, headers)