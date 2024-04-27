import json
# Open the file in read mode
file_path = "/Users/lemengwang/Downloads/CUB_200_2011/CUB_200_2011/attributes/image_attribute_labels.txt" 
list_of_list = [[] for _ in range(313)] 
try:
    with open(file_path, 'r') as file:
        print("Contents of the file:")
        # Read the file line by line
        for line in file:
            # Split each line into individual values
            values = line.strip().split()  # Assuming values are separated by spaces, change split(',') for comma separation
            # Process each value (in this example, just printing them)
            image_id = int(values[0])
            attribute_id = int(values[1])
            is_present = int(values[2])
            certainty_id = int(values[3])
            if is_present != 0:
                list_of_list[attribute_id].append(image_id)
            # print("Values on this line:", values)
    i = 0
    for s in list_of_list:
        print(i,'\n')
        print(*s,'\n')
        i = i + 1

    # Convert the list of lists to JSON format
    json_data = json.dumps(list_of_list, indent=4)

    # Write the JSON data to a file
    output_json_file = "/Users/lemengwang/Downloads/CUB_200_2011/CUB_200_2011/speration.json"  # Specify the path for the output JSON file
    with open(output_json_file, 'w') as json_file:
        json_file.write(json_data)

    print(f"JSON data has been written to '{output_json_file}'.")

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
