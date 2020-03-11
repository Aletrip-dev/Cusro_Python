elif sys.platform == 'darwin':
    settings['libraries'].append('iodbc')
    settings['libraries'].append('odbc')
    
