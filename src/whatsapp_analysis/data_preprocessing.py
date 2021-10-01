import re
import pandas as pd

def starts_with_date_and_time(s):
    '''
    Check if a string starts with date and time
    '''
    pattern = '^([0-9]+).([0-9]+).([0-9]+) klo ([0-9]+).([0-9]+) -' 
    result = re.match(pattern, s)
    if result:
        return True
    return False

def split_line(line):
    '''Split line into four variables: date, time, author, and message'''
    splitLine = line.split(' - ')
    dateTime = splitLine[0]
    date, time = dateTime.split(' klo ')
    message = ' '.join(splitLine[1:])
    if find_author(message):
        splitMessage = message.split(': ')
        author = splitMessage[0]
        message = ' '.join(splitMessage[1:])
    else:
        author = None
    return date, time, author, message

def find_author(s):
    '''Check if a string includes an author'''
    patterns = [
        '([\w]+):',                        # First Name
        '([\w]+[\s]+[\w]+):',              # First Name + Last Name
        '([\w]+[\s]+[\w]+[\s]+[\w]+):',    # First Name + Middle Name + Last Name
        '([\w]+)[\u263a-\U0001f999]+:',    # Name and Emoji              
    ]
    pattern = '^' + '|'.join(patterns)
    result = re.match(pattern, s)
    if result:
        return True
    return False

def import_data(data_path):
    '''Import Whatsapp data and transform it to a Pandas dataframe'''
    parsed_data = []

    with open(data_path, encoding = 'utf-8') as fp:
        message_buffer = []
        date, time, author = None, None, None
        while True:
            line = fp.readline()
            if not line:
                break
            line = line.strip()
            if starts_with_date_and_time(line):
                if len(message_buffer) > 0:
                    parsed_data.append([date, time, author, ' '.join(message_buffer)])
                message_buffer.clear()
                date, time, author, message = split_line(line)
                message_buffer.append(message)
            else:
                message_buffer.append(line)
            
        df = pd.DataFrame(parsed_data, columns = ['date', 'time', 'author', 'message'])
        df['date'] = pd.to_datetime(df['date'], format = '%d.%m.%Y')

        return df