from LR2_equipment import Transformer, CircuitBreaker, Line, Bus
from LR2_faults import OnePhaseFault, TwoPhaseFault, ThreePhaseFault, TurnToTurnFault
import json

def load_json():
    with open('test.json', 'r') as file:
        data = json.load(file) # Создает словарь с данными из файла

    equipment_list = []
    cicuitbreakers_list = []
    faults_list = []
    # Итерация по всем элементам словаря 'Equipment'. При его отсутствии возвращает пустой словарь
    for class_type, class_items in data.items():
        if class_type == 'Equipment':
            for object_type, object_values in class_items.items():
                #print(object_type, object_values)
                for object_data in object_values.items():
                    obj = globals()[object_type](**object_data[1])
                    equipment_list.append(obj)
        if class_type == 'CircuitBreaker':
            for object_type, object_values in class_items.items():
                obj = globals()[class_type](**object_values)
                cicuitbreakers_list.append(obj)
        if class_type == 'Faults':
            for object_type, object_values in class_items.items():
                obj = globals()[object_type](**object_values)
                faults_list.append(obj)

    return equipment_list, faults_list, cicuitbreakers_list
