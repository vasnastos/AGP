import unittest as ut
import classRPS as cr

class Test(ut.TestCase):
    def test_game1(self):
        game=cr.rps()
        game.standard_moves('R','S')
        self.assertTrue(int(game.playerwins)>int(game.computerwins),msg="TestCase:1 Assert:1 Fail")
        game.standard_moves('P','S')
        self.assertEqual(int(game.playerwins),int(game.computerwins),msg="TestCase:1 Assert:2 Fail")
        game.standard_moves('R', 'S')
        game.standard_moves('P', 'P')
        game.standard_moves('S', 'P')
        self.assertTrue(int(game.playerwins)==3,msg="TestCase:1 Assert:3 Fail")
        self.assertEqual(int(game.computerwins),1,msg="TestCase:1 Assert:4 Fail")
        self.assertGreater(int(game.playerwins),int(game.computerwins),msg="TestCase:1 Assert:4 Fail")
        self.assertTrue(str(game.playermove)=='S',msg="TestCase:1 Assert:5 Fail")
        self.assertTrue(str(game.computermove)=='P',msg="TestCase:1 Assert:6 Fail")

if __name__ == '__main__':
    ut.main()
