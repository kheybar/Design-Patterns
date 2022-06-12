from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
        This class is State class
    """
    @abstractmethod
    def mousedown(self):
        pass

    @abstractmethod
    def mouseup(self):
        pass


class BrushTool(BaseTool):
    """
        This class is Concrete State class
    """
    def mousedown(self):
        return 'Brush icon'

    def mouseup(self):
        return 'Draw a line'


class SelectionTool(BaseTool):
    """
        This class is Concrete State class
    """
    def mousedown(self):
        return 'Selection icon'

    def mouseup(self):
        return 'Draw a dashed rectangle'


class Canvas:
    """
        This class is Context class
    """
    def set_current_tool(self, tool):
        self.current_tool = tool()

    def mousedown(self):
        return self.current_tool.mousedown()

    def mouseup(self):
        return self.current_tool.mouseup()


a = Canvas()
a.set_current_tool(SelectionTool)
print(a.mousedown())
print(a.mouseup())

a.set_current_tool(BrushTool)
print(a.mousedown())
print(a.mouseup())
