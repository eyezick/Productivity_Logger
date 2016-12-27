import time

print("""
______                   _               _    _         _  _            _
| ___ \                 | |             | |  (_)       (_)| |          | |
| |_/ / _ __   ___    __| | _   _   ___ | |_  _ __   __ _ | |_  _   _  | |      ___    __ _   __ _   ___  _ __
|  __/ | '__| / _ \  / _` || | | | / __|| __|| |\ \ / /| || __|| | | | | |     / _ \  / _` | / _` | / _ \| '__|
| |    | |   | (_) || (_| || |_| || (__ | |_ | | \ V / | || |_ | |_| | | |____| (_) || (_| || (_| ||  __/| |
\_|    |_|    \___/  \__,_| \__,_| \___| \__||_|  \_/  |_| \__| \__, | \_____/ \___/  \__, | \__, | \___||_|
                                                                 __/ |                 __/ |  __/ |
                                                                |___/                 |___/  |___/
""")
time.sleep(2)
print('Welcome! This program will log your self-reported level of productivity. You will be helped by one of eight different logger personalities.\n\n')
time.sleep(5)
interval = input('\nEnter how long in minutes, you\'d like the check-in interval to be, default is 25 minutes. \n\nPick any positive number or just enter anything else for default. \n')
 # interval had to be on this file to avoid circular dependencies, as the text feedback references the interval variable, and the main file references the text
try:
    if interval.isdigit():
            if int(interval) <= 0:
                    interval = 25
            else:
                interval = int(interval)
    elif float(interval) % 1 == 0:
        interval = int(float(interval))
    else:
        if len(interval) > 4:
            interval = float("{0:.2f}".format(float(interval)))
        else:
            interval = float(interval)
except ValueError:
    interval = 25

# above block is input validation for interval variable, printing floats only if there are decimal places, and limiting decimal places to 2 if more are provided

spanish = ['Que pasa amigo? Quieres productividad? ', 'Por supuesto! Empezamos, vuelvo in {} minutos.'.format(interval), 'Como fue su rendimiento en una escala de 0 a 100?','Muy bien! Lo me gusta mucho, volveremos en {} minutos de nuevo!'.format(interval), 'No creo en este que es tan malo. Lo intentamos de nuevo en {} minutos.'.format(interval), 'Adios mi amigo!']
british = ['ello there! What a grand, productive time we will have today. Shall we commence?', 'Excellent. I\'ll be drinking my tea, and will await your return in {} minutes.'.format(interval), 'How have we conducted ourselves in productivity, rating from 0-100?', 'Top drawer sir! I am pleased with your productivity. Let us reconvene in {} minutes.'.format(interval), 'Well the British Empire wasn\'t built in a day. Let us try again.', 'Until the next time my chap.']
russian = ['Hello Comrade, in Soviet Russia, productivity brings you!', 'I am sure you will bring great honor of productiveness to the motherland. Return in {} minutes.'.format(interval),'What is the performance comrade? In a number 0 to 100 of course.', 'Very very good! We shall drink to your productivity. Come back in {} minutes.'.format(interval), 'Oh comrade, surely you can do better. Let us try once more.', 'Farewell comrade!']
robot = ['Beep. Boop.\nI will track your self-reported productivity scores at set intervals.', 'Please do not set 0 for any scores as it will cause my stack to overflow.\nLogging function to commence in {} minutes.'.format(interval), 'Please input your self-reported productivity score (0-100) into my productivity matrix.', 'Your reported productivity is high. Please reward yourself with a nutritious and wholesome beverage later. Logging to resume in {} minutes.'.format(interval), 'Your reported productivity is low. Please utilize a tool to dig deeper within yourself for your next attempt.', 'Powering myself down...']
cowboy = ['Howdy my productive pardner!' , 'Y\'all ready to track your sweet, sweet productivity? See you in {} minutes!'.format(interval), 'How\'d we do on productivity, from 1 to 100 \'o course, do ya reckon?', 'That them there productivity is mighty fine. Keep it goin\', be back in {} minutes.'.format(interval), 'I am mighty disappointed, let\'s try again in {} minutes.'.format(interval), 'So long pardner!']
trump = []
yoda = ['Greetings young Padawan.', 'Great productivity, you seek. Meet again in {} minutes, we will.'.format(interval), 'Report your level of productivity, you will, on a scale of to 100.', 'Powerful you are becoming, productivity I sense in you. Further confirm in {} minutes, I will.'.format(interval), 'Do or do not, there is no try. Do better you will.', 'Goodbye Chewbacca, miss you I will']
pirate = ['What be happenin\', Matey?', 'No quarter! Ready to git productive? Report aft in {} minutes.'.format(interval), 'How productive have ye been on a scale from 1 to 100?', 'Fine job, that is a very good report. See ye again in {} minutes'.format(interval), 'Blimey! Surely ye can do better, let\'s try one more time.', 'Yo-ho-ho goodbye you scallywag!' ]

profiles = [spanish,british, robot, cowboy, russian, yoda, pirate]
