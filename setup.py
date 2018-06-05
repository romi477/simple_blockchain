from cx_Freeze import setup, Executable

executables = [Executable(r'C:\Users\roma\PycharmProjects\simple_blockchain\main.py')]

setup(name='datacreator',
      version='0.0.1',
      description='my datacreator',
      executables=executables
)