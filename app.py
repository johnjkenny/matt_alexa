#!/usr/bin/env python3 


from multiprocessing import Process
from time import sleep
from os import getpid


class Listener():
    def __init__(self, loop_listen: bool = True):
        self.loop_listen = loop_listen
        self.wakeup_key = None # add actual wake up key/word here

    def listen_for_wakeup_key_in_loop(self):
        print('loop listener started with pid: {}'.format(getpid()))
        count = 1 # added for testing purposes
        while self.loop_listen:
            print('Searching for wakeup word. Count: {}'.format(count))
            if self.search_for_wakeup_key():
                self.run_user_command()
            sleep(5) # add sleeper for testing
            count += 1

    def run_user_command(self):
        # listen to audio for what command to run and run the needed
        pass

    def search_for_wakeup_key(self):
        audio = self.get_audio()
        if audio:
            return self.parse_audio_for_search_case(audio, self.wakeup_key)
        return False

    def get_audio(self):
        audio = None
        # code to handle the audio intake in block sizes
        yield audio

    @staticmethod
    def parse_audio_for_search_case(audio: bytearray, search_case: bytearray):
        if search_case in audio: # search if search_case is found in audio snip
            return True
        return False


class Alexa2dot0():
    def __init__(self):
        self.listener = Listener()
        self.loop_process = None

    def run_loop_listener(self):
        print('start loop listener')
        self.listener.loop_listen = True
        self.loop_process = Process(target=self.listener.listen_for_wakeup_key_in_loop)
        self.loop_process.start()

    def end_loop_listener(self):
        print('stopping loop listener')
        self.listener.loop_listen = False
        self.loop_process.terminate()
        self.loop_process.join()


if __name__ == '__main__':
    alexa = Alexa2dot0()
    print('starting module with pid: {}'.format(getpid()))
    alexa.run_loop_listener()  # start loop listener 
    sleep(60) # add sleeper for testing
    alexa.end_loop_listener() # end loop listener
    print('ending module')
