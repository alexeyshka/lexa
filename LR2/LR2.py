import random
from LR2_json import load_json

# Создание списков с объектами класса оборудования, объектами класса КЗ
equipment, short_circuits, circuit_breakers = load_json()

faulted_equipment = equipment[random.randint(0, len(equipment)-1)]
short_circuit_type = short_circuits[random.randint(0, len(short_circuits)-1)]
short_circuit_type.set_target(faulted_equipment.get_name())

print(short_circuit_type)
