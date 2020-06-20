import re

ZIP_PATTERN = re.compile(r'(?P<zip_code>\d+),(?P<cc>[a-z]{2})')
LL_PATTERN = re.compile(r'(?P<lat>-*\d+\.\d+),(?P<lon>-*\d+\.\d+)')
