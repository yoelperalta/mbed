"""
mbed SDK
Copyright (c) 2011-2013 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from host_test import Test, DefaultTest
from sys import stdout

class DevNullTest(DefaultTest):

    def print_result(self, result):
       print "\n{%s}\n{end}" % result

    def run(self):
        test_result = True
        c = self.mbed.serial.read(512)
        print "Received %d bytes" % len(c)
        if "{failure}" not in c:
            self.print_result('success')
        else:
            self.print_result('failure')
        stdout.flush()

if __name__ == '__main__':
    DevNullTest().run()
