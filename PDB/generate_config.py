#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import utils


def main():
    data = utils.load_data(__file__)
    utils.generate_config(__file__, data)


if __name__ == "__main__":
    main()
