import unittest
import casino.montecarlo as mc

class MonteCarloTestSuite(unittest.TestCase):
    #Die
    def test_1_change_weight(self):
        test_die1 = mc.Die([1,2,3,4])
        print(test_die1._Die__datastore)
        test_die1.change_weight(1,21)
        self.assertEqual(test_die1._Die__datastore['weight'][0],21,'Values are equal')
        
    def test_2_roll(self):
        test_die2 = mc.Die([1,2,3,4])
        rolls = test_die2.roll(6)
        self.assertEqual(len(rolls), 6,'Values are equal')
        
    def test_3_show(self):
        test_die3 = mc.Die([1,2,3,4])
        print(test_die3.show())
    
    #Game
    def test_4_play(self):
        test_die4 = mc.Die(['H','T'])
        test_game4 = mc.Game([test_die4,test_die4,test_die4])
        test_game4.play(25)
        self.assertTrue(test_game4._Game__playdata.shape[0] == 25,'Check passed')
        
    def test_5_show(self):
        test_die5 = mc.Die(['H','T'])
        test_game5 = mc.Game([test_die5,test_die5,test_die5])
        test_game5.play(25)
        print(test_game5.show('N')[:5])
           
    #Analyzer
    def test_6_jackpot(self):
        test_die6 = mc.Die(['H','T'])
        test_game6 = mc.Game([test_die6,test_die6,test_die6])
        test_game6.play(1)
        test_game6.show()
        test_analysis6 = mc.Analyzer(test_game6)
        print(test_analysis6.jackpot())
        
    def test_7_combo(self):
        test_die7 = mc.Die(['H','T'])
        test_game7 = mc.Game([test_die7,test_die7,test_die7])
        test_game7.play(5)
        test_game7.show()
        test_analysis7 = mc.Analyzer(test_game7)
        print(test_analysis7.combo())
    
        
    def test_8_face_count(self):
        test_die8 = mc.Die(['H','T'])
        test_game8 = mc.Game([test_die8,test_die8,test_die8])
        test_game8.play(5)
        test_game8.show()
        test_analysis8 = mc.Analyzer(test_game8)
        print(test_analysis8.face_count)

        
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)