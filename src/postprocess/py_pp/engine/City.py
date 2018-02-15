class City:
    """ Class City:
    
    Class representing a city, it is defined by its name and the coordinates 
    of two points at two ends of the city. It allows the creation of a grid of
    smaller cells which have two lists: the list of the users having their
    umbrella open and the list of the users having their umbrella closed. It's
    a convenient way to place the users on the map in these sort of
    neighborhoods.

    Currently under development!

    Attributes:
        name (str): name of the city
        nwLat (float): latitude of the North West point
        nwLong (float): longitude of the North West point
        seLat (float): latitude of the South East point
        seLong (float): longitude of the South East point
    """

    def __init__(self, name, nwLat, nwLong, seLat, seLong):
        """ Constructor of City:

        Initializes the attributes of the class.

        Args:
            name (str): name of the city
            nwLat (float): latitude of the North West point
            nwLong (float): longitude of the North West point
            seLat (float): latitude of the South East point
            seLong (float): longitude of the South East point
        """
        self.name = name
        self.nwLat = nwLat
        self.nwLong = nwLong
        self.seLat = seLat
        self.seLong = seLong

        