import sys, os
print(sys.path[:5])
print('cwd', os.getcwd())
print('exists app', os.path.exists('app'))
