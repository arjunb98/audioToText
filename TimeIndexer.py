import translator
class TimeIndexer:

    def __init__(self):
        self.translator = translator.Translator()
        self.files = []
        self.file_audio = {}

    def add_file(self, file_path):
        self.files.add(file_path)
        self.translator.set_audio(file_path)
        self.file_audio[file_path] = self.translator.audio_data

    def get_time_stamp(self, audio_path, query):
        return self.translator.get_timestamp(query,self.file_audio[audio_path])


if __name__ == '__main__':
    TI = TimeIndexer()
    TI.add_file('./testAudio/fullTestAudio2.mp3')
    TI.add_file('./testAudio/bpn5min.mp3')
    query = input()
    while query != '':
        print(TI.get_time_stamp('./testAudio/fullTestAudio2.mp3', query))
        query = input()