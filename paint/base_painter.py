from abc import ABC, abstractmethod


class BasePainter(ABC):
    def __init__(self, model_dir_path :str, model_path :str):
        self.model_dir_path = model_dir_path
        self.model_path = model_path
        
    @abstractmethod
    def draw(self, prompt :str):
        pass