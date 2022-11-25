#!/usr/bin/env python

import subprocess
import webbrowser


def main():
	subprocess.call('docker-compose build', shell=True)
	subprocess.call('docker-compose up -d', shell=True)
	webbrowser.open('http://127.0.0.1:8000/api/auto/')
	webbrowser.open('http://127.0.0.1:8000/api/swagger-ui/')


if __name__ == '__main__':
	main()
