# Computing ID: vgs3qt
# Name: Zhiyuan Chang

def instructor_lectures(department, instructor):
    """
    Returns a list of all the course names for the lectures (not laboratories, discussions, etc.) taught by a given
    instructor (within the given department). If an instructor teaches multiple lecture sections of the same class,
    you should only add the class name once (i.e., there should be no duplicates of any class names in the list that
    you return. The list should include all classes that list the given instructor, even if it has a +1 (or something
    similar) listed as well.
    :param department: The department like CS, STS.
    :param instructor: The name of the instructor.
    :return: Returns a list of all the course names for the lectures (not laboratories, discussions, etc.) taught by
    a given instructor (within the given department).
    """
    url = "http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + department
    import urllib.request
    fstream = urllib.request.urlopen(url)
    result = []
    for row in fstream:
        row = row.decode("utf-8")
        cell = row.strip().split("|")
        if cell[5] == "Lecture":
            if cell[4] == instructor or cell[4][0:-2] == instructor:
                if cell[3] not in result:
                    result.append(cell[3])
    return result

def compatible_classes(first_class, second_class, needs_open_space = False):
    """
    Returns True if the two given classes are compatible within the same schedule and False otherwise. Additionally,
    when the needs_open_space argument is True, the function should return False if either of the classes has reached
    enrollment capacity (regardless of whether or not the classes are compatible). Two classes are considered
    compatible if there is no overlap between their schedules.
    :param first_class: Name of the first class.
    :param second_class: Name of the second class.
    :param needs_open_space: If True, the function should return False if either of the classes has reached enrollment
    capacity (regardless of whether or not the classes are compatible)
    :return: Returns True if the two given classes are compatible within the same schedule and False otherwise.
    """
    a1 = first_class.find(" ")
    a2 = first_class.find("-")
    b1 = second_class.find(" ")
    b2 = second_class.find("-")
    url1 = "http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + first_class[0: a1]
    url2 = "http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + second_class[0: b1]
    import urllib.request
    fstream1 = urllib.request.urlopen(url1)
    fstream2 = urllib.request.urlopen(url2)
    first_class_line = []
    second_class_line = []
    for row1 in fstream1:
        row1 = row1.decode("utf-8")
        cell1 = row1.strip().split("|")
        if cell1[1] == first_class[a1 + 1:a2] and cell1[2] == first_class[a2 + 1:]:
            first_class_line = cell1
    for row2 in fstream2:
        row2 = row2.decode("utf-8")
        cell2 = row2.strip().split("|")
        if cell2[1] == second_class[b1 + 1:b2] and cell2[2] == second_class[b2 + 1:]:
            second_class_line = cell2
    if needs_open_space:
        if int(first_class_line[15]) == int(first_class_line[16]) or int(first_class_line[15]) > int(first_class_line[16]):
            return False
        if int(second_class_line[15]) == int(second_class_line[16]) or int(second_class_line[15]) > int(second_class_line[16]):
            return False
    for each in range(1,6):
        if first_class_line[6 + each] == second_class_line[6 + each]:
            if int(first_class_line[12]) <= int(second_class_line[13]) <= int(first_class_line[13]):
                return False
            elif int(first_class_line[12]) <= int(second_class_line[12]) <= int(first_class_line[13]):
                return False
            else:
                return True
        else:
            return True