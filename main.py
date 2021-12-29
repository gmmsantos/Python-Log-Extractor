list_err_lines = []  # declare a empty list to store the lines

search_string = "error".lower()  # substring to search

with open("log_file.log", "rt") as file:  # open the log file in read text mode
    for line in file:  # for each line in the log file add to the list
        if (
            line.lower().find(search_string) != -1
        ):  # The find() method returns -1 if the value is not found.
            list_err_lines.append(line.rstrip("\n"))

with open("output.txt", mode="w") as output:
    for err in list_err_lines:
        output.write(err + "\n")
