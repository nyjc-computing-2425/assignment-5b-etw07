# Part 1
def read_csv(filename):
  """takes a csv file and returns the headers and each following line in the form of a nestled string"""
  # Type your code below
  data = []
  header = []
  f = open(filename,'r')
  for line in f:
    x = line.strip().split(",")
    temp = []
    for i in range(len(x)):
      if x[i].isdigit():
        temp.append(int(x[i]))
      else:
        temp.append(str(x[i]))
    data.append(temp)
  header = data.pop(0)
  return (header,data)
  pass


# Part 2
def filter_gender(enrolment_by_age, sex):
  """returns filtered data from students of the requested gender"""
  # Type your code below
  data = []
  for x in enrolment_by_age:
    if x[2] == sex:
      x.pop(2)
      data.append(x)
  if data[0][2] == "enrolment_jc":
    data = data.remove(0)
  return data
  pass


# Part 3
def sum_by_year(enrolment):
  """returns a nested list containing each year and the total enrolment for that year"""
  # Type your code below
  dyn_year = 0
  data = []
  for x in enrolment:
    if x[0] == dyn_year:
      data[-1][-1] = data[-1][-1] + int(x[2])
    elif x[0] != dyn_year and str(x[0]).isdigit():
      dyn_year = int(x[0])
      data.append([dyn_year,0])
      data[-1][-1] = data[-1][-1] + int(x[2])
  return data
  pass


# Part 4
def write_csv(filename, header, data):
  """creates a new csv file and returns the number of lines in the file"""
  # Type your code below
  data_file = open(filename,'w')
  x = len(header)
  head = ""
  for i in range(x):
    head += header[i]
    if i != x:
      head += ","
  data_file.write(head)
  data_file.write("\n")
  counter = 1
  for i in data:
    temp_string = ""
    for x in i:
      temp_string += str(x)
      if x != i:
        temp_string += ","
      elif x == i:
        temp_string += "\n"
        counter += 1
    data_file.write(temp_string)
  data_file.close()
  return counter
  pass


# TESTING
# You can write code below to call the above functions
# and test the output
