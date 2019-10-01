'''
Copyright (c) 2019, Ryder, rydercoding@hotmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import serial

class AtCommand:
    def __init__(self):
        self.ser = None

    def open(self, port, rd_timeout=1):
        # Open searil port
        self.ser = serial.Serial(port, timeout=rd_timeout)

    def close(self):
        # Close searil port
        self.ser.close() 

    def send_at(self, cmd):
        cmd_ex = cmd + '\r\n'
        print 'Sending ' + cmd + ' ...'
        self.ser.write(cmd_ex)

    def check_at_resp(self, exp_str, max_size=200):
        '''
        It reads AT response and checks if there is any error.
        All AT response string will be returned if no error, otherwise
        None will be returned.
        '''
        ret = self.ser.read_until(exp_str + '\r\n', max_size)
        if not exp_str in ret:
            print "Actual AT response is: ", ret, "\nBut expected response is: ", exp_str
            ret = None
        return ret

    def parse_at_resp(self, targ_str, at_resp):
        '''
        It extracts the line including target string, then return the string after target string
        at the same line.
        None will be returned in case of any error
        '''
        for cur_line in at_resp.split('\r\n'):
            if targ_str in cur_line:
                # Remove leading and trailing whitespace chars and target string          
                return cur_line.replace(targ_str, '').strip()
        else:
            return None

# Instance of the AtCommand class intended to be shared. 
defaultAt = AtCommand()

if __name__ == "__main__":
    test_at = AtCommand()
    test_at.open('COM12')
    
    # Pass case for check_at_resp
    test_at.send_at('AT+COPS?')
    print test_at.check_at_resp('OK')
    # Error case for check_at_resp
    test_at.send_at('AT+COPS?')
    print test_at.check_at_resp('OK1')
    # Pass case for parse_at_resp
    test_at.send_at('ATI')
    print test_at.parse_at_resp('Revision:', test_at.check_at_resp('OK'))
    # Error case for parse_at_resp
    test_at.send_at('ATI')
    print test_at.parse_at_resp('Revision1:', test_at.check_at_resp('OK'))
    
    test_at.close()
