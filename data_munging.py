# import pandas as pd

with open("weather.dat",'r') as file:
    data_positions = []
    whitespace = True
    first_line = True
    for line in file:
        if first_line == True:
            first_line = False
            for i in range(len(line)):
                char = line[i]
                if char == " " and whitespace == False:
                    whitespace = True
                elif char != " " and whitespace == True:
                    data_positions.append(i)
                    whitespace = False
    # print(data_positions)
        else:
            pass



# df = pd.read_csv("weather.dat", delim_whitespace=True)
# print(df.to_string())


# print(df.columns)