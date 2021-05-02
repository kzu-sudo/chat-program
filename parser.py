#!/usr/bin/python3

import argparse

class parser(object):

    @classmethod
    def parse(self) -> list:

        parser = argparse.ArgumentParser(
            add_help = True,
            description = "A simple chat program"
        )

        parser.add_argument(
            "-i", "--ip", action="store", type=str, required=True,
            help="Ip of client or server"
        )

        parser.add_argument(
            "-p", "--port", action="store", type=int, required=True,
            help="Port of client or server"
        )


        parser.add_argument(
            "-k", "--key", action="store", type=str, required=True,
            help="Enter the key which is used to encrypt the messages"
        )

        parser.add_argument('--client-mode', dest='option', action='store_true')
        parser.add_argument('--server-mode', dest='option', action='store_false')
        parser.set_defaults(option=True)

        return_value = {}
        args = parser.parse_args()

        try:
            return_value["host"] = args.ip
            return_value["port"] = args.port
            return_value["option"] = args.option
            return_value["key"] = args.key

        except:
            parser.print_help()
            SystemExit

        return return_value
