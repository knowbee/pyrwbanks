import unittest
from rw_banks import getBank, getBanks,banks

class TestRwbanks(unittest.TestCase):

    def test_getbanks(self):
        self.assertEqual(getBanks(), banks)
    def test_getbank(self):
        bank = {
                "name": "BANK OF KIGALI LIMITED",
                "swift_code": "BKIGRWRW",
                "bank_code": "BKIG",
                "address": "KN 4 Ave, Kigali, Rwanda",
                "postal_code": "175",
                "phone_number": "+250788143000",
                "toll_free": "4455",
                "email_address": "bk@bk.rw",
                "ussd_code": "*334#"
            }
        self.assertEqual(getBank("BKIGRWRW"), bank)
    def test_getnone(self):
        self.assertEqual(getBank("BKIG"), None)
if __name__ == '__main__':
    unittest.main()
