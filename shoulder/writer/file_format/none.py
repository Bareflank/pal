from shoulder.writer.file_format.file_format import FileFormatWriter


class NoneFileFormatWriter(FileFormatWriter):

    def write_newline(self, outfile, count=1):
        pass

    def write_indent(self, outfile, count=1):
        pass
