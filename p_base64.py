#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import argparse
import string

"""
    The application for encrypting and decrypting data.

    Example command:
        encode: python p_base64.py --encode text_example (Result: dGV4dF9leGFtcGxl)
        decode: python p_base64.py --encode dGV4dF9leGFtcGxl (Result: text_example)


    :package     PythonBase64

    :author      Shamsudin Serderov
    :url         https://www.steein.ru

    :copyright   2017 - Steein Inc
"""


class Base64Object(object):
    def __init__(self, encode, decode, author):
        self._encode = self._normalize(encode)  # encode
        self._decode = self._normalize(decode)  # decode
        self._copyright = self._normalize(author)
        self.__go_base()

    @staticmethod
    def _normalize(name):
        return name

    @staticmethod
    def __len(name):
        return len(name)

    """
        Encryption Base64
        The default setting:  b64encode (utf-8)

        :return string
    """

    @staticmethod
    def encode_base(message) -> string:
        return base64.b64encode(message.encode('utf-8'))

    """
        Decryption Base64
        The default setting:  b64decode

        :return string
    """

    @staticmethod
    def decode_base(message) -> string:
        return base64.b64decode(message)

    """
        Processing of information received
    """

    def __go_base(self):
        if self.__len(self._encode) > 0:
            print(self.encode_base(self._encode))

        if self.__len(self._decode) > 0:
            print(self.decode_base(self._decode))


"""
    Configure console commands
"""


def main():
    arg_parser = argparse.ArgumentParser(
        argument_default='-h',
        description='The application for encrypting and decrypting data',
        epilog='Copyright: Shamsudin Serderov (https://www.steein.ru)',
    )

    arg_parser.add_argument('author', action="store_true", default=False,
                            help='Developer Information.')

    arg_parser.add_argument('--encode', action="store", type=str, default='',
                            help='Enter the text to encrypt')

    arg_parser.add_argument('--decode', action="store", type=str, default='',
                            help='Enter the text to decrypt')

    args = arg_parser.parse_args()

    Base64Object(
        encode=args.encode,
        decode=args.decode,
        author=args.author
    )


"""
    Run Process
"""
if __name__ == '__main__':
    main()
