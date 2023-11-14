class MarsRover:
    # (1, 2) N
    # L M L M L M L M M
    def __init__(self, top_right_coordinates) -> None:
        """
        Initializes the compass directions with mappings for 90 degrees 
        to the left or right of each compass direction
        """
        self.top_right_coordinates = top_right_coordinates
        self.compass = {
            'N' : {
                'L' : 'W', 
                'R' : 'E'
            },
            'W' : {
                'L' : 'S', 
                'R' : 'N'
            },
            'S' : {
                'L' : 'E', 
                'R' : 'W'
            },
            'E' : {
                'L' : 'N', 
                'R' : 'S'
            }
        }

    def deploy_rover(self, x: int, y: int, orientation: str, instructions: str) -> dict:
        """
        Moves the rover based on the instructions provided.

        Parameters:
            x: x coordinate position of rover
            y: y coordinate position of rover
            orientation: Compass direction where rover is facing
            instructions: Directions for rover to follow
        Return:
            final_position (dict): Contains the final coordinates and orientation of the rover
        """
        rover_orientation = orientation

        for instruction in instructions:
            if instruction == 'L' or instruction == 'R':
                rover_orientation = self.compass[rover_orientation][instruction]
            else:
                if rover_orientation == 'W':
                    x -= 1
                if rover_orientation == 'E':
                    x += 1
                if rover_orientation == 'N':
                    y += 1
                if rover_orientation == 'S':
                    y -= 1

        if x > self.top_right_coordinates['x'] or x < 0:
            raise ValueError

        if y > self.top_right_coordinates['y'] or y < 0:
            raise ValueError

        final_position = {
            'x': x,
            'y': y,
            'orientation': rover_orientation
        }

        return final_position

