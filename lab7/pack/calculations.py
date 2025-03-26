from .constants import SPEED_OF_LIGHT, PLANCK_CONSTANT


def calculate_specific_charge(mass, charge):
    return charge / mass


def calculate_compton_wavelength(mass):
    return PLANCK_CONSTANT / (mass * SPEED_OF_LIGHT)