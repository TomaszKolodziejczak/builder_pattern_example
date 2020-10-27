from dataclasses import dataclass

from abc_computer_builder import AbcComputerBuilder


@dataclass
class BComputerBuilder(AbcComputerBuilder):

    def set_computer_version(self):
        """Set computer version"""
        self._computer.version = "B"

    def get_case(self):
        self._computer.case = "Plastic Case"

    def get_mainboard(self):
        self._computer.mainboard = "alpha 100"
        self._computer.cpu = "AMD"
        self._computer.memory = "4GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_disc = "64GB"