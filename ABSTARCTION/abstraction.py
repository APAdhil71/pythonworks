from abc import ABC 
from abc import abstractmethod
class Editor(ABC):
    @abstractmethod
    def create_module_and_package(self):
        pass
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def debug(self):
        pass

class VsCode(Editor):
    def create_module_and_package(self):
        print("vs code create and module")
    def edit(self):
        print("vscode edit")
    def debug(self):
        print("vscode debug")

editor_instance=VsCode()
editor_instance.debug()
editor_instance.create_module_and_package()
editor_instance.edit()