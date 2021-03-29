import parentheses

class TestParent():
    def test_check_1(self):
        assert parentheses.check('>]]])(<>)(){}}]') == False        
    def test_check_2(self):
        assert parentheses.check('[{sgfdgs([[[<dfgsdfg>]]])(<>)(){}}]') == True      
    def test_check_3(self):
        assert parentheses.check(']()(){<>}[[()]]') == False      
    def test_check_4(self):
        assert parentheses.check('{[][[]]]}') == True
    def test_check_1(self):
        assert parentheses.check('{{}{}}{{{{{}}}}}}}}{{}}}}') == False            
