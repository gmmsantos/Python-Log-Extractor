list_oid = []  # declare a empty list to store Object ID

search_string = "error".lower()  # substring to search

with open("log_file.log", "rt") as file:  # open the log file in read text mode
    for line in file:  # for each line in the log file add to the list
        if (
            line.lower().find(search_string) != -1
        ):  # The find() method returns -1 if the value is not found.
            list_oid.append(line.rstrip("\n"))

with open("output.txt", mode="w") as output:
    for oid in list_oid:
        output.write(oid + "\n")
