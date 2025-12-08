class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents
        self._input_string = self._title + " " + self._contents
        self._input_list = self._input_string.split(" ")
        self._current_read_index = 0

    def format(self):
        return f"{self._title}: {self._contents}"

    def count_words(self):
        return len(self._input_list)

    def reading_time(self, wpm):
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        _words_readable = int(wpm * minutes)
        _start_index = self._current_read_index
        _end_index = _start_index + _words_readable

        if _end_index > self.count_words():
            chunk_as_list = self._input_list[_start_index:]
            output_chunk = " ".join(chunk_as_list)
            self._current_read_index = 0
            return output_chunk
        else:
            chunk_as_list = self._input_list[_start_index:_end_index]
            output_chunk = " ".join(chunk_as_list)
            self._current_read_index = _end_index
            return output_chunk

