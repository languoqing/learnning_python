import pytest

class TestCaseCollection:
    
    def checkStatus(self):
        pass
    
    def checkValue(self):
        pass
    
    @pytest.fixture()
    def upTestCaseValue(self):
        pass
    
    @pytest.mark.usefixtures()
    def downTestCase(self):
        pass