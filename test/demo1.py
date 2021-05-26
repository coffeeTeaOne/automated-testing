
import ddt



@ddt.ddt
class TestProfile():
    @ddt.file_data(r'C:\Users\lyial\Desktop\testing\automated-testing\test\config\test.yaml')
    def test_profile(self, **case_data):
           print(case_data)

if __name__ == '__main__':
    TestProfile().test_profile()

