from a_computer_builder import AComputerBuilder
from b_computer_builder import BComputerBuilder
from director import Director

builder_1 = AComputerBuilder()
d = Director(builder_1)
d.build_computer()
computer = d.get_computer()
computer.display()

builder_2 = BComputerBuilder()
d = Director(builder_2)
d.build_computer()
computer = d.get_computer()
computer.display()