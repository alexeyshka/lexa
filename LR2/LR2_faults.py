from LR2_equipment import Equipment
import random

class Faults:
    def __init__(self, probability, self_extinct, target=None):
        self.__probability = probability
        self.__self_extinct = self_extinct
        self.__target = target
        if target:
            self.base_current = 1000 if Equipment.get_by_name(target).get_voltage() == 330 else 500

    def get_probability(self):
        return self.__probability
    def get_self_extinct(self):
        return self.__self_extinct
    def get_target(self):
        return self.__target

    def set_target(self, target):
        self.__target = target

    # Метод для вывода всех атрибутов класса
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_probability()}, voltage={self.get_self_extinct()}, current={self._get_extra_repr()}, target = {self.get_target()})"

    # Геттер атрибутов наследуемых классов. В них он переписан
    def _get_extra_repr(self):
        """Child classes override this to add their attributes"""
        return ""

class OnePhaseFault(Faults):
    def __init__(self, probability, self_extinct, target=None):
        super().__init__(probability, self_extinct, target)
        self.__current = random.uniform(self.base_current * 0.5, self.base_current * 1.0) if target else 0

    def _get_extra_repr(self):
        return self.__current
    def get_current(self):
        return self.__current

class TwoPhaseFault(Faults):
    def __init__(self, probability, self_extinct, target=None):
        super().__init__(probability, self_extinct, target)
        self.__current = random.uniform(self.base_current * 0.8, self.base_current * 1.2) if target else 0

    def _get_extra_repr(self):
        return self.__current

class ThreePhaseFault(Faults):
    def __init__(self, probability, self_extinct, target=None):
        super().__init__(probability, self_extinct, target)
        self.__current = random.uniform(self.base_current * 1.0, self.base_current * 1.4) if target else 0

    def _get_extra_repr(self):
        return self.__current

class TurnToTurnFault(Faults):
    def __init__(self, probability, self_extinct, target=None):
        super().__init__(probability, self_extinct, target)
        self.__current = random.uniform(self.base_current * 0.4, self.base_current * 0.8) if target else 0

    def _get_extra_repr(self):
        return self.__current
