class parser:
    def parseFile(file_dir):
        file_data=open(file_dir, 'r');
        parsed_data = file_data.split()
        return parsed_data