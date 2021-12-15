import load_files 
import load_user
import log_in
import register
import purchase_game
import rent_game
import add_game
import main 
import unittest
import unittest.mock

class register_test(unittest.TestCase):
 @patch (register.register, username_input ="jaja")
 def registration_fail_test(self):
     self.assertstd.out "Username has been taken, please select another"

 @patch (register.register, username_input ="baba")
 def registration_pass_test(self):
     self.assertEqual check is true 
 end

if __name__ == '__main__':
    unittest.main()