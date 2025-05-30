from .constants import ELECTRON_CHARGE, PROTON_CHARGE, PROTON_MASS, NEUTRON_MASS, ELECTRON_MASS
from .calculations import calculate_specific_charge, calculate_compton_wavelength
from abc import ABC


class Particle(ABC):
    def __init__(self, name, mass, charge=0):
        self.name = name
        self.mass = mass
        self.charge = charge

    def __repr__(self):
        pass

    @property
    def specific_charge(self):
        return calculate_specific_charge(self.mass, self.charge)

    @property
    def compton_wavelength(self):
        return calculate_compton_wavelength(self.mass)


class Electron(Particle):
    def __init__(self):
        super().__init__("Электрон", ELECTRON_MASS, ELECTRON_CHARGE)

    def __repr__(self):
        pass


class Proton(Particle):
    def __init__(self):
        super().__init__("Протон", PROTON_MASS, PROTON_CHARGE)

    def __repr__(self):
        pass


class Neutron(Particle):
    def __init__(self):
        super().__init__("Нейтрон", NEUTRON_MASS, 0)

    def __repr__(self):
        pass
