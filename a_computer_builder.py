from dataclasses import dataclass

from abc_computer_builder import AbcComputerBuilder


@dataclass
class AComputerBuilder(AbcComputerBuilder):

    def set_computer_version(self):
        self._computer.version = "A"

    def get_case(self):
        self._computer.case = "Transparent Case"

    def get_mainboard(self):
        self._computer.mainboard = "XYZ 500"
        self._computer.cpu = "AMD Ryzen"
        self._computer.memory = "32GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_disk = "Seagate 256GB"
