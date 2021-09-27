from utils import  display_table, load_lines_from_file


lines, headers = load_lines_from_file("Fitbit.csv")


data = display_table(lines, headers)

