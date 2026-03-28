class SpatialObject:

    def effective_area(self):
        """
        Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError

class Parcel (SpatialObject):

class Building (SpatialObject):

class Road (SpatialObject):