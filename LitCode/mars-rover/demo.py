from MarsRover import MarsRover

def parse_input(input_file: str):
    counter = 0
    output = []

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for index, line in enumerate(lines):
        line.strip()
        if index == 0:
            upper_right_coordinates = line.split()
            top_right_coordinates = {
                "x": int(upper_right_coordinates[0]),
                "y": int(upper_right_coordinates[1])
            }
            mars_rover = MarsRover(top_right_coordinates)
        if index % 2 == 1:
            coordinates = line.split()
            x = int(coordinates[0])
            y = int(coordinates[1])
            orientation = coordinates[2]
            counter += 1
        if index % 2 == 0 and index > 0:
            instructions = line.split()
            instructions = instructions[0]
            counter += 1

        if counter == 2:
            position = mars_rover.deploy_rover(x, y, orientation, instructions)

            x = position['x']
            y = position['y']
            rover_orientation = position['orientation']
            output.append(f'{x} {y} {rover_orientation} \n')
            counter = 0
    
    return output

def write_output(output_filename: str, output: list[str]):
    with open(output_filename, 'w') as f:
        for line in output:
            f.write(line)


output = parse_input('input.txt')
write_output('output.txt', output)