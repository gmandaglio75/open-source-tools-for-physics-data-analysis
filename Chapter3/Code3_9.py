import math
        if not isinstance(radius, (int, float)):
            raise TypeError("The radius must be a number.")
        if radius < 0:
            raise ValueError("The radius cannot be negative.")
        self.__radius = float(radius)  
￼
    def set_angular_velocity(self, angular_velocity):
        if not isinstance(angular_velocity, (int, float)):
            raise TypeError("The angular velocity must be a number.")
        if angular_velocity < 0:
            raise ValueError("The angular velocity cannot be negative.")
        self.__angular_velocity = float(angular_velocity) 
￼
    # Calculation methods
    def calculate_tangential_velocity(self):
        return self.__angular_velocity * self.__radius
￼
    def calculate_centripetal_acceleration(self):
        return self.__radius * (self.__angular_velocity ** 2)
￼
    def calculate_period(self):
        if self.__angular_velocity == 0:
            raise ValueError("The angular velocity must be nonzero to calculate the period.")
        return 2 * math.pi / self.__angular_velocity
￼
    # Getter methods for private variables
    def get_radius(self):
        return self.__radius
￼
    def get_angular_velocity(self):
        return self.__angular_velocity
￼
    def __str__(self):
        """
        Textual representation of the UniformCircularMotion object.
        """
        return f"UniformCircularMotion(radius={self.__radius}, angular_velocity={self.__angular_velocity})"
￼
# Example usage of the class
if __name__ == "__main__":
    try:
        # User input
        radius = float(input("Enter the radius (in meters): "))
        angular_velocity = float(input("Enter the angular velocity (in radians per second): "))
￼
        # Creating an object of the class
        motion = UniformCircularMotion(radius, angular_velocity)
￼
        # Calculations
        print(f"Motion object: {motion}")
        print("Tangential velocity:", motion.calculate_tangential_velocity(), "m/s")
        print("Centripetal acceleration:", motion.calculate_centripetal_acceleration(), "m/s^2")
        print("Period:", motion.calculate_period(), "s")
￼
        # Example using setters
        motion.set_radius(10)
        motion.set_angular_velocity(3)
        print(f"Motion object after setters (after modification): {motion}")
        print("Tangential velocity (after modification):", motion.calculate_tangential_velocity(), "m/s")
        print("Centripetal acceleration (after modification):", motion.calculate_centripetal_acceleration(), "m/s^2")
        print("Period (after modification):", motion.calculate_period(), "s")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")
    except Exception as e:
        print(f"An error occurred: {e}")
