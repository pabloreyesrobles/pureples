class Substrate(object):

    def __init__(self, input_coordinates, output_coordinates, hidden_coordinates=(), res=10.0, coordinates=()):
        self.input_coordinates = input_coordinates
        self.hidden_coordinates = hidden_coordinates        
        self.output_coordinates = output_coordinates
        self.res = res

        # Modular substrate
        self.coordinates = coordinates

