from shoulder.writer.file_format.file_format import FileFormatWriter


class WindowsFileFormatWriter(FileFormatWriter):

    def write_newline(self, outfile, count=1):
        for i in range(count):
            outfile.write("\r\n")

    def write_indent(self, outfile, count=1):
        for i in range(count):
            outfile.write("\t")
