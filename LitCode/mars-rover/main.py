class MarsRover:
    # (1, 2) N
    # L M L M L M L M M
    def __init__(self) -> None:
        self.navigation = {
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

    def navigate(self, x: int, y: int, orientation: str, instructions: list[str]):
        rover_orientation = orientation
        
        for ch in instructions:
            if ch == 'L' or ch == 'R':
                rover_orientation = self.navigation[rover_orientation][ch]
            else:
                if rover_orientation == 'W':
                    x -= 1
                if rover_orientation == 'E':
                    x += 1
                if rover_orientation == 'N':
                    y += 1
                if rover_orientation == 'S':
                    y -= 1

        print(x, y, rover_orientation)


MarsRover().navigate(3, 3, 'E', 'MMRMMRMRRM')
